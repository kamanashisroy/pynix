
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

Create a README file

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

Also read a directory or file.

```
cat /root
cat /root/goody
cat /root/README
```

#### Mkdir command

Create a goody directory

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

#### Chmod command

Set read,write and execute permission.

```
chmod /root 0b111
('Changing permission', '/root')
('Permission Of Others', 7)
('============================ Success',)
```

#### Login command

```
login admin admin
('============================ Success',)
```

