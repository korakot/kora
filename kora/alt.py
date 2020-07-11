import json
from altair import *
from altair import vega
from vega_datasets import data
from vega_datasets.core import Dataset

vega.Vega.renderers.enable('colab')  # allow vega display


# Adding data.thailand.url to Altair
data._datasets['thailand'] = 'thailand'

Dataset._dataset_info['thailand'] = {
    "filename": "thailand-topo.json",
    "format"  : "json",
    "is_local": False,
}

class Thailand(Dataset):
    """ Need to create a subclass to be searched and included 
    """
    name = "thailand"
    _return_type = dict
    
    def __init__(self, name):
        Dataset.__init__(self, name)
        self.url = 'https://raw.githubusercontent.com/korakot/thailand-hex-map/master/data/thailand-topo.json'

    def __call__(self, use_local=False, **kwargs):
        __doc__ = super(Thailand, self).__call__.__doc__  
        return json.loads(self.raw(use_local=use_local).decode(), **kwargs)
