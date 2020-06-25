from urllib.request import urlretrieve
from matplotlib import *  # font_manager, ft2font, rc


def add_thai_font():
    url = 'https://raw.githubusercontent.com/korakot/kora/40a2bb269383501965c0745055f1ad4f23e167a3/THSarabunChula.ttf'
    name = add_font(url)
    set_font(family=name, size=18)

add_font_thai = add_thai_font

def add_font(url: str) -> str:
    if url.startswith('http'):
        filename = urlretrieve(url)[0]  # in /tmp/...
    else:
        filename = url   # already manual download to colab
    name = get_font_name(filename)
    font_manager.fontManager.addfont(filename)
    return name


def get_font_name(filename: str):
    font = ft2font.FT2Font(filename)
    return font.family_name


def set_font(**kw):
    rc('font', **kw) # family, size


# set animation suitable for Colab
rc('animation', html='jshtml')


def use_svg(enable=True):
    """ Set figure_format to SVG """
    format = 'svg' if enable else 'png'
    magic = get_ipython().run_line_magic
    magic('config', f"InlineBackend.figure_format = '{format}'")