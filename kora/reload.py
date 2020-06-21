""" make calling autoreload easier """

# from importlib import reload    # probably don't need manual reload
from IPython import get_ipython


magic = get_ipython().run_line_magic
magic('load_ext', 'autoreload')
magic('autoreload', '2')  # on by default


def on():
    magic('autoreload', '2')

def off():
    magic('autoreload', '0')