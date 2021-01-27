"""
Install a new version of Google Cloud Speech Python Client
(Speech-to-Text)
"""

import os
import sys
from time import sleep

if 'google.cloud.speech' not in sys.modules:
    url = 'https://storage.googleapis.com/api-client-staging/speech-v1p1beta1-py_20200928.tar.gz'
    os.system(f'curl {url} | tar xz')
    os.chdir('speech-v1p1beta1-py')
    os.system('pip install .')
    
    print("Runtime is now restarting...")
    print("You can ignore the error message [Your session crashed for an unknown reason.]")
    sleep(0.5)
    os._exit(0)  # restart
