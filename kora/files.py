"""
To replace google.colab.files
Add files.edit(filepath) and %edit
"""
from pathlib import Path
from IPython.core.magic import register_line_magic
from google.colab.files import *  # upload, download, view


@register_line_magic
def edit(filepath):
    """
    This can be used as files.edit(fname) or %edit fname
    """
    path = Path(filepath)
    if not path.exists():
        path.touch()  # create empty
    view(path)
