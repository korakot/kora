"""
Taken from dataprep.eda. Modified to work in Colab.
"""
import os
os.system("pip install dataprep")
from dataprep.eda import *
# from dataprep.eda import report


# def _report_repr_html_(self):
#     from bokeh.io.notebook import load_notebook
#     from bokeh.embed.notebook import notebook_content
#     load_notebook(hide_banner=True)
#     script, div, _ = notebook_content(self.to_render)
#     return f'{div}<script>{script}</script>'

# report.Report._repr_html_ = _report_repr_html_
