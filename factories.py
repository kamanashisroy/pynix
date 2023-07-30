
class AbstractPynixFactory:
  def make_filesystem(self):
    pass

  def make_directory(self, name, owner):
    pass

  def make_file(self, name, owner):
    pass

  def make_user_group(self, name):
    pass

  def make_user(self, name,password,grp):
    pass

  def make_filesystem_oper(self):
    pass

  def make_console(self):
    pass
