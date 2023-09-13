

from collections import deque

class PathUtil:
  def __init__(self, pwd, relPath):
    self.pwd = pwd
    pathStr = relPath

    if not pathStr or pathStr[0] != '/':
      # get relative path
      pathStr = self.pwd + '/' + pathStr

    path = pathStr.split('/')
    self.pathq = deque()
    for item in path:
      if '..' == item:
        self.pathq.pop() # previous directory
      elif '.' == item:
        pass
      elif 0 != len(item):
        self.pathq.append(item)

  def absolute_path(self):
    return '/' + '/'.join(self.pathq)


  
