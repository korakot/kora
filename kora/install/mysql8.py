import os

os.system('wget -qO mysql.deb  https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb')
os.system('dpkg -i mysql.deb')
os.remove('mysql.deb')
os.system('apt update')
os.system('apt install mysql-server')
get_ipython().system_raw('mysqld_safe &')

os.system('pip install -U ipython-sql pymysql -q')
