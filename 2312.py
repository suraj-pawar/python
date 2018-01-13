Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x="India"
>>> print x
India
>>> x[1]
'n'
>>> x[-4]
'n'
>>> x[1:4]
'ndi'
>>> x[:]
'India'
>>> x[3:]
'ia'
>>> x[:3]
'Ind'
>>> x[-7:]
'India'
>>> x[5:1]
''
>>> x[-6:]
'India'
>>> x[-5:-3]
'In'
>>> x[0:-3]
'In'
>>> x[-6:]
'India'
>>> x[::2]
'Ida'
>>> x[::-2]
'adI'
>>> [::-1]
SyntaxError: invalid syntax
>>> x[::-1]
'aidnI'
>>> 
>>> x="hello"
>>> x.capitalize()
'Hello'
>>> 
>>> x="suraj42pawar"
>>> x.isalnum()
True
>>> 
>>> x="suraj42pawar"
>>> x.isalnum()
True
>>> 
>>> x.islower()
True
>>> x.isalpha()
False
>>> x.isupper()
False
>>> 
>>> x="su raj"
>>> x.isspace()
False
>>> x="suraj"
>>> x.isspace()
False
>>> x=" "
>>> x.isspace()
True
>>> 
>>> x=["a","b","c","d"]
>>> x
['a', 'b', 'c', 'd']
>>> y="".join(x)
>>> y
'abcd'
>>> y=" ".join(x)
>>> y
'a b c d'
>>> 
>>> y="*".join("hello")
>>> y
'h*e*l*l*o'

>>> s="suraj"
>>> s.startswith('s')
True
>>> s.startswith('s',2)
False
>>> s.startswith('s',0)
True
>>> 
>>> s.index('s')
0


>>> s.find('s')
0
>>> s.index('A')

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.index('A')
ValueError: substring not found
>>> s.find("A")
-1


Deifference with statr index and end index 
>>> x="hello"
>>> x.count('l')
2
>>> x.count("l",0,3)
1
>>> 
>>> 