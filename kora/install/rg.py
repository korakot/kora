import os
from IPython.core.magic import register_line_magic

os.system('wget -qO rg.deb https://github.com/BurntSushi/ripgrep/releases/download/12.1.1/ripgrep_12.1.1_amd64.deb')
os.system('dpkg -i rg.deb')
os.remove('rg.deb')

@register_line_magic
def rg(line):
    get_ipython().system('rg '+line)