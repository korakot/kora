""" What bs4 should have been """
import os
os.system("pip install beautifulsoup4 -U") # 4.9 for advanced selector
from bs4 import BeautifulSoup, Tag
import requests 
from pathlib import Path


def Soup(s, features='lxml', **kw):
    """ A fake class, of what BeautifulSoup should have been 
    
    It accepts a url or a file, in addition to html/xml as usual
    """
    if isinstance(s, Path):
        src = s.read_text()
    elif s.startswith('http'):
        src = requests.get(s).text
    elif Path(s).exists():
        src = open(s).read()
    else:
        src = s
    return BeautifulSoup(src, features, **kw)


Tag.select1 = Tag.select_one
