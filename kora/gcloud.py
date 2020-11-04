"""
Convenient tools that call gcloud or gsutil
or work with Google Cloud Platform
"""
import os


def config(project='kora-id'):
    os.system(f"gcloud config set project {project}")

def login():
    os.system('gcloud auth login')

