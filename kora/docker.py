"""
Use docker in Colab, by manual pull and extract
"""

import os
import json
import tarfile
from IPython import get_ipython
from kora.tree import convert, _TEMPLATE

# install docker-pull
os.system("wget https://raw.githubusercontent.com/sdenel/docker-pull/master/docker-pull")
os.system("chmod +x docker-pull")
os.system("mv docker-pull /usr/local/bin")


def pull(fullname):
    if fullname.count('/')==0:
        fullname = 'library/'+fullname
    if fullname.count('/')==1:
        fullname = 'index.docker.io/'+fullname
    target = '/tmp/' + fullname.split('/')[-1]
    cmd = f'docker-pull {fullname} {target}'
    print('> '+cmd)
    get_ipython().system(cmd)  # show progress
    return DockerTar(target)

  
class DockerTar:
    """
    Manage extraction and visualization of a docker tarfile
    Usage:
    > pkg = docker.pull('org/pkg')
    > pkg.extract('*', target='/')
    """
    def __init__(self, file_path):
        self.path = file_path
        self.extract_config()
        self.extract_viz()
    
    def extract_config(self):
        """ get config and layers"""
        tar = tarfile.open(self.path)
        mf = json.load(tar.extractfile('./manifest.json'))[0]
        cfg = './' + mf['Config']
        self.config = json.load(tar.extractfile(cfg))
        self.layers = [l.split('/')[0] for l in mf['Layers']]
        tar.close()

    def extract_viz(self):
        root = {}
        prefix = '/root/.docker-pull-layers-cache/sha256_'
        for layer in self.layers:
            tar = tarfile.open(prefix + layer)
            root[layer] = {}
            for mem in tar.getmembers():
                if mem.isdir(): continue
                node = root[layer]
                for part in mem.name.split('/'):
                    if part not in node:
                        node[part] = {}
                    node = node[part]
            tar.close()
        data = convert(root, False)
        self.viz_data = json.dumps(data)

    def _repr_html_(self):
        """ fancytree of docker layers """
        return _TEMPLATE % self.viz_data

    def extract(self, pattern, target='.', lay=None):
        """
        Extract files by pattern (can be just a file path)
        They are copied to a target directory
        If `lay` is given, it is used to extract from that layer by its prefix.
        """
        for layer in self.layers:
            if lay and not layer.startswith(lay):
                continue  # only look at this layer, if given
            self.extract_layer(layer, pattern, target)

    def extract_layer(self, layer, pattern, target):
        prefix = '/root/.docker-pull-layers-cache/sha256_'
        os.system(f"tar xf {prefix+layer} -C {target} --wildcards '{pattern}' ")
