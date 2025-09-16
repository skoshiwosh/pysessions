Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### list comprehension and generators ###
>>> squares = []
>>> for x in range(5):
...     squares.append(x ** 2)
... 
...     
>>> squares
[0, 1, 4, 9, 16]
>>> powlist = [i ** 2 for i in range(5)]
>>> powlist
[0, 1, 4, 9, 16]
>>> comp_list = [j ** 2 for j in range(7) if j % 2 == 0]
>>> comp_list
[0, 4, 16, 36]
>>> gen_list = (j ** 2 for j in range(7) if j % 2 == 0)
>>> gen_list
<generator object <genexpr> at 0x104e2aa80>
>>> for x in gen_list:
...     print(x)
... 
...     
0
4
16
36
>>> ### note generator uses less memory but is slower in execution ###
>>> mystr = "suzanne berger is trying"
>>> listfromstr = [x for x in mystr if x != " "]
>>> listfromstr
['s', 'u', 'z', 'a', 'n', 'n', 'e', 'b', 'e', 'r', 'g', 'e', 'r', 'i', 's', 't', 'r', 'y', 'i', 'n', 'g']
>>> my_iterator = iter(comp_list)
>>> next(my_iterator)
0
>>> next(my_iterator)
4
>>> next(my_iterator)
16
