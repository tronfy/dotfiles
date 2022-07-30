from json import load
from os.path import exists

from _common import custom, link, DOT_DIR, DB_PATH

db = {}
if exists(DB_PATH):
  with open(DB_PATH, 'r') as db_file:
    db = load(db_file)
else:
  print('error: database ' + DB_PATH + ' not found')
  exit(1)

for entry in db:
  a = input("link " + db[entry] + "? [Y/n] ")

  if a != 'n':
    link(DOT_DIR.rstrip('/') + '/' + db[entry], custom(entry))
