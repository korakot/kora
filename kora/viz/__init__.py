"""
__init__.py contains only small viz I use frequently
"""
import pandas as pd
from collections import Counter

def histogram(data, name='num', **kw):
    """
    No binning, just a bar chart of Counter()
    **kw can be title, width, or range_x=(0,10)
    """
    import plotly.express as px
    items = Counter(data).items()
    df = pd.DataFrame(items, columns=[name, 'freq'])
    return px.bar(df, x=name, y='freq', **kw)
