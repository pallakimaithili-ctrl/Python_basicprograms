Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #String Methods
>>> #len()=length of string
>>> a="Codegnan"
>>> len(a)
8
>>> b=""
>>> len(b)
0
>>> c=" "
>>> len(c)
1
>>> #space is also one character so it is consider in a length
>>> #space is also one character so it is consider in a length
>>> #count()
>>> a="twinkle twinkle little star"
>>> count()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count()
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> # this is the correct way of representing count
>>> #count = no of times a string/character is repeated in the given variable
>>> a.count(" ")
3
>>> a.count("a")
1
>>> #find a string
>>> a="python"
>>> a[3]
'h'
a.find("h")
3
#it will give the position of the character . if the given character is repeated it takes the first time it appears in the string given.
b="Hello"
b.find("l")
2
# if you ant both ,you have to do slicing
b[2:4]
'll'
#escape sequence
#\n = new line
#\t = tab space = 4 to 8 spaces
a="name\nphone number\tcity\nmail id"
print(a)
name
phone number	city
mail id
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
a.lower()
'python'
#capitalize()
a.capitalize()
'Python'
'Python'
'Python'
a="python course"
#title()
a.title()
'Python Course'
#Conditions for all these
a="data science"
a.isupper()
False
a.islower()
True
a.startswith("d")
True
a.endswith("e")
True
a.isalpha()
False
b="datascience"
b.alpha()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
b.isalpa()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b.isalpa()
AttributeError: 'str' object has no attribute 'isalpa'. Did you mean: 'isalpha'?
b.isalpha()
True
a.isdigit()
False
c="abc123"
c.isdigit()
False
c.isalpha()
False
c.isalnum()
True
a.isalnum()
False
b.isalnum()
True
#strip()
#lstrip(),rstrip()
a,strip()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a,strip()
NameError: name 'strip' is not defined
a="      code       "
a.strip()
'code'
a.lstrip()
'code       '
a.rstrip()
'      code'
#split()
a="python  java  c  c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python full stack"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
#join()
a.join()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.join()
TypeError: str.join() takes exactly one argument (0 given)
b.join()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    b.join()
TypeError: str.join() takes exactly one argument (0 given)
#cannot give single string to join()
a="apple","ball","cat"
"".join(a)
'appleballcat'
#only use the format above for join
"k".join(a)
'applekballkcat'
#works for letters in between too"
#Application
fname="Nobody"
lname="cares"
print(fname+lname)
Nobodycares
print(fname+" "+lname)
Nobody cares
print(fname.title()+" "+lname.title())
Nobody Cares
#alltogether title() means->
print((fname+" "+lname).title())
Nobody Cares
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
#so the above process is called concatenation
#formatting
a,b=4,7
print(a+b)
11
print("the sum is",a+b)
the sum is 11
#format method
x="motu"
y="patlu"
print("hello {}{}".format(a,b))
hello 47
print("hello {}{}".format(x,y))
hello motupatlu
#fstring
a="vijaya"
b="wada"
print(f"hello {a}{b}")
hello vijayawada
