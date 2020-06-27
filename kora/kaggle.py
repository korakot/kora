import os
import pandas as pd
from io import StringIO
from subprocess import getoutput
from IPython import get_ipython
import kora.data_table


# check if mounted, or explain
assert os.path.exists('/content/drive'), "You need to mount the drive first"
# check if kaggle.json exists, or explain
assert os.path.exists('/content/drive/My Drive/kaggle.json'), \
       "You need to create API token and store it as kaggle.json in your drive"

# copy API token to Colab
os.makedirs('/root/.kaggle', exist_ok=True)  # ~/.kaggle
os.system("cp 'drive/My Drive/kaggle.json' /root/.kaggle/")
os.chmod('/root/.kaggle/kaggle.json', 0o600)


def _show_csv(csv):
    """ Help display as table"""
    buf = StringIO(csv)
    if csv.startswith('Warning:'):
        buf.readline()
    return pd.read_csv(buf)

def search(query):
    """ Search for dataset names that match query """
    cmd = 'kaggle datasets list -v -s '+query
    return _show_csv(getoutput(cmd))

def ls(dataset):
    """ List all files for this dataset name """
    cmd = 'kaggle datasets files -v '+dataset
    return _show_csv(getoutput(cmd))

def download(dataset, only=None):
    """ Download all dataset files, or only a specific file """
    opt_f = ("-f "+only) if only else ""
    cmd = f"kaggle datasets download {dataset} --unzip {opt_f}"
    get_ipython().system(cmd)  # display too
    if opt_f:  # rename it back correctly
        for fn in os.listdir():
            if fn.startswith("datasets") and fn.endswith(only):
                os.rename(fn, only)
