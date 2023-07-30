
from commands import Command
from collections import deque

class CatCommand(Command):
  '''
  \brief Allow Read/Write files
  
  '''
  def __init__(self):
    pass

  def execute(self, fac, fs, fsOper, csl, sess, args):
    args.pop(0) # skip command name
    csl.debug('checking path ', args)
    if not args:
      csl.error('Error path is empty')
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
      csl.error('Error path should begin with root')
      self.help()
      return

    pathq.popleft()
    cur = fs.root
    isDir = True
    while pathq:
      if cur is None:
        csl.error('Invalid path')
        return

      name = pathq.popleft()
      if name is None:
        csl.error('Invalid path')
        return

      if not isDir:  
        csl.error('Path is too long, at position', name)
        return

      if name in cur.childDirectories:
        cur = cur.childDirectories[name]
      elif name in cur.childFiles:
        cur = cur.childFiles[name]
        isDir = False
      else: # the content is not there
        if not pathq: # has no more content
          cur.childFiles[name] = fac.make_file(name,cur.owner)
          cur = cur.childFiles[name]
          isDir = False

    csl.echo('Showing path', pathStr)
    csl.echo('Name', cur.name)
    csl.echo('Owner', cur.owner)
    csl.echo('Permission Of Others', cur.otherUserPermission)
    if isDir:
      csl.echo('Sub directories', cur.childDirectories.keys())
      csl.echo('Files', cur.childFiles.keys())
    else: # show content
      if len(contentStr) > 0:
        cur.content.append(contentStr)
      csl.echo('Content', cur.content)
    csl.echo('============================ Success')

  def help(self):
    print("SYNOPSIS")
    print("\t\tcat path_to_file [Added Content]")
    print("cat lists file or directory content.")
