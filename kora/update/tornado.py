import os
import pkg_resources
from time import sleep


version = pkg_resources.get_distribution("tornado").version
# Run once only. If call again, will not restart
if version == '4.5.3':
    os.system("pip install -U tornado")  # to 6.0.4

    print("Runtime is now restarting...")
    print("You can ignore the error message [Your session crashed for an unknown reason.]")
    sleep(0.5)
    os._exit(0)  # restart