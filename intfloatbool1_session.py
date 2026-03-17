Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> x = 3.75
>>> print(type(x), x)
<class 'float'> 3.75
>>> # former ersions of python allowed print as a statement
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> # both print as a statement and function work in python 2.7
>>> print("x is %s with value %f" % (type(x), x))
x is <class 'float'> with value 3.750000
>>> print("x is %s with value %3.2f" % (type(x), x))
x is <class 'float'> with value 3.75
>>> # above 2 prints shows old way of string formatting
>>> print("x is {} with value {}".format(type(x), x))
x is <class 'float'> with value 3.75
>>> # above is newer way of formatting
>>> print(f"x is {type(x)} with value {x}")
x is <class 'float'> with value 3.75
>>> # above is newest way to do string formatting and is recommended
>>> i = 15
>>> k = 9
>>> divki = k/i
>>> divki
0.6
>>> divki = int(k/i)
>>> divki
0
>>> i
15
>>> bool(i)
True
>>> j = 0
>>> bool(j)
False
>>> k = -1
>>> bool(k)
True
>>> i and j
0
>>> i or j
15
>>> not i
False
>>> not j
True
>>> i == j
False
>>> i != j
True
