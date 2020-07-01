import os
from importlib import import_module


def install(name, package_name=None):
    """ Try to import library, but may need to pip-install first 
    
    It's a lazy import/install. If it's already installed, calling this is fast.
    Try will just import it as normal.
    """
    try:
        return import_module(name)
    except:
        if package_name is None:  # could be different too
            package_name = name  
        os.system("pip install " + package_name)
        return import_module(name)
