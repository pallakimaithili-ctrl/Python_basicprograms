Python 3.13.14 (v3.13.14:fd17997c386, Jun 10 2026, 08:55:00) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#TYPES OF OPERATORS
#Arthematic
a,b=3,6
a+b
9
print(a-b)
-3
a*b
18
a/b
0.5
a//b
0
a%b
3
a**b
729
#Assignment
a,b=3,4
a+=b
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
11
#since i typed it two times it's 11
a-=b
a
7
a*=b
a
28
a/=b
a
7.0
#can also give numbers instead of b
a**=5
a
16807.0
a%=4
a
3.0
#Comparision
a,b=4,8
a,b
(4, 8)
a<b
True
a>b
False
b<a
False
b>a
True
a<=b
True
a>=b
False
a!=b#a not equal to b
True
>>> a==b
False
>>> a=b
>>> a
8
>>> b
8
>>> #this is the difference between '=' and '=='
>>> #logical
>>> a,b=8,10
>>> a>b and b<a
False
>>> a<=b and a=b
SyntaxError: cannot assign to expression
>>> a<=b and a==b
False
>>> a!=b and a==b
False
>>> a<=b or b>=a
True
>>> a!=b or a==b
True
>>> not True
False
>>> not False
True
>>> #identity
>>> #is,is not
>>> a=5
>>> type(a) is int
True
>>> type(a) is not float
True
>>> #Membership
>>> a=1,2,3,4,5,6,7
>>> 10 in a
False
>>> 7 in a
True
