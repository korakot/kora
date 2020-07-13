"""
SCB-MT-EN-TH

SCB Machine Translation Dataset
More than 1 millions sentence pairs
"""

import os

def download():
    url = "https://github.com/vistec-AI/dataset-releases/releases/download/scb-mt-en-th-2020_v1.0/scb-mt-en-th-2020.zip"
    print("Start downloading: .. ")
    os.system(f"wget {url}")
    os.system(f"unzip -j scb-mt-en-th-2020.zip")
    print("""\
  There are 12 files:
    task_master_1.csv                 Chat dialog to achieve a task
    generated_reviews_translator.csv  Reviews translated by translators
    generated_reviews_yn.csv          Reviews checked by translators
    generated_reviews_crowd.csv	      Reviews translated by crowd-sourcing
    nus_sms.csv                       SMS messages (crowd-source)
    msr_paraphrase.csv                Microsoft paraphrase (crowd-source)
    mozilla_common_voice.csv          Mozilla Common Voices ASR (crowd-source)
    assorted_government.csv           Bilingual government documents
    thai_websites.csv                 Bilingual Top-500 Thai websites (crawling)  
    paracrawl.csv                     Selections from Paracrawl
    wikipedia.csv                     Selections from Wikipedia
    apdf.csv                          Asia Pacific Defence Forum""")
