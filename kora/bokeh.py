""" Make bokeh easier to use in Colab
"""

from bokeh import *
from bokeh import io, plotting
from bokeh.plotting import figure  


def _fig_repr_html(self):
    """ Figure can display itself """
    from bokeh.io.notebook import load_notebook
    from bokeh.embed.notebook import notebook_content
    from IPython.display import publish_display_data

    load_notebook(hide_banner=True)
    (script, div, cell_doc) = notebook_content(self)
    EXEC_MIME = 'application/vnd.bokehjs_exec.v0+json'
    publish_display_data({'application/javascript': script, EXEC_MIME: ""},
                        metadata={EXEC_MIME: {"id": self.id}})
    return div

plotting.Figure._repr_html_ = _fig_repr_html
