"""
BEST dataset

For thai word segmentation
"""
import os
from urllib.request import urlretrieve


def download():
    base = 'http://www.nectec.or.th/corpuso/phocadownload/dl_text_thai-eng/BEST/TrainingSet/'
    genres = ['article', 'encyclopedia', 'news', 'novel']
    print("Start downloading: .. ")
    for genre in genres:
        url = base + genre + '.zip'
        fname, _ = urlretrieve(url)
        os.system(f'unzip {fname}')
        print(genre, end=' .. ')
    print('\nThe results are in these 4 folders')
    return genres
