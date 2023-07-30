
from commands import Command
from collections import deque

class QuitCommand(Command):
  '''
  \brief Show command help
  
  '''
  def __init__(self):
    pass

  def execute(self, fac, fs, fsOper, csl, args):
    pass

  def help(self):
    print("SYNOPSIS")
    print("\t\tquit")
    print("End script")
