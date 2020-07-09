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
        "rotate": {"field": "datum.angle"},
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
        'transform': [{
            "type": "formula", "as": "angle",
            "expr": "0"
        }]
    }],
    "scales": [{
        "name": "color",
        "type": "ordinal",
        "range": [],  # to fill
    }],
    "marks": [mark_spec],
}

angle2expr = {
    0: '0',
    45: "[-45, 0, 45][~~(random() * 3)]",
    90: "[0, 90][~~(random() * 2)]",
}


def plot(words, height=300, width=500, 
              size=10, fmin=1, angle=0,
              colors=["#d5a928", "#652c90", "#939597"]):
    """
    size: smallest font to show
    fmin: smallest frequency to show
    angle: 0, 45, or 90
    colors: will alternate
    """
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
    spec['data'][0]['transform'][0]['expr'] = angle2expr.get(angle, '0')
    # other parameters
    spec['width'] = width
    spec['height'] = height
    spec['marks'][0]['transform'][0]['size'] = [width, height]
    spec['scales'][0]['range'] = colors
    return Vega(spec)
