"""
Kaldi is a library for Speech Recognition
"""
import os

# Just extract from my custom tar. Very fast (17s)
url = 'https://github.com/airesearch-in-th/kora/releases/download/v0.7/kaldi.tar.gz'
os.system(f"curl -L {url} | tar xz -C /")
# Add openfst to path
os.environ['PATH'] += ':/opt/kaldi/tools/openfst/bin'
