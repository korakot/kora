"""
Allow using normal Jupyter Notebook and Jupyter Lab in Colab
"""

import os
os.system("pip install jupyterlab")
from kora import ngrok


def start(lab=False):
    url = ngrok.connect(8888).public_url
    if not lab:
        url += '/tree'  # normal jupyter notebook
    os.system("jupyter lab --ip=0.0.0.0&")
    print(url)


def stop():
    ngrok.kill()
    os.system("pkill jupyter-lab")
