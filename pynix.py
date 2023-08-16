
from default_factories import DefaultPynixFactory
from session import Session

class pynix(Session):
  def __init__(self):
    self.fac = DefaultPynixFactory()
    self.fs = self.fac.make_filesystem()
    self.dbm = self.fac.make_dbm()
    fs = self.dbm.load()
    if fs is not None:
      self.fs = fs
    self.cmdLookup = self.fac.make_filesystem_commands()
    self.csl = self.fac.make_console()
    self.usr = 'guest'
    self.pwd = '/'

  def getFactory(self):
    return self.fac

  def getFilesystem(self):
    return self.fs

  def getCommands(self):
    return self.cmdLookup

  def getConsole(self):
    return self.csl

  def getUser(self):
    return self.usr

  def setUser(self, usr):
    self.usr = usr

  def getPwd(self):
    return self.pwd

  def setPwd(self, path:str):
    self.pwd = path

  def execute(self, cmd):
    args = cmd.split()
    if args[0] in self.cmdLookup:
      target = self.cmdLookup[args[0]]
      target.execute(self, args)
    else:
      print("Operation not found")

  def prompt(self):
    self.csl.prompt(self.usr, self.cmdLookup.keys())
    
  def onQuit(self):
    self.dbm.save(self.fs)

if __name__ == "__main__":
  pnx = pynix()
  while True:
    pnx.prompt()
    cmd = input()
    if cmd == 'quit':
      pnx.onQuit()
      break
    #print('executing',cmd)
    pnx.execute(cmd)
