import os

os.system('wget -qO libta.deb https://launchpad.net/~mario-mariomedina/+archive/ubuntu/talib/+files/libta-lib0_0.4.0-oneiric1_amd64.deb')
os.system('wget -qO ta.deb https://launchpad.net/~mario-mariomedina/+archive/ubuntu/talib/+files/ta-lib0-dev_0.4.0-oneiric1_amd64.deb')
os.system('dpkg -i libta.deb ta.deb')
os.system('rm libta.deb ta.deb')
os.system('pip install ta-lib')

from talib import *
# maybe I should move this talib.py to kora/talib.py instead
# people can then just use 'from kora import talib' to both install & import