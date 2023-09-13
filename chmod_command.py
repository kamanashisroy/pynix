
from commands import Command
from collections import deque
from pathtools import PathUtil
from permtools import PermUtil

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
    path = PathUtil(sess.getPwd(), pathStr)
    pathq = path.pathq.copy()
    abspath = path.absolute_path()
    usr = sess.getUser()
    usr_grp = sess.getFilesystem().users[usr].group
    permGuard = PermUtil(usr, usr_grp)

    permStr = args[1] if len(args) > 0 else ''
    perm = int(permStr,2)
    if len(permStr) == 0 or perm not in (0b0,0b1,0b11,0b111):
      csl.error('Invalid permission')
      self.help(sess)
      return

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
        if not permGuard.has_chmod_access(cur):
          csl.error('Permission denied', pathStr)
          return
      elif name in cur.childFiles:
        cur = cur.childFiles[name]
        if not permGuard.has_chmod_access(cur):
          csl.error('Permission denied', pathStr)
          return
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
