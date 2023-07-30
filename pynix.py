
from default_factories import DefaultPynixFactory

class pynix:
  def __init__(self):
    self.fac = DefaultPynixFactory()
    self.fs = self.fac.make_filesystem()
    self.fsOper = self.fac.make_filesystem_oper()
    self.csl = self.fac.make_console()
    self.sess = dict()
    self.sess['usr'] = 'guest'

  def execute(self, cmd):
    args = cmd.split()
    if args[0] in self.fsOper:
      target = self.fsOper[args[0]]
      target.execute(self.fac, self.fs, self.fsOper, self.csl, self.sess, args)
    else:
      print("Operation not found")

  def prompt(self):
    self.csl.prompt(self.fsOper.keys())
    
if __name__ == "__main__":
  pnx = pynix()
  while True:
    pnx.prompt()
    cmd = input()
    if cmd == 'quit':
      break
    #print('executing',cmd)
    pnx.execute(cmd)
