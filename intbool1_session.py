Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> i = 2
>>> j = 3
>>> k = 6
>>> i + j * k
20
>>> (i + j) * k
30
>>> i += 1
>>> i
3
>>> i *= 5
>>> i
15
>>> k = j ** 2
>>> k
9
>>> i % k
6
>>> i / k
1.6666666666666667
>>> k >> 2
2
>>> k_bin = bin(k >> 2)
>>> k_bin
'0b10'
>>> type(k)
<class 'int'>
>>> type(k_bin)
<class 'str'>
>>> i < 0
False
>>> if i >= 0:
...     print('variable "i" is greater than zero')
... 
...     
variable "i" is greater than zero
>>> if (i >= 0):
...     print("parenthesis can help readability as well as enforcing precedence")
... 
...     
parenthesis can help readability as well as enforcing precedence
>>> if (i > 0) and (j > 0):
...     print('both "i" and "j" are greater than zero')
... 
...     
both "i" and "j" are greater than zero
>>> if (i > 0) and (k < 0):
...     print("yup")
... else:
...     print("nope")
... 
...     
nope
