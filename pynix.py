
import factories

class pynix:
  def __init__(self):
    self.fs = factories.FsFactory.make_filesystem()
    self.fsOper = factories.FsFactory.make_filesystem_oper()

  def execute(self, cmd):
    args = cmd.split()
    if args[0] in self.fsOper:
      target = self.fsOper[args[0]]
      target.execute(args)
    else:
      print("Operation not found")

if __name__ == "__main__":
  pnx = pynix()
  while True:
    cmd = input()
    if cmd == 'quit':
      break
    print('executing',cmd)
    pnx.execute(cmd)
