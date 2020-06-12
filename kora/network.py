import os

os.system('pip install pyvis')
import pyvis
from pyvis.network import *

class Network(pyvis.network.Network):
    """ Same as pyvis but change for Colab notebook """

    def __init__(self, height=500, width=500, **kwargs):
        """ Allow integer as h, w and set notebook=True """
        if type(height)==int:
            height = '%dpx' % height
        if type(width)==int:
            width = '%dpx' % width
        kwargs['height'] = height
        kwargs['width']  = width
        kwargs['notebook'] = True
        super().__init__(**kwargs)

    def _repr_html_(self):
        nodes, edges, height, width, options = self.get_network_data()
        html = self.template.render(height=height, width=width, 
                                    nodes=nodes, edges=edges, 
                                    options=options)
        return html