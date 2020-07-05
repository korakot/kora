""" install neo4j, py2neo

Can be used as py2neo replacement. 
Use %%nj for easy query with Cypher
"""

import os
from IPython.core.magic import register_cell_magic


# download neo4j 4.1
print("Installing neo4j 4.1")
os.system("wget https://neo4j.com/artifact.php?name=neo4j-community-4.1.0-unix.tar.gz -O nj.tgz")
# decompress and rename
os.system("tar -xf nj.tgz")
os.system("mv neo4j-community-4.1.0 nj")
# download APOC plugin
os.system("wget -P nj/plugins https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.1.0.0/apoc-4.1.0.0-all.jar")
# config to disable password, use APOC
os.system("sed -i '/dbms.security.auth_enabled/s/^#//g' nj/conf/neo4j.conf")
os.system("sed -i '/dbms.security.procedures.unrestricted/s/^#//g' nj/conf/neo4j.conf")
os.system("sed -i 's/my.extensions.example,my.procedures/apoc/' nj/conf/neo4j.conf")
# start server
os.system("nj/bin/neo4j start")


# py2neo
print("Installing py2neo")
os.system("pip install py2neo")  # errors can be ignore
from py2neo import *   # e.g. Node, Relationship, Graph
graph = Graph("bolt://localhost:7687")  # connect to server


# Use %%nj similar to %%cypher
@register_cell_magic
def nj(line, cell=None):
    return graph.run(cell or line).to_data_frame()
