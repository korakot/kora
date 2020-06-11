import os
from IPython.core.magic import register_line_magic

os.system('wget -qO fd.deb https://github.com/sharkdp/fd/releases/download/v8.1.1/fd_8.1.1_amd64.deb')
os.system('dpkg -i fd.deb')
os.remove('fd.deb')

@register_line_magic
def fd(line):
    get_ipython().system('fd '+line)