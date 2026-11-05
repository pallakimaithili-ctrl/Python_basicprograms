#Functions

#used to reduce the no of times we type the same code for  a particular calculations
'''def calculate(a,b):
    print("sum is ",a+b)
    print("diff is ",a-b)
    print("product is ",a*b)
calculate(10,20)
calculate(100,200)'''

#**,%,//
'''def calculate(a,b):
    print("power is ",a**b)
    print("mod is ",a%b)
    print("int div is ",a//b)
calculate(10,20)
calculate(100,200)'''

#diff between print and return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
''' #return c
    #return d
    #return e
'''
    return c,d,e
print(cal(2,4))'''

#we must use print in return so we can see the result
#the difference is that print can be used n no of times but return will only give values when given in one line as we have done above

#keyword and positional arguments

'''def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

#positional argument->
'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id=70,name="pooja",mailid="p@gmail.com")
Details("pooja",70,"p@gmail.com") '''#here,it will print as it is if we don't give keyword
'''Details(id=71,mailid="s@gmail.com",name="siddarth")''' #even though,we have given the wrong order,it prints according to the order since we mentioned the keywords!

