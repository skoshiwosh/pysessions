Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### list methods ###
>>> newstr = '***foobar***'
>>> komy = 'lala'
>>> mylist = [newstr, komy, 3, 12, 'a', 'z', 'c']
>>> mylist[1] = 'b'
>>> mylist
['***foobar***', 'b', 3, 12, 'a', 'z', 'c']
>>> mylist.reverse()
>>> mylist
['c', 'z', 'a', 12, 3, 'b', '***foobar***']
>>> mylist.sort()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mylist.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> mylist
['a', 'c', 'z', 12, 3, 'b', '***foobar***']
>>> len(mylist)
7
>>> mylist[0:1] = ['x', 'r', 't']
>>> mylist
['x', 'r', 't', 'c', 'z', 12, 3, 'b', '***foobar***']
>>> mylist.count('t')
1
>>> mylist.sort()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    mylist.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> mylist
['c', 'r', 't', 'x', 'z', 12, 3, 'b', '***foobar***']
>>> del mylist[5:6]
>>> mylist
['c', 'r', 't', 'x', 'z', 3, 'b', '***foobar***']
>>> del mylist[5]
>>> mylist
['c', 'r', 't', 'x', 'z', 'b', '***foobar***']
>>> mylist.sort()
>>> mylist
['***foobar***', 'b', 'c', 'r', 't', 'x', 'z']
>>> mylist.append('h')
>>> mylist
['***foobar***', 'b', 'c', 'r', 't', 'x', 'z', 'h']
>>> del mylist[0:2]
>>> mylist
['c', 'r', 't', 'x', 'z', 'h']
>>> mylist.extend(['y', 'x', 'c'])
>>> mylist
['c', 'r', 't', 'x', 'z', 'h', 'y', 'x', 'c']
>>> mylist.sort()
>>> mylist
['c', 'c', 'h', 'r', 't', 'x', 'x', 'y', 'z']
>>> mylist.pop()
'z'
>>> mylist
['c', 'c', 'h', 'r', 't', 'x', 'x', 'y']
