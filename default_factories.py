
from filesystem import FileSystem,User,UserGroup,Directory,File
from factories import AbstractPynixFactory
from default_console import DefaultConsole
from cat_command import CatCommand
from mkdir_command import MkdirCommand
from help_command import HelpCommand
from quit_command import QuitCommand

import commands

class DefaultPynixFactory(AbstractPynixFactory):
  def __init__(self):
    pass

  def make_filesystem(self):
    fs = FileSystem()

    # make admin group
    fs.groups['admin'] = self.make_user_group('admin')

    # make root directory
    fs.root = self.make_directory("root", 'admin')

    # make admin user
    fs.admin = self.make_user("admin","admin",'admin')
    return fs

  def make_directory(self, name, owner_name):
    dir = Directory()
    dir.name = name
    dir.owner = owner_name
    return dir

  def make_file(self, name, owner_name):
    fl = File()
    fl.name = name
    fl.owner = owner_name
    return fl

  def make_user_group(self, name):
    grp = UserGroup()
    grp.name = name
    return grp

  def make_user(self, name,password,grp):
    usr = User()
    usr.name = name
    usr.password = password
    usr.group = grp
    return usr

  def make_filesystem_oper(self):
    opr = dict()
    opr['cat'] = CatCommand()
    opr['mkdir'] = MkdirCommand()
    opr['help'] = HelpCommand()
    opr['quit'] = QuitCommand()
    return opr

  def make_console(self):
    return DefaultConsole()
