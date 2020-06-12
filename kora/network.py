import os

os.system('pip install pyvis')
import pyvis
from pyvis.network import *

class Network(pyvis.network.Network):
    """ Same as pyvis but change for Colab notebook """

    def __init__(self, *args, **kwargs):
        kwargs['notebook'] = True
        super().__init__(*args, **kwargs)

    def _repr_html_(self):
        nodes, edges, height, width, options = self.get_network_data()
        html = self.template.render(height=height, width=width, 
                                    nodes=nodes, edges=edges, 
                                    options=options)
        return html