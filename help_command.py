
from commands import Command
from collections import deque

class HelpCommand(Command):
  '''
  \brief Show command help
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    if not args:
      self.help(sess)
    else:
      target = args[0]
      cmdLookup = sess.getCommands()
      if target in fsOper:
        fsOper[target].help(sess)
      else:
        csl.error('Command not found')
    
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\thelp command_name")
    csl.echo("Display usage of a command.")
