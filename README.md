
In memory filesystem
====================

It has directories, files and users.
It also supports persistence.

Please refer to [slides](slides/) for presentations.

How to use
============

#### Invoking the pynix

```
python3 pynix.py 
```

#### Help command

Check command help by typing `help` and enter.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
help 
('SYNOPSIS',)
('\t\thelp command_name',)
('Display usage of a command.',)
('============================ Success',)
```

#### Mkdir command


```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
help mkdir
('SYNOPSIS',)
('\t\tmkdir path',)
('helps to create directory',)
('============================ Success',)
```

Create a _goody_ directory by command `mkdir goody`.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
mkdir goody
('Making directory under', 'root')
('Showing path', '/goody')
('Name', 'goody')
('Owner', 'guest')
('Permission Of Others', None)
('Sub directories', dict_keys([]))
('Files', dict_keys([]))
('============================ Success',)
```

Check if directory is created by `ls` command.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
help ls
('SYNOPSIS',)
('\t\tls path_to_directory',)
('ls lists file or directory content.',)
('============================ Success',)
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
ls goody
('Showing path', '/goody')
('Name', 'goody')
('Owner', 'guest')
('Permission Of Others', None)
('Sub directories', dict_keys([]))
('Files', dict_keys([]))
```


#### cat command

Create a file named 'camera' containing 'nikkon'.


```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
cat goody/camera nikkon
('Making file under', 'goody')
('Showing path', '/goody/camera')
('Name', 'camera')
('Owner', 'guest')
('Permission Of Others', None)
('Appending', 'nikkon')
('Content', ['nikkon'])
('============================ Success',)
```

Also read a directory or file.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
cat goody/camera
('Showing path', '/goody/camera')
('Name', 'camera')
('Owner', 'guest')
('Permission Of Others', None)
('Content', ['nikkon'])
('============================ Success',)
```

`ls` command also works.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
ls goody/camera
('Showing path', '/goody/camera')
('Name', 'camera')
('Owner', 'guest')
('Permission Of Others', None)
('Content', ['nikkon'])
('============================ Success',)
```

#### Chmod command

Set read,write and execute permission.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
help chmod
('SYNOPSIS',)
('\t\tchmod path_to_file perm_flag',)
('Perm flag 0b1 = READ.',)
('Perm flag 0b11 = READ and WRITE.',)
('Perm flag 0b111 = READ and WRITE and EXECUTE.',)
```

Here is an example,

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
chmod goody/camera 0b111
('Changing permission', '/goody/camera')
('Permission Of Others', 7)
('============================ Success',)
```

#### Login command

For login we have `login` command. Notice that after login the user changes in the prompt.

```
pynix [ guest ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
login admin admin
('============================ Success',)
pynix [ admin ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
```

#### Persistence

Data is written upon `quit` command.

```
pynix [ admin ] > dict_keys(['cat', 'mkdir', 'help', 'quit', 'chmod', 'login', 'ls', 'pwd'])
quit
{'cls': 'FileSystem', 'users': {'admin': <filesystem.User object at 0x7f6de92e0da0>, 'guest': <filesystem.User object at 0x7f6de92e0eb8>}, 'groups': {'admin': <filesystem.UserGroup object at 0x7f6de92e0f28>, 'guest': <filesystem.UserGroup object at 0x7f6de92e0f98>}, 'root': <filesystem.Directory object at 0x7f6de92e5320>} <class 'dict'>
{'cls': 'User', 'name': 'admin', 'group': 'admin', 'password': 'admin'} <class 'dict'>
{'cls': 'User', 'name': 'guest', 'group': 'guest', 'password': 'guest'} <class 'dict'>
{'cls': 'UserGroup', 'name': 'admin'} <class 'dict'>
{'cls': 'UserGroup', 'name': 'guest'} <class 'dict'>
{'cls': 'Directory', 'name': 'root', 'owner': 'admin', 'childDirectories': {'goody': <filesystem.Directory object at 0x7f6de92e51d0>}, 'childFiles': {}, 'otherUserPermission': None} <class 'dict'>
{'cls': 'Directory', 'name': 'goody', 'owner': 'guest', 'childDirectories': {}, 'childFiles': {'camera': <filesystem.File object at 0x7f6de92e52e8>}, 'otherUserPermission': None} <class 'dict'>
{'cls': 'File', 'name': 'camera', 'owner': 'guest', 'otherUserPermission': 7, 'content': ['nikkon']} <class 'dict'>
```

Data is saved in 'fs.txt' file in JSON format.

