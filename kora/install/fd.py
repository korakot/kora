import os

os.system('wget -qO fd.deb https://github.com/sharkdp/fd/releases/download/v8.1.1/fd_8.1.1_amd64.deb')
os.system('dpkg -i fd.deb')
os.remove('fd.deb')
