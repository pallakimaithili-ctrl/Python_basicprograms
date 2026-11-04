#CONDITIONS

#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=2
b=4
if a<b:
    print("True")'''

'''a=3
b=6
if a>b:
    print("True")'''

'''a=10
b=15
if a<=b:
    print("less")'''

'''a=20
b=40
if a>=b:
    print("true")'''

'''a,b=7,11
if a!=b:
    print("not equal")'''

'''a,b=7,7
if a==b:
    print("not equal")'''

#this works for strings as well!
#you can also use run_time inputs() to input values from user!

#if-condition by using logical operators
#and,or,not

#and
'''a,b=5,10
if a<b and b>=a:
    print("true")'''

'''a,b=4,8
if a<=b and b>=a:
    print("true")'''

'''a,b=3,6
if a!=b and a==b:
    print("true")'''

#or

'''a,b=8,12
if a<b or b>a:
    print("true")'''

'''a,b=13,15
if a>=b or a<=b:
    print("true")'''

'''a,b=10,20
if a!=b or a==b:
    print("true")'''

#not-you have to mention it immediately after if not like and ,or

'''a,b=4,6
if not a<b:
    print("true")'''

'''a,b=4,6
if not a>b:
    print("true")'''

'''a,b=7,11
if not a<b and b>a:
    print("true")'''

#if-condition by using identify operators
#is,is not
#idetify means we can use type casting!

'''a=5
if type(a) is int:
    print("it is int")'''

'''a=5.8
if type(a) is not int:
    print("it is not int")'''

'''a=float(input("value:")
if type(a) is float:
        print("it is float")'''

#note:we can consider int as float as well since it can be converted into float.eg:3 can be written as 3.0


#if-condition by using membership operators
#in,not in

a=3,4,5,6,7,8,9,10
'''if 10 in a:
    print("true")
if 30 not in a:
    print("true")'''

'''a=int(input("a value:"))
if 50 in a:
    print("true")'''#it will raise error

#the right way->

'''a=[5,6,7,8,9,10]
b=int(input("value"))
if b in a:
    print("true")'''
