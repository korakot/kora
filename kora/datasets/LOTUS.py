"""
LOTUS Speech Corpus for ASR, by NECTEC
Licensed under CC-BY-NC-SA
"""

import os


def download():
    url = "https://github.com/korakot/corpus/releases/download/v1.0/AIFORTHAI-LotusCorpus.zip"
    print("NECTEC licensed LOTUS under CC-BY-NC-SA")
    print("Start downloading: .. ")
    os.system(f"wget {url}")
    os.system("unzip AIFORTHAI-LotusCorpus.zip")
    os.system("rm AIFORTHAI-LotusCorpus.zip")
    os.system("mv LOTUS-CD-FREE LOTUS")  # rename
    print("Finished")
