""" Utility functions not available in google.colab.drive
    Mainly use pydrive
"""
from os.path import basename
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