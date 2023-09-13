
from session import Session
from commands import Command
from collections import deque
from pathtools import PathUtil

class CdCommand(Command):
  '''
  \brief Change directory
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    csl.echo('Current directory', sess.getPwd())

    pathStr = ''
    if args:
      pathStr = args[0]

    path = PathUtil(sess.getPwd(), pathStr)
    pathq = path.pathq.copy()
    abspath = path.absolute_path()

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
        csl.error('path is not a valid directory', pathStr)
        return
      else: # the content is not there
        csl.error('Path is too long, at position', name)
        return

    csl.echo('Changing current path to', abspath)
    csl.echo('Name', cur.name)
    csl.echo('Owner', cur.owner)
    csl.echo('Permission Of Others', cur.otherUserPermission)
    sess.setPwd(abspath)

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tcd [target directory]")
    csl.echo("Change directory.")
