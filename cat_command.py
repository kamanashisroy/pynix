
from session import Session
from commands import Command
from collections import deque
from pathtools import PathUtil
from permtools import PermUtil

class CatCommand(Command):
  '''
  \brief Allow Read/Write files
  
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
      args.pop(0) # skip path string

    path = PathUtil(sess.getPwd(), pathStr)
    pathq = path.pathq.copy()
    abspath = path.absolute_path()
    usr = sess.getUser()
    usr_grp = sess.getFilesystem().users[usr].group
    perm = PermUtil(usr, usr_grp)
    contentStr = ' '.join(args) if len(args) > 0 else ''

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
        if not perm.has_write_access(cur):
          csl.error('Permission denied', pathStr)
          return
      elif name in cur.childFiles:
        cur = cur.childFiles[name]
        if not perm.has_write_access(cur):
          csl.error('Permission denied', pathStr)
          return
        isDir = False
      else: # the content is not there
        if not pathq: # has no more content
          csl.echo('Making file under', cur.name)
          cur.childFiles[name] = sess.getFactory().make_file(name,sess.usr)
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
        csl.echo('Appending', contentStr)
        cur.content.append(contentStr)
      csl.echo('Content', cur.content)
    csl.echo('============================ Success')

  def help(self, sess):
    csl = sess.getConsole()
    csl.echo("SYNOPSIS")
    csl.echo("\t\tcat path_to_file [Added Content]")
    csl.echo("cat lists file or directory content.")
