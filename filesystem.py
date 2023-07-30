

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
  childDirectories = dict()
  childFiles = dict()
  otherUserPermission = None

class File:
  name  = None # string
  owner = None # UserGroup
  otherUserPermission = None # FilePermission
  content = []

class User:
  name     = None # string
  password = None # string
  group    = None # UserGroup

class FileSystem:
  root    = None  # Directory
  groups  = dict() # UserGroup
  users   = dict() # User





 
