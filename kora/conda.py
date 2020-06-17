# make installing with conda easier
# from kora import conda
# conda.install('packagename')

# first install miniconda like
# !wget -O mini.sh https://repo.anaconda.com/miniconda/Miniconda3-4.3.21-Linux-x86_64.sh 
# !chmod +x mini.sh
# !bash ./mini.sh -b -f -p /usr/local

# also add path
# import sys
# sys.path.insert(5, '/usr/local/lib/python3.6/site-packages')

# then install and add python==3.6 to allow it to work with colab
# !conda install -q -y --prefix /usr/local python=3.6 # add your_library
# can set channel as well inside {params}

import os, sys

os.system('wget -O mini.sh https://repo.anaconda.com/miniconda/Miniconda3-4.3.21-Linux-x86_64.sh')
os.chmod('mini.sh', 0o777)
os.system("./mini.sh -b -f -p /usr/local")
sys.path.insert(5, '/usr/local/lib/python3.6/site-packages')
os.system("conda config --add channels conda-forge")

def install(params: str) -> None:
    print("Use this command:")
    print(f'!conda install -q -y --prefix /usr/local {params} python=3.6')