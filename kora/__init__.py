import sys
from pkg_resources import get_distribution

def get_ver(package):
    return get_distribution(package).version

__version__ = get_ver('kora')


from fastcore.imports import IN_COLAB

# for %edit
if IN_COLAB:
    import kora.files
