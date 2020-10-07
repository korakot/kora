import os
from IPython import get_ipython
magic = get_ipython().run_line_magic


os.system("curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -")
os.system('add-apt-repository "$(curl https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"')
os.system("curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/msprod.list")
os.system("apt update")

os.system("apt install mssql-server")  # install, config, and start
os.environ['MSSQL_PID'] = 'Developer'
os.environ['ACCEPT_EULA'] = 'Y'
os.environ['MSSQL_SA_PASSWORD'] = 'Password.'  # UC, LC, sym or num
os.system("/opt/mssql/bin/mssql-conf -n setup")
os.system("sudo -u mssql /opt/mssql/bin/sqlservr &") # in background

# client
os.system("apt install mssql-tools unixodbc-dev")  # for sqlcmd
os.environ['PATH'] += ':/opt/mssql-tools/bin'
os.system("pip install ipython-sql -U")  # 4.0
os.system("pip install pymssql")   # cannot use pyodbc
magic('load_ext', 'sql')
magic('config', 'SqlMagic.displaycon=False')
magic('config', 'SqlMagic.autopandas=True')
# magic('config', 'SqlMagic.feedback=False')  # Done, rows affected

# default connection
magic('sql', 'mssql+pymssql://sa:Password.@localhost:1433/master')
