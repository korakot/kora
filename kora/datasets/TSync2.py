"""
TSync2 Speech Corpus for TTS, by NECTEC
Licensed under CC-BY-NC-SA
"""

import os


def download():
    url = "https://github.com/korakot/corpus/releases/download/v1.0/AIFORTHAI-TSync2Corpus.zip"
    print("NECTEC licensed TSync2 under CC-BY-NC-SA")
    print("Start downloading: .. ")
    os.system(f"wget {url}")
    os.system("unzip AIFORTHAI-TSync2Corpus.zip")
    os.system("rm AIFORTHAI-TSync2Corpus.zip")
    print("Finished")
