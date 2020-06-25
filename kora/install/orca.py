import os
from urllib.request import urlretrieve
url = "https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage"
orca = '/usr/local/bin/orca'
urlretrieve(url, orca)
os.chmod(orca, 0o755)
os.system("apt install xvfb libgconf-2-4")