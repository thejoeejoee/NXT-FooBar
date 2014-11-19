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
    for _ in range(20):
        source = source.\
            replace('\n', ' ').\
            replace('\t', ' ').\
            replace('  ', ' ').\
            replace('   ', ' ').\
            replace('{ ', '{').\
            replace(' {', '{').\
            replace(', ', ',').\
            replace(' = ', '=').\
            replace(' =', '=').\
            replace(' } ', '}').replace('== ', '==')
    return source


sys.argv.remove(os.path.basename(__file__))
source_param = sys.argv[0]
if source_param[-4:] == '.lua':  # file
    f = open(source_param, 'r')
    with f:
        source = ''.join(f)
    before = len(source)
    source = mimify(source)
    after = len(source)
    f_new = ''.join(('mim_', source_param))
    new_file = open(f_new, 'w')
    with new_file:
        new_file.write(source)
    print('{} chars mimified to {} chars, diff: {} chars.'.format(before, after, after-before))



