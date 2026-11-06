#default arguments in functions
#1
'''
def Grocery(item,price):
    print("item is %s"%item)
    print("price is %f"%price)
Grocery("rice",100)
'''
#2
'''
def Grocery(item="rice",price=100):
    print("item is %s"%item)
    print("price is %f"%price)
Grocery()
'''
#3
'''
def Grocery(item,price=100):
    print("item is %s"%item)
    print("price is %f"%price)
Grocery("rice")
'''
#4->this method is wrong because non def arg doesn't follow non-default arg.so,either we have to give details for both or keave the item and give the price and then when calling mention the item but vice versa can't be done
'''
def Grocery(item="ghee",price):
    print("item is %s"%item)
    print("price is %f"%price)
Grocery(100)
'''

#* arguments-> * is used to unpack elements

'''list
a=[2,3,4,5,6,7]
print(a)
print(*a)'''

'''tuple
b=(2,3,4,5,6,7)
print(b)
print(*b)'''

'''set
c={2,3,4,5,6,7}
print(c)
print(*c)'''

'''dict
d={"name":"pooja","city:"vja"}
print(d)
print(*d)'''#it will print only keys when * is applied

'''string
e="codegnan"
print(e)
print(*e)'''#it will print with spaces in between


#speciality of * argument:
'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4,5,6,7
print(a)
print(b)
print(c)'''#this will give value error normally

#but, in * argument,
'''*a,b,c=2,3,4,5,6,7
print(*a)
print(b)
print(c)'''
#here, more than one * variable shouldn't be used!⭐️

#variable length arguments

#to check the type->
'''
def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6,7]
check(*b)
c=(2,3,4,5,6,7)
check(*c)
'''
'''
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
    print(d)
check1()
check1(2,3,4,5,6,7)
'''
#it will add all these and gives result

#kwargs()
'''
def check(**a)
    print(a)
    print(type(a))
check()
details={"name":["Nivedh","Yaswanth","Jaswanth"],"marks":[60,70,90]}
check(**details)
'''
#to print only keys or both instead of the whole dictionary:
'''
def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])#without func
    for i in a.values:
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items:
        print(i)
check()
details={"name":["Nivedh","Yaswanth","Jaswanth"],"marks":[60,70,90]}
check(**details)
'''




#both * and ** usage
'''
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is ",i)
        print("item is ",j)
final()
data=(2,3,4,4.5,2.3,3.3)
final(*data)
details={"names":["anusha","ambica"],"places":["vja","hyd"]}
final(**details)
final(*data,**details)
'''
#global and local variables
#the variable is declared inside and outside the function's is called global and local variables respectively
#a variable is defined above/outside the function and is accesible to the entire global space is a global variable
#a variable is defined inside the function is a local variable
#case-1 of global variables
'''a=5
def check1():
    print("inside value is ",a)
check1()
print("outside value is ",a)'''
#case-2 of global varibles
'''a=4
def check2():
    a=5
    a=a**2
    print("inside value is ",a)
check2()
print("outside value is ",a)'''
#case-3 of both global and local variables in single code
'''a=2
def check3():
    a=10
    print("inside value is ",a)
    a=15
    print("updated value is ",a+5)
    b=12#local variable
    b=b+a
    print("value of b is ",b)
check3()
print("a value is ",a)
print("b value is ",b)'''#this will giove you error as it is not a global variable

#usage of global keyword
#when user wants to create a variable inside the function directly and carry forward the updated value given outside the function then we need to use global keyword
'''a=4
def final():
    global a
    print("inside value is ",a)
    a=10print("updated value is ",a)
    b=15
    b=b+a
    print("b value is ",b)
final()
print("value of a is ",a)
print("value of b is ",b)'''

