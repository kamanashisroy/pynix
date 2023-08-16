
from commands import Command
from collections import deque

class LoginCommand(Command):
  '''
  \brief Login as an user
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    if not args or len(args) < 2:
      csl.error('Error no user or pass')
      self.help(sess)
      return

    name = args[0]
    pwd = args[1]

    fs  = sess.getFilesystem()
    if name not in fs.users:
      csl.error('User not found')
      self.help(sess)
      return

    usr = fs.users[name]
    if usr.password != pwd:
      csl.error('Invalid pass')
      self.help(sess)
      return

    sess.setUser(usr.name)
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tlogin user pass")
