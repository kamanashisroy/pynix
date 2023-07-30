
from commands import Command
from collections import deque

class LoginCommand(Command):
  '''
  \brief Login as an user
  
  '''
  def __init__(self):
    pass

  def execute(self, fac, fs, fsOper, csl, sess, args):
    args.pop(0) # skip command name
    if not args or len(args) < 2:
      csl.error('Error no user or pass')
      self.help()
      return

    name = args[0]
    pwd = args[1]

    if name not in fs.users:
      csl.error('User not found')
      self.help()
      return

    usr = fs.users[name]
    if usr.password != pwd:
      csl.error('Invalid pass')
      self.help()
      return

    sess['usr'] = usr
    csl.echo('============================ Success')

  def help(self):
    print("SYNOPSIS")
    print("\t\tlogin user pass")
