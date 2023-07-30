
from commands import Command
from collections import deque

class HelpCommand(Command):
  '''
  \brief Show command help
  
  '''
  def __init__(self):
    pass

  def execute(self, fac, fs, fsOper, csl, sess, args):
    args.pop(0) # skip command name
    if not args:
      self.help()
    else:
      target = args[0]
      if target in fsOper:
        fsOper[target].help()
      else:
        csl.error('Command not found')
    
    print('============================ Success')

  def help(self):
    print("SYNOPSIS")
    print("\t\thelp command_name")
    print("Display usage of a command.")
