"""
Set default to pyngrok.ngrok
- set auth token automatically, if available
- set connect() to return tunnel, and use https.
"""
import os
from fastcore.utils import partialler

# install pyngrok
os.system('pip install pyngrok')
from pyngrok.ngrok import *


# auto-cofig token
token_file = '/content/drive/My Drive/ngrok.token'
if os.path.exists(token_file):
    with open(token_file) as f:
        token = f.read()
    set_auth_token(token)


# set default arguments for connect
# this behaves like upcoming pyngrok 5.0 and avoid warnings
connect = partialler(connect, return_ngrok_tunnel=True, bind_tls=True)
