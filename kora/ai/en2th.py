"""
Use AIResearch MT model easily
"""

import os

os.system('pip install sentencepiece')
os.system('pip install git+https://github.com/pytorch/fairseq@6f6461b')

from fairseq.models.transformer import TransformerModel


# download model
url = 'https://github.com/vistec-AI/model-releases/releases/download/SCB_1M%2BTBASE_v1.0/SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0.tar.gz'
system.os(f'curl -L {url} | tar xz')

model = TransformerModel.from_pretrained(
    model_name_or_path='SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0/models/',
    checkpoint_file='checkpoint.pt',
    data_name_or_path='SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0/vocab/',
    bpe='sentencepiece',
    sentencepiece_vocab='SCB_1M-MT_OPUS+TBASE_en-th_spm-spm_32000-joined_v1.0/bpe/spm.en.model'
)

# function en2th.translate
translate = model.translate
