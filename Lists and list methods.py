Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #list[]
>>> a=[2,4.5,6+9j,True,False]
>>> type(a)
<class 'list'>
>>> b=[4.5]
>>> type(b)
<class 'list'>
>>> #can have only one thing in the list too!
>>> a=["python","java","c","c++"]
>>> #list methods
>>> #appends(0
>>> a.append("ml")
>>> a
['python', 'java', 'c', 'c++', 'ml']
>>> a.append("ai","ds")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ai","ds")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ai","ds"])
>>> a
['python', 'java', 'c', 'c++', 'ml', ['ai', 'ds']]
>>> #extend()
>>> a=["ai","ml","ds"]
>>> a.extend(["python","java"])
>>> a
['ai', 'ml', 'ds', 'python', 'java']
>>> #insert()
>>> b=["black","white"]
>>> b.insert(1,"red")
>>> b
['black', 'red', 'white']
>>> #index()
>>> b.index("black")
0
>>> b.index("red")
1
b.index("white")
2
b.index("purple")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.index("purple")
ValueError: list.index(x): x not in list
a=b
a
['black', 'red', 'white']
a.copy()
['black', 'red', 'white']
b=a.copy()
b
['black', 'red', 'white']
#can equate a list and b list in the above two ways
#can equate a list and b list in the above two ways
#sort()
c=[7,3,9,11,70,2,0,6]
c.sort()
c
[0, 2, 3, 6, 7, 9, 11, 70]
d=["python","java","ai","ml","ds"]
d.sort()
d
['ai', 'ds', 'java', 'ml', 'python']
#reverse()
d.reverse()
d
['python', 'ml', 'java', 'ds', 'ai']
a.reverse()
a
['white', 'red', 'black']
#it doesn't give the result in alphabetical order when in reverse,it simply reverses the order of the list
#pop()
a.pop("white")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
a.pop()
'black'
a
['white', 'red']
#it pops the last object in the list!
#it pops the last object in the list!but if you want to remove a specific object do the following
a.pop(1)
'red'
a
['white']
#use it's position!
#use it's position!
#to remove directly:
#remove()
d.remove("ai")
d
['python', 'ml', 'java', 'ds']
#clear()
a.clear()
a
[]
