Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> nickname1 = "peanuts"
>>> nickname2 = 'bergerbits'
>>> allmynames = """
... peanuts
... bergerbits
... skoshiwosh
... zany
... """
>>> allmynames
'\npeanuts\nbergerbits\nskoshiwosh\nzany\n'
>>> print(allmynames)

peanuts
bergerbits
skoshiwosh
zany

>>> nickname1
'peanuts'
>>> nickname2
'bergerbits'
>>> # you can add strings together like numbers
>>> nickname1 + ' ' + nickname2
'peanuts bergerbits'
>>> # but prefarble to use f-string to format string
>>> f'{nickname1} {nickname2}'
'peanuts bergerbits'
>>> # above could be contained in print function
>>> print(f'{nickname1} {nickname2}')
peanuts bergerbits
>>> print(f'My nicknames are {nickname1} and {nickname2}')
My nicknames are peanuts and bergerbits
>>> # olders way to format strings
>>> print("My nicknames are {0} and {1}".format(nickname1, nickname2))
My nicknames are peanuts and bergerbits
>>> print("My nicknames are %s and %s" % (nickname1, nickname2))
My nicknames are peanuts and bergerbits
>>> # indexing into strings
>>> nickname1[0]
'p'
>>> nickname1[-1]
's'
>>> nickname1[3:5]
'nu'
>>> nickname1[0:-1:2]
'pau'
