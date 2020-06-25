""" What bs4 should have been """

from bs4 import BeautifulSoup
import requests 
from os.path import splitext


def Soup(s, features='lxml', **kw):
    """ A fake class, of what BeautifulSoup should have been 
    
    It accepts a url or a file, in addition to html/xml as usual
    """
    if s.startswith('http'):
        src = requests.get(s).text
        return BeautifulSoup(src, features, **kw)
    if splitext(s)[1] in ('.html', '.xml'):
        src = open(s).read()
        return BeautifulSoup(src, features, **kw)
    return BeautifulSoup(s, features, **kw)