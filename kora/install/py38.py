import os
os.system("pip install pyngrok")
from pyngrok import ngrok

# install anaconda3
os.system("wget -O ac.sh https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")
os.system("bash ./ac.sh -b")
os.symlink("/usr/local/lib/python3.6/dist-packages/google",
           "/root/anaconda3/lib/python3.8/site-packages/google")
# start jupyter
os.system("/root/anaconda3/bin/jupyter-lab --ip=0.0.0.0&")

# and show URL
url = ngrok.connect(8888)
print(url.replace('http','https')+'/tree')
