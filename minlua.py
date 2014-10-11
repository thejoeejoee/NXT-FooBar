"""
pyscript mimifying lua scripts for NXT
USAGE:

$ python minlua.py file.lua
OR
$ python minlua.py folder/

from file.lua it creates file_min.lua OR create new directory named folder_min/
"""
import sys
import os

def mimify(source):
    return source.replace('\n',' ').replace('\t', ' ').replace('  ', ' ').replace('   ', ' ')


sys.argv.remove(os.path.basename(__file__))
source_param = sys.argv[0]
if source_param[-4:] == '.lua':  # file
    f=open(source_param)
    with f:
        source = ''.join(f)
        print mimify(source)



