"""
Papers with Code dataset
For tracking the lastest AI research papers
"""

import os

urls = """
https://paperswithcode.com/media/about/papers-with-abstracts.json.gz
https://paperswithcode.com/media/about/links-between-papers-and-code.json.gz
https://paperswithcode.com/media/about/evaluation-tables.json.gz
https://paperswithcode.com/media/about/methods.json.gz
""".split()

def download():
    """ downloand and unzip into PPWC """
    os.mkdir('PPWC')
    for url in urls:
        fname = url.split('/')[-1]
        jname = fname[:-3]
        os.system(f"wget {url}")
        os.system(f"gunzip {fname}")
        os.system(f"mv {jname} PPWC")
