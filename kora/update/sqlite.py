import os
from time import sleep

os.system("add-apt-repository -y ppa:dqlite/stable")
os.system("apt update")
os.system("apt install sqlite3")

print("Runtime is now restarting...")
print("You can ignore the error message [Your session crashed for an unknown reason.]")
sleep(0.5)
os._exit(0)  # restart
