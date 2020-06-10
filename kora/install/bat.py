import os
from IPython.core.magic import register_line_magic

os.system('wget -qO bat.deb https://github.com/sharkdp/bat/releases/download/v0.15.4/bat_0.15.4_amd64.deb')
os.system('dpkg -i bat.deb')
os.remove('bat.deb')

# set default display in the config file
os.makedirs('/root/.config/bat')
with open('/root/.config/bat/config', "w") as f:
    f.write('''
--theme="ansi-light"
--wrap=never
''')

@register_line_magic
def bat(line):
    get_ipython().system('bat '+line)
