""" Make bokeh easier to use in Colab
"""

from bokeh import *
from bokeh import io, plotting


def figure(height=600, width=600, **kw):
    """ Set height, width easily """
    kw['height'] = height
    kw['width'] = width
    return plotting.figure(**kw)


def _fig_repr_html(self):
    """ Figure can display itself """
    from bokeh.io.notebook import load_notebook
    from bokeh.embed.notebook import notebook_content

    load_notebook(hide_banner=True)
    (script, div, cell_doc) = notebook_content(self)
    return f'{div}<script>{script}</script>'

plotting.Figure._repr_html_ = _fig_repr_html
