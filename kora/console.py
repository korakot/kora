"""
Open another tab for web console (command line)
"""
import os
from subprocess import Popen, PIPE


# Install
url = "https://github.com/gravitational/teleconsole/releases/download/0.4.0/teleconsole-v0.4.0-linux-amd64.tar.gz"
os.system(f"curl -L {url} | tar xz")  # download & extract
os.system("mv teleconsole /usr/local/bin/")  # in PATH

# Set PS1, directory
with open("/root/.bashrc", "a") as f:
    f.write('PS1="\e[1;36m\w\e[m# "\n')
    f.write("cd /content \n")


def start():
    """ start the teleconsole, and print URL """
    process = Popen("teleconsole", shell=True,
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
    for i in range(6):
        line = process.stdout.readline()
    url = line.decode().strip().split()[-1]
    print("Console URL:", url)


def stop():
    os.system("pkill teleconsole")

def restart():
    stop()
    start()
