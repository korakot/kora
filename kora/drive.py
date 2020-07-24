""" Utility functions not available in google.colab.drive
    Mainly use pydrive
"""
import os
from os.path import basename
from pathlib import Path
from urllib.request import urlretrieve


def auth_drive():
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    from oauth2client.client import GoogleCredentials as GC
    from google.colab import auth
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GC.get_application_default()
    return GoogleDrive(gauth)


def get_file(filename):
    """ Get this file if exists
    Or create a new one. Does not support folder, at root only.
    """
    drive = auth_drive()
    q = f"title = '{filename}' and 'root' in parents"
    res = drive.ListFile({'q': q}).GetList()
    if res:
        fid = res[0]['id']
        return drive.CreateFile({'id': fid})
    else:
        return drive.CreateFile({'title': filename})


def upload_public(filename):
    """ Upload the file to Google Drive and set permission to public """
    f = get_file(basename(filename))
    f.SetContentFile(filename)
    f.Upload()
    f.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})
    return 'https://drive.google.com/uc?id=' + f.get('id')  # direct link


def download_folder(folder_id):
    """ I copy this one from my old code, use drive API directly (not pydrive) """
    # authenticate
    from google.colab import auth
    auth.authenticate_user()
    # get folder_name
    from googleapiclient.discovery import build
    service = build('drive', 'v3')
    folder_name = service.files().get(fileId=folder_id).execute()['name']
    # install library 
    url = 'https://github.com/segnolin/google-drive-folder-downloader/raw/master/download.py'
    path = '/usr/local/lib/python3.6/dist-packages/download.py'
    urlretrieve(url, path)
    # recursive download
    import download
    download.download_folder(service, folder_id, './', folder_name)
    return folder_name


def get_path(file_id, drive=None):
    """ Use file_id to get the file path in Google Drive """
    if drive is None:
        drive = auth_drive()
    f = drive.CreateFile({'id': file_id})
    name = f['title']
    if f['parents']:
      parent_id = f['parents'][0]['id'] 
      return get_path(parent_id, drive) / name
    else:
      return Path(name)


def current_notebook():
    """ Get the filename, file_id of this notebook """
    import requests
    d = requests.get('http://172.28.0.2:9000/api/sessions').json()[0]
    file_id = d['path'].split('=')[1]
    return d['name'], file_id


def chdir_notebook():
    """ Change directory to its location in Google Drive"""
    # first confirm that drive is mounted
    if not os.path.exists("/content/drive"):
        from google.colab.drive import mount
        mount("/content/drive")
    # then get the directory and change to it
    _, file_id = current_notebook()
    path = get_path(file_id)
    nb_dir = '/content/drive' / path.parent
    os.chdir(nb_dir)
    return nb_dir
