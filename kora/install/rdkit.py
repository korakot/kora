"""
RDKit is a library for Cheminformatics and Machine Learning
"""
import os


# 2018 is much faster (6 secs), so, skip 2020 for now
# If there's a problem with 2018 version, will revert to 2020

# Need libboost 1.67 for rdkit > 2018.09.1
# os.system("add-apt-repository -y ppa:hnakamur/boost")
# os.system("add-apt-repository -y ppa:hnakamur/icu")
# os.system("apt update")
# Don't know why, but cannot install just libboost-dev
# os.system("apt install libboost-python1.67.0 libboost-serialization1.67.0" 
#     " libboost-system1.67.0 libboost-regex1.67.0 libboost-iostreams1.67.0")

# Install RDKit, extracted from Anaconda package
# url = "https://anaconda.org/rdkit/rdkit/2020.03.3.0/download/linux-64/rdkit-2020.03.3.0-py36hc20afe1_1.tar.bz2"
# os.system(f"curl -L {url} | tar xj lib")
# os.system("mv lib/python3.6/site-packages/rdkit /usr/local/lib/python3.6/dist-packages/")
# os.system("mv lib/*.so.* /usr/lib/x86_64-linux-gnu/")
# os.system("rm -r lib")   # clean up

url = 'https://anaconda.org/rdkit/rdkit/2018.09.1.0/download/linux-64/rdkit-2018.09.1.0-py36h71b666b_1.tar.bz2'
os.system(f"curl -L {url} | tar xj lib")
os.system("mv lib/python3.6/site-packages/rdkit /usr/local/lib/python3.6/dist-packages/")
x86 = '/usr/lib/x86_64-linux-gnu'
os.system(f"mv lib/*.so.* {x86}/")
os.system(f"ln -s {x86}/libboost_python3-py36.so.1.65.1 {x86}/libboost_python3.so.1.65.1")
os.system("rm -r lib")
