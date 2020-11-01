import os
from kora import ngrok

# install anaconda3
os.system("wget -O ac.sh https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")
os.system("bash ./ac.sh -b")
os.remove("ac.sh")
os.symlink("/usr/local/lib/python3.6/dist-packages/google",
           "/root/anaconda3/lib/python3.8/site-packages/google")

# start jupyter
os.system("/root/anaconda3/bin/jupyter-lab --ip=0.0.0.0&")
# auto add path for new notebooks
startup_fname = "/root/.ipython/profile_default/startup/startup.py"
with open(startup_fname, 'w') as f:
  f.write("import os; os.environ['PATH'] = '/root/anaconda3/bin:' + os.environ['PATH']")

# show URL
url = ngrok.connect(8888).public_url
print(url)
