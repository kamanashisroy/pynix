
from filesystem import FileSystem,User,UserGroup,Directory,File
import commands

class FsFactory:
  @staticmethod
  def make_filesystem():
    fs = FileSystem()

    # make admin group
    fs.groups['admin'] = FsFactory.make_user_group('admin')

    # make root directory
    fs.root = FsFactory.make_directory("root", fs.groups['admin'])

    # make admin user
    fs.admin = FsFactory.make_user("admin","admin",fs.groups['admin'])
    return fs

  @staticmethod
  def make_directory(name, owner):
    dir = Directory()
    dir.name = name
    dir.owner = owner
    return dir

  @staticmethod
  def make_user_group(name):
    grp = UserGroup()
    grp.name = name
    return grp

  @staticmethod
  def make_user(name,password,grp):
    usr = User()
    usr.name = name
    usr.password = password
    usr.group = grp
    return usr

  @staticmethod
  def make_filesystem_oper():
    opr = dict()
    opr['cd'] = commands.CdCommand()
    return opr
