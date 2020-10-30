"""
TSync1 Speech Corpus for TTS, by NECTEC
Licensed under CC-BY-NC-SA
"""

import os


def download():
    url = "https://github.com/korakot/corpus/releases/download/v1.0/TSync1Corpus.zip"
    print("NECTEC licensed TSync1 under CC-BY-NC-SA")
    print("Start downloading: .. ")
    os.system(f"wget {url}")
    os.system("unzip TSync1Corpus.zip")
    os.system("rm TSync1Corpus.zip")
    print("Finished")
