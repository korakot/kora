"""
TTC dataset

Thai Textbook Corpus(TTC) contains word list and frequencies.
"""
import os
import pandas as pd
from urllib.request import urlretrieve

def load_data(path='ttc_freq_extra.csv'):
    url = 'https://github.com/korakot/thainlp/raw/master/ttc_freq_extra.csv'
    if not os.path.exists(path):
        urlretrieve(url, path)
    return pd.read_csv(path)
