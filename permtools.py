


class PermUtil:
  def __init__(self, usr, role):
    self.usr = usr
    self.role = role

  def has_read_access(self, content):
    if 'admin' == self.role:
      return True
    if self.usr == content.owner:
      return True
    flag = content.otherUserPermission 
    flag = 0 if flag is None else flag
    if (flag & 0b11):
      return True
    return False

  def has_write_access(self, content):
    if 'admin' == self.role:
      return True
    if self.usr == content.owner:
      return True
    flag = content.otherUserPermission
    flag = 0 if flag is None else flag
    if flag & 0b10:
      return True
    return False

  def has_chmod_access(self, content):
    if 'admin' == self.role:
      return True
    if self.usr == content.owner:
      return True
    return False


  
