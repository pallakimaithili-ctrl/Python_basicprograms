#zip()->we can combine multiple collections into one collection(list into relation int the form of list,tuple or set)
'''
a=[10,20,30,40,50]
names=["nivedh","harsha","yogitha","vignesh","satya"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)
'''

#anonymous functions(nameless functions)
#syntax
#a=lambda arg:expr

#write a function to calculate 2*x+5 where x=5

'''def f(x):
    print(2*x+5)
f(5)'''

#in anonymous functions:

'''a=lambda arg:2*x+5
print(a(5))'''

'''a=int(input("value"))
b=lambda a:2*x+5
print(b(a))'''

#product

'''a=lambda x,y:x*y
print(a(4,5))'''

'''a=int(input("a value"))
b=int(input("b value"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a=codegnan
b=lambda a:a.upper()
print(b(a))'''
#or
'''b=lambda a:a.upper()
print(b("codegnan"))'''

#fname+lname=fullname
'''
fname=input("first name:")
lname=input("last name:")
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))
'''

#filter
'''a=[10,20,30,40,50,]
if a%2==0:
    print(a)'''#error

'''a=[10,20,30,40,50,]
for i in a:
    if i%2==0:
     print(i)'''

#instead of that,to get as list:
'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#filter on [],(),set(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{}," ",None,3.5,6,"pooja"7+9j,True,False]
b=list(filter(None,a))
print(b)'''

