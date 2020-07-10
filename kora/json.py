from json import *
import requests

from IPython.display import HTML

_render_template = """
<script src="https://rawgit.com/caldwell/renderjson/master/renderjson.js"></script>
<script>
renderjson.set_show_to_level(1)
document.body.appendChild(renderjson(%s))
new ResizeObserver(google.colab.output.resizeIframeToContent).observe(document.body)
</script>
"""

requests.models.Response._repr_html_ = lambda rsp: _render_template % rsp.text


def render(jstr):
    if type(jstr) != str:
        jstr = dumps(jstr)
    if jstr.startswith('http'):
        jstr = requests.get(jstr).text
    if jstr.endswith('.json'):
        with open(jstr) as f:
            jstr = f.read()
    return HTML(_render_template % jstr)
