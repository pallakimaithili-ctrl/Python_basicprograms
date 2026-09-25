Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#datatypes
a=3
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="code gnan"
type(d)
<class 'str'>
e='''python'''
type(e)
<class 'str'>
f=5+6j
type(f)
<class 'complex'>
g=7j
type(g)
<class 'complex'>
j=5+8j
type(j)
<class 'complex'>
i= 5-6j
type(i)
<class 'complex'>
k=5-8i
SyntaxError: invalid decimal literal
type(k)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(k)
NameError: name 'k' is not defined
#i is not the default used for imaginary numbers in python
c=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
#true is a keyword so error is given
c='true'
type(c)
<class 'str'>
#data conversions
#int
int(8)
8
int(6.9)
6
int("python")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(4+9j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(4+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(true)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(false)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
int(False)
0

#float
float(5)
5.0
float(3.4)
3.4
float("pooja")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float("pooja")
ValueError: could not convert string to float: 'pooja'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(true)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
float(false)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(True)
1.0
float(False)
0.0
#string
str(6)
'6'
str(7.8)
'7.8'
>>> str(6+6j)
'(6+6j)'
>>> str("hi")
'hi'
>>> str(True)
'True'
>>> str(true)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> str(false)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    str(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> str(False)
'False'
>>> #Complex
>>> complex(6)
(6+0j)
>>> complex(3.4)
(3.4+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(3+4j)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex(true)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> complex(false)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> #boolean
>>> bool(7)
True
>>> bool(7.5)
True
>>> bool(7+7j)
True
>>> bool("hello")
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(true)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> bool(false)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    bool(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
