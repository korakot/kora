from urllib.request import urlretrieve
from matplotlib import *  # font_manager, ft2font, rc


def add_thai_font():
    url = 'https://raw.githubusercontent.com/korakot/kora/40a2bb269383501965c0745055f1ad4f23e167a3/THSarabunChula.ttf'
    add_font(url)

add_font_thai = add_thai_font

def add_font(url):
    if url.startswith('http'):
        filename = urlretrieve(url)[0]  # in /tmp/...
    else:
        filename = url   # already manual download to colab
    name = get_font_name(filename)
    font_manager.fontManager.addfont(filename)
    set_font(family=name)     # select this font automatically


def get_font_name(filename):
    font = ft2font.FT2Font(filename)
    return font.family_name


def set_font(**kw):
    rc('font', **kw) # family, size