

import json
import filesystem
from dbm import AbstractDbm

class DefaultDbm(AbstractDbm):
  def load(self):
    try:
      with open('fs.txt','r') as content:
        return json.dump(content, cls=filesystem.FileSystem)
    except:
      print('**** db error')
    return

  def save(self, fs):
    with open('fs.txt','w') as content:
      return json.dump(fs, content)
    return None
