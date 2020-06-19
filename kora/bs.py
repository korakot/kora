""" What bs4 should have been """

from bs4 import BeautifulSoup
import requests 


def Soup(s, features='lxml', **kw):
    """ A fake class, of what BeautifulSoup should have been 
    
    It accepts a url or a file, in addition to html/xml as usual
    """
    if s.startswith('http'):
        src = requests.get(s).text
        return BeautifulSoup(src, features, **kw)
    if s.startswith('/') or s.startswith("."):
        src = open(s).read()
        return BeautifulSoup(src, features, **kw)
    return BeautifulSoup(s, features, **kw)