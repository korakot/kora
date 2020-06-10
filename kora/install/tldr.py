import os
from IPython.core.magic import register_line_magic

os.system('wget -qO tldr https://github.com/dbrgn/tealdeer/releases/download/v1.3.0/tldr-linux-x86_64-musl')
os.system('chmod +x tldr')
os.system('mv tldr /usr/local/bin')
os.system('tldr --update')  # need once

@register_line_magic
def tldr(line):
    get_ipython().system('tldr '+line)
