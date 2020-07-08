"""
ORCHID dataset

For Thai POS tagging
"""
from urllib.request import urlretrieve
from kora.bs import Soup


def download():
    base = 'https://raw.githubusercontent.com/korakot/thainlp/master/'
    filenames = ['orchid_pos.txt', 'xmlchid.xml']
    for fname in filenames:
        url = base + fname 
        urlretrieve(url, fname)
    print('orchid_pos.txt : Pairs of word & pos')
    print('xmlchid.xml    : ORCHID converted to XML (by K. Vee)')
    return filenames

def list_docs():
    return Soup('xmlchid.xml').select('document')

def list_sents():
    return Soup('xmlchid.xml').select('sentence')

def list_words():
    return Soup('xmlchid.xml').select('word')
