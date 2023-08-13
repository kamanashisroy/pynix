
from commands import Command
from collections import deque

class ChmodCommand(Command):
  '''
  \brief Modify permission
  
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
    permStr = args[1] if len(args) > 1 else ''
    perm = int(permStr,2)
    if len(permStr) == 0 or perm not in (0b0,0b1,0b11,0b111):
      csl.error('Invalid permission')
      self.help(sess)
      return
    path = pathStr.split('/')
    pathq = deque()
    for item in path:
      if 0 != len(item):
        pathq.append(item)
    if not pathq or pathq[0] != 'root':
      csl.error('Error path should begin with root')
      self.help(sess)
      return

    pathq.popleft()
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
        csl.error('Invalid path')
        return

    csl.echo('Changing permission', pathStr)
    cur.otherUserPermission = perm
    csl.echo('Permission Of Others', cur.otherUserPermission)
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tchmod path_to_file perm_flag")
    csl.echo("Perm flag 0b1 = READ.")
    csl.echo("Perm flag 0b11 = READ and WRITE.")
    csl.echo("Perm flag 0b111 = READ and WRITE and EXECUTE.")
