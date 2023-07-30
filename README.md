
In memory filesystem
====================

It has directories, files and users.

How to use
============

#### Invoking the pynix

```
python3 pynix.py 
```

#### Help command

```
python3 pynix.py 
pynix > dict_keys(['cat', 'mkdir', 'help', 'quit'])
help
executing help
SYNOPSIS
		help command_name
Display usage of a command.
============================ Success
```

#### cat command

```
cat /root/README hello
executing cat /root/README hello
checking path  ['/root/README', 'hello']
Showing path /root/README
Name README
Owner admin
Permission Of Others None
Content ['hello']
============================ Success
```

#### Mkdir command

```
mkdir /root/goody
executing mkdir /root/goody
checking path  ['/root/goody']
Showing path /root/goody
Name goody
Owner admin
Permission Of Others None
Sub directories dict_keys(['goody'])
```
