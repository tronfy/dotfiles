from genericpath import exists
from re import sub
from os import environ, pardir, symlink
from os.path import dirname, realpath, islink

def generic(custom):
  return sub(r'^' + environ['HOME'], '~', custom)

def custom(generic):
  return sub(r'^~', environ['HOME'], generic)

def link(src, dst):
  if exists(dst):
    if not islink(dst):
      a = input("file " + dst + "exists, replace with symlink? [y/N] ")
      if a == 'y':
        symlink(src, dst)
    else:
      print('already linked:', dst, '->', src)
  else:
    symlink(src, dst)

HERE = dirname(realpath(__file__))
DOT_DIR = custom(dirname(HERE))
DB_PATH = custom(HERE) + '/db.json'
