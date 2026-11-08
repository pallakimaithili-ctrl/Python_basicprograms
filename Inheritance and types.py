#inheritance
#single-inheritence
'''
class RBI():#parent class
    cash=1000000
    def available_cash(cls):
        print("available cash is ",cls.cash)
        print("available cash is ",RBI.cash)
class SBI(RBI):#child-1
    pass
class HDFC(RBI):#child-2
    cash=50000
    def new_cash(cls):
        print("new cash is ",cls.cash+cls.cash)
        print("new cash is ",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()
'''

#multiple inheritence
#class->father->height->5.5
#class->mother->weight->60kgs
#class->chil->dob->...
'''
class father():#parent-1
    def height(self):
        print("5.5 inches")
class mother():#parent-2
    def weight(self):
        print("60 kgs")
class child():
    def dob(self):
        print("just born..")
a=father()
a.height()
b=mother()
b.weight()
c=child()
c.dob()
'''
#with multiple inheritance:
'''
class father():#parent-1
    def height(self):
        print("5.5 inches")
class mother():#parent-2
    def weight(self):
        print("60 kgs")
class child():
    def dob(father,mother):
        print("just born..")

c=child()
c.dob()
c.height()
c.weight()
'''

#multi-level inheritence
#grandparent->land
#parent->house
#child->bike
'''
class grandparent():
    def land(self):
        print("2 acres")
class parent(grandparent):
    def house(self):
        print("100 sqft")
class child(parent):
    def bike(self):
        print("bike")
c=child()
c.land()
c.house()
c.bike()
'''

#hierarchical inheritence
#employee->company name(parent)
#developer->develop(child-1)
#trainer->teaching(child-2)
'''
class Employee():
    def company_name(self):
        print("codegnan")
class developer(Employee):
    def develop(self):
        print("develop the code")
class trainer(Employee):
    def teaching(self):
        print("teach the code")
a=developer()
b=trainer()
a.develop()
a.company_name()
b.teaching()
b.company_name()
'''

#hybrid inheritance
#person->details
#trainer->teach
#student->study
#program_manager->managing->trainer,student
'''
class person():
    def details(self):
        print("pooja")
class trainer(person):
    def teach(self):
        print("teaching")
class student(person):
    def study(self):
        print("learn")
class program_manager(trainer,student):
    def manage(self):
        print("assign the work")
a=program_manager()
a.details()
a.teach()
a.study()
a.manage()
'''

#super()->we can't directly access parent function with out using super in this
'''
class parent():#super class
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#derived class
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("pooja",28)
print(a.name)
print(a.age)
'''
        
#encapsulation->combining multiple units into single unit.
#we have three types:
#publicdata
#_protecteddata
#__privatedata

#publicdata
'''
class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
a=child()
a.method1()
a.method2()
'''

#_protecteddata
'''
class parent():
    _protecteddata="pooja"
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
a=child()
a.method1()
a.method2()
print(a._protecteddata)
'''

#__privatedata
'''
class parent():
    __privatedata="pooja"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
a=child()
a.method1()
a.method2()
'''

#abstraction->hiding internal implementation details and exposing only the essential functionality to the user

'''class parent():
    def method1(self):
        pass
obj=parent()
obj.method1()'''
'''class parent():
    def method1(self):
        print("python full stack")
obj=parent()
obj.method1()'''

'''
from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("data")
obj=A()
obj.method1()
'''
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data")
obj=A()
obj.method1()'''#error,here only one method is given but abstraction means it needs more than one method

'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj=B()
obj.method1()
obj.method2()
obj.method3()
'''
