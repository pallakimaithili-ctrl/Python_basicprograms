Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> print(a)
10
>>> b=40
>>> print(B)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(B)
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> # rule 1 -python is case sensitive.
>>> print(Z)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined
>>> Z=10
>>> print(Z)
10
>>> 4=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> #rule 2- can't use numbers as variables.
>>> a4=50
>>> print(a4)
50
>>> D0123456789=456
>>> print(D0123456789)
456
>>> a=3,b=10
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> #rule 3 -don't give commas between two variable instead use semicolon
>>> a=3;b=10
>>> print(a,b)
3 10
>>> a,b=3,10 #allowed
>>> print(a,b)
3 10
>>> a,b,c=3,10,15
>>> a,b,c,d=3,10,13,17
>>> print(a,b,c)
3 10 13
>>> a,b,c=18,36,47,48
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,b,c=18,36,47,48
ValueError: too many values to unpack (expected 3)
>>> #no of variables must be equal to number of values given
>>> name="Army"
>>> print(name)
Army
>>> #variables can also be words however those words mustn't be keywords.
>>> Name="Army"
>>> print(Name)
Army
>>> NAME="Army"
>>> print(NAME)
Army
>>> #can also include capitol letters as given above as long as they aren't a keyword.
>>> a=56
>>> print(a)
56
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a4'?
>>> #to delete a keyword,just use'del' as shown above
