import os
os.system('apt install xattr')
from xattr import *

def get_id(filename):
    """ Google Drive FileID """
    x = xattr(filename)
    file_id = x.get('user.drive.id')
    return file_id.decode()  # b'' -> str