import os
import re
import requests 
from subprocess import Popen, PIPE, STDOUT
from IPython.core.magic import register_cell_magic
from urllib.parse import urljoin


# download server
ver = '7.9.2'
url = f'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{ver}-linux-x86_64.tar.gz'
os.system(f"curl {url} | tar xz")
os.system(f"chown -R daemon:daemon elasticsearch-{ver}")

# start server
es_server = Popen([f'elasticsearch-{ver}/bin/elasticsearch'], 
                  stdout=PIPE, stderr=STDOUT,
                  preexec_fn=lambda: os.setuid(1)  # as daemon
                 )
for i in range(77):
    es_server.stdout.readline()  # wait till started


# client
os.system("pip install elasticsearch")

# client magic
@register_cell_magic
def es(line=None, cell=""):
    cell = re.sub(r'(?m)^\s*#.*\n?','', cell) # remove comment
    line1 = (cell + '\n').find('\n')
    method, path = cell[:line1].split(None, 1)
    body = cell[line1:].strip()
    args = {}
    if body:
        args['data'] = (body + '\n').encode()  # add \n in case _bulk
        args['headers'] = {'Content-Type': 'application/json'}

    url = urljoin('http://localhost:9200', path)
    req = requests.Request(method, url, **args).prepare()
    rsp = requests.Session().send(req)
    return rsp

# client viz
def render(r):
    text = r.text  
    if text[0] in "[{":  # really json
        return """
        <script src="https://rawgit.com/caldwell/renderjson/master/renderjson.js"></script>
        <script>
        renderjson.set_show_to_level(1)
        document.body.appendChild(renderjson(%s))
        new ResizeObserver(google.colab.output.resizeIframeToContent).observe(document.body) 
        </script>
        """ % text
    else:    # other status text
        return "<pre>%s</pre>" % text
requests.models.Response._repr_html_ = render
