import os

# install PostgreSQL 10
os.system("apt install postgresql postgresql-contrib")
os.system("service postgresql start")
os.system("sudo -u postgres psql -c 'CREATE USER root WITH SUPERUSER'")

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
