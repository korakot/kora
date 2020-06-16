import os
from IPython import get_ipython

# need this fix first
os.environ["LD_PRELOAD"] = ""
os.system("apt remove libtcmalloc-minimal4")
os.system("apt install libtcmalloc-minimal4")
os.environ["LD_PRELOAD"] = "/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4.3.0"
os.system("dpkg -L libtcmalloc-minimal4")

# then install blender
url = "https://download.blender.org/release/Blender2.83/blender-2.83.0-linux64.tar.xz"
os.system(f"curl {url} | tar xJ")
os.system("ln -s /content/blender-2.83.0-linux64/blender /usr/local/bin/blender")
# show result
get_ipython().system("blender -v")