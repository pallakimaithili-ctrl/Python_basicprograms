Python 3.14.7 (v3.14.7:823f0323ee6, Aug  5 2026, 07:07:01) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#TASK 2
#to swap two values

a=10
b=20
temp=a
a=b
b=temp
print("final value of a",a)
final value of a 20
print("final value of b",a)
final value of b 20
print("final value of b",b)
final value of b 10

#2:
>>> 
>>> a=10
>>> b=20
>>> 
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print("final value of a",a)
final value of a 20
>>> print("final value of b",b)
final value of b 10
>>> 
>>> #3:
>>> 
>>> a=10
>>> b=20
>>> 
>>> a,b=b,a
>>> print("a=%d",a)
a=%d 20
>>> print("b=",b)
b= 10
>>> #python doesn't have format specifiers like in c.please don't forget for the love of god!
>>> 
>>> #4:
>>> 
>>> a=10
>>> a=10
>>> b=20
>>> 
>>> #4 is the same as 3 but printing is done using format specifiers,i have used the wrong notation-_-
>>> 
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print("after swapping,a=%d,b=%d"%(a,b))
after swapping,a=20,b=10
