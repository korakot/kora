"""
Vega Wordcloud, with tooltips
"""
import os
from collections import Counter
from math import sqrt

os.system("pip install -U pyyaml")
from altair.vega import Vega
Vega.renderers.enable('colab')


mark_spec = {
    "type": "text",
    "from": {"data": "table"},
    "encode": {
        "enter": {
            "text": {"field": "word"},
            "fill": {"scale": "color", "field": "word"},
            "tooltip": {"field": "text"}
        },
    },
    "transform": [{
        "type": "wordcloud",
        "size": [500, 300],  # to fill
        "text": {"field": "text"},
        # "font": "Sarabun New"
        "fontSize": {"field": "datum.size"},
    }]
}


spec = {
    "name": "wordcloud",
    "width": 500,
    "height": 300,
    "data" : [{
        'name'  : 'table',
        'values': [], # to fill
    }],
    "scales": [{
        "name": "color",
        "type": "ordinal",
        "range": [],  # to fill
    }],
    "marks": [mark_spec],
}


def plot(words, height=300, width=500, 
              size=10, fmin=1, 
              colors=["#d5a928", "#652c90", "#939597"]):
    cnt = Counter(words)   # words can also be a Counter() or dict()
    values = []
    for k, v in cnt.items():
        if v < fmin: continue
        values.append({
            'word': k,
            'text': f"{k} - {v}",    # จะเปลี่ยน label ก็ได้
            'size': size*sqrt(v),
        })
    spec['data'][0]['values'] = values
    # other parameters
    spec['width'] = width
    spec['height'] = height
    spec['marks'][0]['transform'][0]['size'] = [width, height]
    spec['scales'][0]['range'] = colors
    return Vega(spec)
