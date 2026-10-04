Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#sets{}
a={3.5,4,"love",7+7j,True,False}
print(a)
{False, True, 3.5, 4, 'love', (7+7j)}
type(a)
<class 'set'>
b={5,6,7,8,2,4,6,8,7}
b
{2, 4, 5, 6, 7, 8}
#doesn't repeat values!
#add()
a.add(9)
a
{False, True, 3.5, 4, 'love', 9, (7+7j)}
a.add(True)
a
{False, True, 3.5, 4, 'love', 9, (7+7j)}
#since, what i have given is already there and sets don't repeat values, no change happens
#issubset()
a={1,2,3,4,5,6,7}
b={1,4,7}
b.issubset(a)
True
a.issubset(b)
False
c={}
c.issubset(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.issubset(a)
AttributeError: 'dict' object has no attribute 'issubset'
#issuperset()
b.issuperset(a)
False
a.issuperset(b)
True
a.issuperset(a)
True
c.issuperset(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c.issuperset(a)
AttributeError: 'dict' object has no attribute 'issuperset'
#here,empty sets don't work??
#intersection()
a.intersection(b)
{1, 4, 7}
b.intersection(a)
{1, 4, 7}
#both are same!!
#difference()
a.difference(b)
{2, 3, 5, 6}
b.difference(a)
set()
a.difference(a)
set()
\
a.difference(a)
set()
a
{1, 2, 3, 4, 5, 6, 7}
#update()
a
{1, 2, 3, 4, 5, 6, 7}
b
{1, 4, 7}
a.update(b)
b
{1, 4, 7}
a
{1, 2, 3, 4, 5, 6, 7}
b.update(a)

a
{1, 2, 3, 4, 5, 6, 7}
b
{1, 2, 3, 4, 5, 6, 7}
#soit only works when we are replacing the set which is a smaler set??
a={2,3,4,5,6,7}
b={4,5,6,7}
#symmetric_difference()
a.symmetric_difference(b)
{2, 3}
#difference_update()
a={2,3,4,5,6,7}
b={4,5,6,7}
SyntaxError: multiple statements found while compiling a single statement
b={4,5,6,7}
a.difference_update(b)
a
{2, 3}
b.difference_update(a)
b
{4, 5, 6, 7}
#removes the similar vales and gives the different values
#intersection_update()
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection_update(b)
a
{8, 9, 6, 7}
b
{6, 7, 8, 9, 10, 11}
a={3,4,5,6,7}
b={6,7,8,9,10}
#symmetric_difference_update()
a.symmetric_difference_update(b)
a
{3, 4, 5, 8, 9, 10}
b.symmetric_difference_update(b)
b
set()
set()
set()
a={7,8,9,10}
a.copy()
{8, 9, 10, 7}
b=a.copy()
a=b
a
{8, 9, 10, 7}
>>> b
{8, 9, 10, 7}
>>> #pop()
>>> a.pop()
8
>>> a
{9, 10, 7}
>>> #remove()
>>> a.remove(10)
>>> a
{9, 7}
>>> #discard()
>>> a.discard(7)
>>> a
{9}
>>> #discard=remove and 'b=a.copy()'='a=b'
>>> #clear()
>>> a.clear()
>>> a
set()
>>> #empty set will not be denoted by {} but by set()
>>> #add()
>>> b=set()
>>> b.add(10)
>>> b
{10}
>>> #disjoint()
>>> a={1,2,3,4}
>>> b=set()
>>> a.isdisjoint(b)
True
>>> b.issubset(a)
True
>>> b.isdisjoint(a)
True
>>> #in setssice there are no repeated values store,count doesn't work!
>>> len(a)
4
