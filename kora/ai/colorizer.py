"""
From InstColorization
Github: github.com/ericsujw/InstColorization
Colab: colab.to/ericsujw/InstColorization/InstColorization.ipynb

Simplified into a function call
"""
import os
from os import listdir
from os.path import join, isfile, isdir
from urllib.request import urlretrieve
import sys
import numpy as np
import cv2
import PIL
import torch

import warnings

warnings.simplefilter("ignore")
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


# Install InstColorization
print("Installing InstColorization")
os.system("npx degit ericsujw/InstColorization inst")
sys.path.append('/content/inst')  # allow import
# Load checkpoint
print("Loading Colorization model")
os.system("wget https://github.com/airesearch-in-th/kora/releases/download/v0.9/colorization_checkpoints.zip")
os.system("unzip colorization_checkpoints.zip")
os.system("rm colorization_checkpoints.zip")


# Install Detectron
print("Installing Detectron2")
os.system("pip install pyyaml -U")  # 5.1+
os.system("pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/index.html")
PIL.TiffTags.IFD = 13   # instead of restart

print("Loading Detectron2 model")
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)


# Create directories
for d in 'example example_bbox results'.split():
  os.makedirs(d, exist_ok=True)
input_dir = "example"
output_npz_dir = "example_bbox"


# Importing InstColorization
from options.train_options import TestOptions
from models import create_model
from fusion_dataset import Fusion_Testing_Dataset
from util import util
import multiprocessing
multiprocessing.set_start_method('spawn', True)

torch.backends.cudnn.benchmark = True

sys.argv = [sys.argv[0]]  # clear options ?
opt = TestOptions().parse()
save_img_path = opt.results_img_dir

model = create_model(opt)
model.setup_to_test('coco_finetuned_mask_256_ffs')


def open(fname):
    # copy to input
    input_img = 'example/input.jpg'
    if fname.startswith('http'):
        urlretrieve(fname, input_img)
    else:
        os.system(f'cp {fname} {input_img}')
    # find bbox
    img = cv2.imread(input_img)
    lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(lab_image)
    l_stack = np.stack([l_channel, l_channel, l_channel], axis=2)
    outputs = predictor(l_stack)
    save_path = 'example_bbox/input'
    pred_bbox = outputs["instances"].pred_boxes.to(torch.device('cpu')).tensor.numpy()
    pred_scores = outputs["instances"].scores.cpu().data.numpy()
    np.savez(save_path, bbox = pred_bbox, scores = pred_scores)
    # load data
    dataset = Fusion_Testing_Dataset(opt, -1)
    dataset_loader = torch.utils.data.DataLoader(dataset, batch_size=opt.batch_size)
    data_raw = next(iter(dataset_loader))
    # predict colors
    data_raw['full_img'][0] = data_raw['full_img'][0].cuda()
    if data_raw['empty_box'][0] == 0:
        data_raw['cropped_img'][0] = data_raw['cropped_img'][0].cuda()
        box_info = data_raw['box_info'][0]
        box_info_2x = data_raw['box_info_2x'][0]
        box_info_4x = data_raw['box_info_4x'][0]
        box_info_8x = data_raw['box_info_8x'][0]
        cropped_data = util.get_colorization_data(data_raw['cropped_img'], opt, ab_thresh=0, p=opt.sample_p)
        full_img_data = util.get_colorization_data(data_raw['full_img'], opt, ab_thresh=0, p=opt.sample_p)
        model.set_input(cropped_data)
        model.set_fusion_input(full_img_data, [box_info, box_info_2x, box_info_4x, box_info_8x])
        model.forward()
    else:
        full_img_data = util.get_colorization_data(data_raw['full_img'], opt, ab_thresh=0, p=opt.sample_p)
        model.set_forward_without_box(full_img_data)
    model.save_current_imgs(join(save_img_path, data_raw['file_id'][0] + '.png'))
    # combine grey & color
    img = cv2.imread('example/input.jpg')
    lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, _, _ = cv2.split(lab_image)

    img = cv2.imread('results/input.png')
    lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    _, a_pred, b_pred = cv2.split(lab_image)
    a_pred = cv2.resize(a_pred, (l_channel.shape[1], l_channel.shape[0]))
    b_pred = cv2.resize(b_pred, (l_channel.shape[1], l_channel.shape[0]))

    color_image = cv2.cvtColor(np.stack([l_channel, a_pred, b_pred], 2), cv2.COLOR_LAB2BGR)
    return PIL.Image.fromarray(color_image[:,:,::-1])  # BGR -> RGB
