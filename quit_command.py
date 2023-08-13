
from commands import Command
from collections import deque

class QuitCommand(Command):
  '''
  \brief Show command help
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    pass

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tquit")
    csl.echo("End script")
