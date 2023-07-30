
from commands import Command
from collections import deque

class MkdirCommand(Command):
  '''
  \brief Allow Make directory
  
  '''
  def __init__(self):
    pass

  def execute(self, fac, fs, fsOper, csl, args):
    args.pop(0) # skip command name
    print('checking path ', args)
    if not args:
      print('Error path is empty')
      self.help()
      return

    pathStr = args[0]
    contentStr = args[1] if len(args) > 1 else ''
    path = pathStr.split('/')
    pathq = deque()
    for item in path:
      if 0 != len(item):
        pathq.append(item)
    if not pathq or pathq[0] != 'root':
      print('Error path should begin with root')
      self.help()
      return

    pathq.popleft()
    cur = fs.root
    isDir = True
    while pathq:
      if cur is None:
        print('Invalid path')
        return

      name = pathq.popleft()
      if name is None:
        print('Invalid path')
        return

      if not isDir:  
        print('Path is too long, at position', name)
        return

      if name in cur.childDirectories:
        cur = cur.childDirectories[name]
      elif name in cur.childFiles:
        cur = cur.childFiles[name]
        isDir = False
      else: # the content is not there
        if not pathq: # has no more content
          cur.childDirectories[name] = fac.make_directory(name,cur.owner)
          cur = cur.childDirectories[name]
          break
        else:
          print('Not allowed', pathStr)
          return

    print('Showing path', pathStr)
    print('Name', cur.name)
    print('Owner', cur.owner)
    print('Permission Of Others', cur.otherUserPermission)
    if isDir:
      print('Sub directories', cur.childDirectories.keys())
      print('Files', cur.childFiles.keys())
    else: # show content
      if len(contentStr) > 0:
        cur.content.append(contentStr)
      print('Content', cur.content)

    print('============================ Success')

  def help(self):
    print("SYNOPSIS")
    print("\t\tmkdir path")
    print("helps to create directory")
