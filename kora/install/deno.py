import os

os.system('curl -fsSL https://deno.land/x/install/install.sh | sh')
os.environ['DENO_INSTALL'] = "/root/.deno"
os.environ['PATH'] += ':/root/.deno/bin'
