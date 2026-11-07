#OOPs->Object-Oriented Programming System
             #syntax
#class classmate():
           #attributes
#    name="pooja"
#    age=28
#    city="vja"
#    def fname(method_name):
#        print("statements...")
#a=classmate()
#a.fname()

#class declaration
'''
class Details():
    name="pooja"
    age=28
    city="vja"
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()
'''#where dir=directary=collection of files

#Object instantiation->to create objects instantaniously
'''
class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("priya",20,"vja")
a.display()
b=Details()
print(dir(b))
b.data("prem",21,"vja")
b.display()
'''

#Object instantiation using constructors
'''
class Details():'''
    #creating a constructor
'''
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("priya",20,"vja")
a.display()
b=Details()
print(dir(b))
b.data("prem",21,"vja")
b.display()
'''
#Methods of getting user input for the code
#1
'''
class Details():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()
'''
#2
'''
class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()
'''

#diff between _ and __
#when user wants to create __ ,our python interpreter treats it as a special variable to avoid name conflicts with methods and inner classes
'''
class Employee1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=1000000'''#private variable
'''
class Employee2():
    def __init__(self):
        self.name="priya"
        self._mailid="priya@codegnan.com"
        self.__salary=2000000       
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)'''
#print(a.__salary)#error will be given
'''print(a._Employee1__salary)
b=Employee2()
print(dir(a))
print(b.name)
print(b._mailid)
print(b._Employee2__salary)
'''

#polymorphism
#operator overloading
'''
a=3
b=4
print(a.__add__(b))#in oops,to avoid operator overloading ,we use this..
print(a.__sub__(10))
print(a.__mul__(1))
#print(a.__div__(2))'''#it is a directory ,so it doesn't exist here and will give error if used
'''print(a.__pow__(2))
print(a.__ge__(5))
print(a.__le__(10))
print(a.__eq__(9))
'''
'''
a=[2,3,4,5,6,7];b=[6,7,8,9,10,11,12]
print(a.__add__(b))
print(a.__getitem__(3))#getitem=index
print(b.__getitem__(6))
'''
'''
a="code";b="gnan"
print(a.__add__(" "+b))
a="python";b="course"
print(a.__add__(b).title())#if you want space in between
print("pooja".__add__(" ch").title())'''#we can add directly without variables!^^

'''
class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        self.a*value.b
class B():
    def __init__(self.b)
    self.b=b
x=A(4)
y=B(5)
print(x+y)
'''
#here, if we used inheritence,then we can use self.a*self.b directly!

#method overloading
'''
class new():
    def sum(self,a=None,b=None,c=None):
       if a!=None and b!=None and c!=None:
           print("the sum is ",a+b+c)
       elif a!=None and b!=None:
           print("the product is ",a*b)
       else:
            print("program ended")
x=new()
x.sum()
x.sum(2,5,7)
'''
