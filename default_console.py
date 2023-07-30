
from console import Console

class DefaultConsole(Console):
  def echo(self, args):
    print(args);

  def prompt(self, args):
    print('pynix >', args)

  def error(self, args):
    print('***',*args)
