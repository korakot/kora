""" What bs4 should have been """

from bs4 import BeautifulSoup
import requests 


def Soup(s):
    """ A fake class, what BeautifulSoup should have been """
    if s.startswith('http'):
        src = requests.get(s).text
        return BeautifulSoup(src)
    if s.startswith('/') or s.startswith("."):
        src = open(s).read()
        return BeautifulSoup(src)
    return BeautifulSoup(s)