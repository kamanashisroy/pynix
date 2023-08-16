

class UserPermission:
  CREATE_USER = 1
  READ_USER = 2
  EDIT_USER = 3
  DELETE_USER = 4

class DirectoryPermission:
  CREATE_FILE = 1
  CREATE_DIRECTORY = 2
  READ_DIRECTORY = 3
  EDIT_DIRECTORY = 4
  DELETE_DIRECTORY = 5

class FilePermission:
  READ_FILE = 1
  WRITE_FILE = 2
  DELETE_FILE = 3
  EXECUTE_FILE = 4

class UserGroup:
  name = None # string

class Directory:
  name  = None # string
  owner = None # UserGroup
  childDirectories = None
  childFiles = None
  otherUserPermission = None
  def __init__(self):
    self.childFiles = dict()
    self.childDirectories = dict()

class File:
  name  = None # string
  owner = None # UserGroup
  otherUserPermission = None # FilePermission
  content = None
  def __init__(self):
    self.content = []

class User:
  name     = None # string
  password = None # string
  group    = None # UserGroup

class FileSystem:
  root    = None  # Directory
  groups  = None # UserGroup
  users   = None # User
  def __init__(self):
    self.groups = dict()
    self.users = dict()




 
