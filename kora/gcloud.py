"""
Convenient tools that call gcloud or gsutil
or work with Google Cloud Platform
"""
import os
from IPython import get_ipython

shell = get_ipython().system

def config(project='kora-id'):
    os.system(f"gcloud config set project {project}")

def login():
    shell('gcloud auth login')

