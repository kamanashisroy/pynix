
from console import Console

class DefaultConsole(Console):
  def echo(self, *args):
    print(args);

  def debug(self, *args):
    #print(args);
    pass

  def prompt(self, *args):
    print('pynix >', *args)

  def error(self, *args):
    print('***',*args)

  def showTable(self, table):
    NCOL = len(table[0])
    NROW = len(table)

    for row in table:
      output = []
      for col in row:
        output.append(col)
        output.append('\t\t\t|')

      print(''.join(output))

        
