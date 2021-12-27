from re import sub
from os import environ, pardir, symlink
from os.path import dirname, realpath

def generic(custom):
  return sub(r'^' + environ['HOME'], '~', custom)

def custom(generic):
  return sub(r'^~', environ['HOME'], generic)

def link(src, dst):
  try:
    symlink(src, dst)
    print('linked', dst, '->', src)
  except FileExistsError:
    print('already linked:', dst, '->', src)

HERE = dirname(realpath(__file__))
DOT_DIR = custom(dirname(HERE))
DB_PATH = custom(HERE) + '/db.json'
