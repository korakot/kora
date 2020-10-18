"""
Python wrapper around `thpronun` (https://github.com/tlwg/thpronun)
Many thanks to P' Thep and P' Ott
"""
import os
import subprocess
from ast import literal_eval


# install thpronun to /usr/local/bin
url = 'https://github.com/airesearch-in-th/kora/releases/download/v0.7/thpronun.tar'
os.system(f'curl -L {url} | tar x -C /')


output_dict = {
    'roman': 'r',
    'thai': 't',
    'phonetic': 'p',
    'raw': 'w',
    'soundex': 's',
}

def g2p(word, output='phonetic', group=False):
    """ 
    From word to pronunication. You can set `output` to 
    - phonetic (default: equivalent to IPA)
    - roman (Royin romanization)
    - thai (Thai pronunication, easy to read)
    - soundex (for similarity search)
    - raw (internal format)

    For a long sentence, you may want to set `group` to True 
    to avoid too many possibilities.
    """
    output = output_dict.get(output, output)
    cmd = ['thpronun', '-'+output]
    if group:
        cmd.append('-g')
    cmd.append(word)
    res = subprocess.check_output(cmd)
    lines = res.decode().strip().split('\n')
    if group:
        return literal_eval(lines[1])
    else:
        return lines[1:]
