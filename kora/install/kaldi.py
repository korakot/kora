"""
Kaldi is a library for Speech Recognition
"""
import os

# Just extract from my custom tar. Very fast (17s)
url = 'https://github.com/airesearch-in-th/kora/releases/download/v0.7/kaldi.tar.gz'
os.system(f"curl -L {url} | tar xz -C /")

# Add paths to binaries
paths = [''] + """
/opt/kaldi/src/bin
/opt/kaldi/src/featbin
/opt/kaldi/src/fstbin
/opt/kaldi/src/gmmbin
/opt/kaldi/tools/openfst/bin
""".split()

os.environ['PATH'] += ':'.join(paths)
