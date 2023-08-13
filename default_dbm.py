

import json
from filesystem import FileSystem,User,UserGroup,Directory,File
from dbm import AbstractDbm


class DefaultDbm(AbstractDbm):
  def load(self):

    def asFile(dctObj):
      fl = File()
      if 'name' in dctObj:
        fl.name = dctObj['name']

      if 'owner' in dctObj:
        fl.owner = dctObj['owner']

      if 'otherUserPermission' in dctObj:
        fl.otherUserPermission = dctObj['otherUserPermission']

      if 'content' in dctObj:
        fl.content = dctObj['content']

      return fl

    def asDirectory(dctObj):
      dr = Directory()

      if 'name' in dctObj:
        dr.name = dctObj['name']

      if 'owner' in dctObj:
        dr.owner = dctObj['owner']

      if 'childDirectories' in dctObj and len(dctObj['childDirectories']) > 0:
        dr.childDirectories = dctObj['childDirectories']

      if 'childFiles' in dctObj:
        dr.childFiles = dctObj['childFiles']

      if 'otherUserPermission' in dctObj:
        dr.otherUserPermission = dctObj['otherUserPermission']

      return dr


    def asUserGroup(dctObj):
      grp = UserGroup()

      if 'name' in dctObj:
        grp.name = dctObj['name']
      return grp


    def asUser(dctObj):
      usr = User()

      if 'name' in dctObj:
        usr.name = dctObj['name']

      if 'group' in dctObj:
        usr.group = dctObj['group']

      if 'password' in dctObj:
        usr.password = dctObj['password']

      return usr

    def asFileSystem(dctObj):
      fs = FileSystem()
      if 'users' in dctObj:
        fs.users = dctObj['users']

      if 'groups' in dctObj:
        fs.groups = dctObj['groups']

      if 'root' in dctObj:
        fs.root = dctObj['root']

      return fs

    def readFileSystem(dctObj):
      fsObj = {'FileSystem' : asFileSystem, 'User' : asUser, 'UserGroup' : asUserGroup, 'Directory': asDirectory, 'File' : asFile}
      if 'cls' in dctObj and dctObj['cls'] in fsObj:
        return fsObj[dctObj['cls']](dctObj)
      return dctObj

    try:
      with open('fs.txt','r') as infile:
        return json.load(infile, object_hook=readFileSystem)
    except:
      print('Dbm error')
    return None

  def save(self, fs):

    def dumpFileSystem(obj):
      out = dict()
      if isinstance(obj, FileSystem):
        out['cls'] = "FileSystem"
        out['users'] = obj.users
        out['groups'] = obj.groups
        out['root'] = obj.root
      elif isinstance(obj, User):
        out['cls'] = "User"
        out['name'] = obj.name
        out['group'] = obj.group
        out['password'] = obj.password
      elif isinstance(obj, UserGroup):
        out['cls'] = "UserGroup"
        out['name'] = obj.name
      elif isinstance(obj, Directory):
        out['cls'] = "Directory"
        out['name'] = obj.name
        out['owner'] = obj.owner
        out['childDirectories'] = obj.childDirectories
        out['childFiles'] = obj.childFiles
        out['otherUserPermission'] = obj.otherUserPermission
      elif isinstance(obj, File):
        out['cls'] = "File"
        out['name'] = obj.name
        out['owner'] = obj.owner
        out['otherUserPermission'] = obj.otherUserPermission
        out['content'] = obj.content
      print(out, out.__class__)
      return out 
    with open('fs.txt','w') as outfile:
        json.dump(fs, outfile, default=dumpFileSystem)
    return None
