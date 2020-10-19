"""
InfluxDB is a time-series database
"""
import os

# install server
os.system("curl -sL https://repos.influxdata.com/influxdb.key | apt-key add -")
with open('/etc/apt/sources.list.d/influxdb.list', 'w') as f:
    f.write("deb https://repos.influxdata.com/ubuntu bionic stable")
os.system('apt update')
os.system('apt install influxdb')
os.system('influxd -config /etc/influxdb/influxdb.conf &')

# install client
os.system("pip install influxdb")
