
from session import Session
from commands import Command
from collections import deque

class PwdCommand(Command):
  '''
  \brief Allow Read/Write files
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    csl.echo('Current directory', sess.getPwd())
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tpwd")
    csl.echo("Gives current directory.")
