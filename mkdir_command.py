
from commands import Command
from collections import deque

class MkdirCommand(Command):
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
          csl.echo('Making directory under', cur.name)
          cur.childDirectories[name] = sess.getFactory().make_directory(name,sess.usr)
          cur = cur.childDirectories[name]
          break
        else:
          csl.error('Not allowed', pathStr)
          return

    csl.echo('Showing path', pathStr)
    csl.echo('Name', cur.name)
    csl.echo('Owner', cur.owner)
    csl.echo('Permission Of Others', cur.otherUserPermission)
    assert(isDir)
    csl.echo('Sub directories', cur.childDirectories.keys())
    csl.echo('Files', cur.childFiles.keys())
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tmkdir path")
    csl.echo("helps to create directory")
