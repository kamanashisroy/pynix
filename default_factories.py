
from filesystem import FileSystem,User,UserGroup,Directory,File
from factories import AbstractPynixFactory
from default_console import DefaultConsole
from cat_command import CatCommand
from mkdir_command import MkdirCommand
from help_command import HelpCommand
from quit_command import QuitCommand
from chmod_command import ChmodCommand
from login_command import LoginCommand
from ls_command import LsCommand
from pwd_command import PwdCommand
from rm_command import RmCommand
from rmdir_command import RmdirCommand
from default_dbm import DefaultDbm

import commands

class DefaultPynixFactory(AbstractPynixFactory):
  def __init__(self):
    pass

  def make_filesystem(self):
    fs = FileSystem()

    # make admin group
    fs.groups['admin'] = self.make_user_group('admin')
    fs.groups['guest'] = self.make_user_group('guest')

    # make root directory
    fs.root = self.make_directory("root", 'admin')

    # make admin user
    fs.users['admin'] = self.make_user("admin","admin",'admin')
    fs.users['guest'] = self.make_user("guest","guest",'guest')
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

  def make_filesystem_commands(self):
    opr = dict()
    opr['cat'] = CatCommand()
    opr['mkdir'] = MkdirCommand()
    opr['help'] = HelpCommand()
    opr['quit'] = QuitCommand()
    opr['chmod'] = ChmodCommand()
    opr['login'] = LoginCommand()
    opr['ls'] = LsCommand()
    opr['pwd'] = PwdCommand()
    opr['rmdir'] = RmdirCommand()
    opr['rm'] = RmCommand()
    return opr

  def make_console(self):
    return DefaultConsole()

  def make_dbm(self):
    return DefaultDbm()
