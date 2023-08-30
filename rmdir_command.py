
from commands import Command
from collections import deque

class RmdirCommand(Command):
  '''
  \brief Allow Make directory
  
  '''
  def __init__(self):
    pass

  def execute(self, sess, args):
    args.pop(0) # skip command name
    csl = sess.getConsole()
    csl.debug('checking path ', args)
    if not args:
      csl.error('Error path is empty')
      self.help(sess)
      return

    pathStr = args[0]

    if not pathStr or pathStr[0] != '/':
      pathStr = sess.getPwd() + pathStr

    path = pathStr.split('/')
    pathq = deque()
    for item in path:
      if 0 != len(item):
        pathq.append(item)

    parent = None
    cur = sess.getFilesystem().root
    while pathq:
      if cur is None:
        csl.error('Invalid path')
        return

      name = pathq.popleft()
      if name is None:
        csl.error('Invalid path')
        return

      if name in cur.childDirectories:
        parent = cur
        cur = cur.childDirectories[name]
      elif name in cur.childFiles:
        csl.error('Path contains a file', pathStr)
        return
      else: # the content is not there
        csl.error('Directory not found', pathStr)
        return

    if parent is None:
      csl.echo('Cannot delete root directory')
      return

    csl.echo('Showing path', pathStr)
    csl.echo('Name', cur.name)
    csl.echo('Owner', cur.owner)
    csl.echo('Permission Of Others', cur.otherUserPermission)
    csl.echo('Sub directories', cur.childDirectories.keys())
    csl.echo('Files', cur.childFiles.keys())
    csl.echo('Deleting', cur.name)
    del parent.childDirectories[cur.name]
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\trmdir path")
    csl.echo("helps to remove directory")
