"""
Allow using normal Jupyter Notebook and Jupyter Lab in Colab
"""

import os
os.system("pip install jupyterlab")
os.system("pip install pyngrok")
from pyngrok import ngrok


def start(lab=False):
    url = ngrok.connect(port=8888)
    url = url.replace('http://','https://')
    if not lab:
        url += '/tree'  # normal jupyter notebook
    os.system("nohup jupyter lab --no-browser --allow-root --ip=0.0.0.0&")
    print(url)


def stop():
    os.system("pkill ngrok")
    os.system("pkill jupyter-lab")
