from json import dump, load
from os import makedirs
from os.path import exists
from re import sub
from shutil import move
from sys import argv

from common import generic, link, DOT_DIR, DB_PATH

if (len(argv) != 2 and len(argv) != 3) or argv[1] == '-h' or argv[1] == '--help':
  print('usage: python add.py [src] [--no-link]')
  exit(1)

no_link = False
if len(argv) == 3:
  no_link = (argv[2] == '--no-link')

db = {}
if exists(DB_PATH):
  with open(DB_PATH, 'r') as db_file:
    db = load(db_file)
else:
  print('database ' + DB_PATH + ' not found, will be created')

source_raw = argv[1].rstrip('/')
source = generic(source_raw)
local = sub(r'^.config/', '', sub(r'^~/', '', source))
local_raw = DOT_DIR.rstrip('/') + '/' + local

if not source.startswith('~'):
  print('error: not absolute path')
  exit(1)

if source in db:
  print('error: already tracked:', source, '->', db[source])
  exit(1)

db[source] = local

try:
  makedirs('/'.join(local_raw.split('/')[:-1]))
except FileExistsError:
  pass

move(source_raw, local_raw)

if not no_link:
  link(local_raw, source_raw)
else:
  print('--no-link is set: not linking')
  print(source_raw, '->', local_raw)

with open(DB_PATH, 'w') as db_file:
  dump(dict(sorted(db.items())), db_file, indent=2)
