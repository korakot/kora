""" make calling autoreload easier """

from importlib import reload    # -> from kora.autoreload import reload
from IPython import get_ipython


magic = get_ipython().run_line_magic
magic('load_ext', 'autoreload')
magic('autoreload', '2')