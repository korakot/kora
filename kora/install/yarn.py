"""
Yarn is used to develop front-end webapp
"""
import os

os.system('curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -')
os.system('echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list')
os.system('apt update')
os.system('apt install yarn')
