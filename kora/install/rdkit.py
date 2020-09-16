"""
RDKit is a library for Cheminformatics and Machine Learning
"""
import os

# Just extract from my custom tar. Very fast (1.7s)
url = 'https://github.com/airesearch-in-th/kora/releases/download/v0.6/rdkit.tar.gz'
os.system(f"curl -L {url} | tar xz -C /")
