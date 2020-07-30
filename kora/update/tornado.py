import os
from time import sleep

from kora import get_ver

# Run once only. If call again, will not restart
if get_ver('tornado') == '5.1.1':
    os.system("pip install -U tornado")  # to 6.0.4

    print("Runtime is now restarting...")
    print("You can ignore the error message [Your session crashed for an unknown reason.]")
    sleep(0.5)
    os._exit(0)  # restart
