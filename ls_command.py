
from session import Session
from commands import Command
from collections import deque

class LsCommand(Command):
  '''
  \brief Show directory content
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    csl.debug('checking path ', args)

    pathStr = ''
    if args:
      pathStr = args[0]

    if not pathStr or pathStr[0] != '/':
      pathStr = sess.getPwd() + pathStr

    path = pathStr.split('/')
    pathq = deque()
    for item in path:
      if 0 != len(item):
        pathq.append(item)

    cur = sess.getFilesystem().root
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
          isDir = False

    csl.echo('Showing path', pathStr)
    csl.echo('Name', cur.name)
    csl.echo('Owner', cur.owner)
    csl.echo('Permission Of Others', cur.otherUserPermission)
    if isDir:
      csl.echo('Sub directories', cur.childDirectories.keys())
      csl.echo('Files', cur.childFiles.keys())
    else: # show content
      csl.echo('Content', cur.content)
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tls path_to_directory")
    csl.echo("ls lists file or directory content.")
