""" Utility functions not available in google.colab.drive
    Mainly use pydrive
"""

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
    f = get_file(filename)
    f.SetContentFile(filename)
    f.Upload()
    f.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})
    return 'https://drive.google.com/uc?id=' + f.get('id')  # direct link
