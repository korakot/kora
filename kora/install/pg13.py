import os

# update apt
os.system("curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -")
with open('/etc/apt/sources.list.d/pgdg.list', 'w') as f:
  f.write("deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main")
os.system("apt update")

# install PostgreSQL 13 and setup for root
os.system("apt install postgresql-13 postgresql-client-13")
os.system("service postgresql start")
os.system("sudo -u postgres psql -c 'CREATE USER root WITH SUPERUSER'")
os.system("psql postgres -c 'CREATE DATABASE root'")

# update %%sql and add pg special commands
os.system('pip install -U ipython-sql')
os.system('pip install pgspecial')
os.system('pip install psycopg2-binary')  # avoid warning

# config for %%sql
magic = get_ipython().run_line_magic
magic('load_ext', 'sql')
magic('config', 'SqlMagic.displaycon=False')
magic('config', 'SqlMagic.feedback=False')
magic('config', 'SqlMagic.autopandas=True')
magic('sql', 'postgresql+psycopg2://@/postgres')
