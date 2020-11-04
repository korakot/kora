"""
Convenient tools that call gcloud or gsutil
or work with Google Cloud Platform
"""
import os
from IPython import get_ipython

sh = get_ipython().system


def config(project='kora-id'):
    sh(f"gcloud config set project {project}")


def login():
    sh('gcloud auth login')


def list_projects():
    """ List all projects associated with this account """
    sh('gcloud projects list')


def list_services(available=False):
    """ List enabled services. Or all available services.
    """
    cmd = "gcloud services list"
    if available:
        cmd += " --available"
    sh(cmd)


def enable(service):
    """ enable service, which can be listed above """
    if not service.endswith('.googleapis.com'):
        service += '.googleapis.com'
    sh(f'gcloud services enable {service}')


def upload(fname, target='gcs://kora-data'):
    """ Target can be your own gcs, and can rename the file too.
    Default target is kora's gcs which is publicly writable (auto-delete everyday)
    """
    sh(f"gsutil cp {fname} {target}")
