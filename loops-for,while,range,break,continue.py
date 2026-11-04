#loops()
#for(),while(),range(),break(),continue()

#for()->sequence iteration
'''a=[10,20,30,40,50]'''

'''for i in a:
    print(i)'''#result:
#10
#20
#30
#40
#50

'''for i in a:
    print(i,end=" ")'''#result:10 20 30 40 50

#to print types
'''a=[3,4,5,6,7]'''#list

'''for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(5,6,7,8,9)'''#tuple

'''for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={1,2,3,4,5,6,7,8,9}'''#set
'''for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
'''d={"Name":"pooja","city":"vja","year":2026}'''#dict
'''for i in d:
    print(i)         '''#since, it is built in for for loop,it will only show keys so we use functions as we did below
'''for i in d.keys():
    print(i)
    print(type(d))
    print(type(i))
for i in d.values():
    print(i)
    print(type(d))
    print(type(i))
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))'''

'''a=[4,5.6,"pooja",7+7j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#while()->continuos iteration
a=10
'''while a>1:
    print(a)'''# it goes on forever like this
'''while a>1:
    print(a)
    a=a-1'''
'''while a>1:
    a=a-1
    print(a)'''
'''while a>1:
    a=a-1
print(a)'''#there is a small difference between the above mentioned three.
#range()
#start-stop-step
'''for i in range(10):
    print(i)'''
'''for i in range(10,31):
    print(i)'''

#break()-it doesn't work without for or while loop
'''while a>1:
    print(a)
    a=a-1
    if a==6:
        break
    print(i)'''
'''q="python"
for i in q:
    if i=="h":
        break
    print(i)'''

#continue-the number we gave will be skipped and then everything will go on as per the given condition
'''a=20
while a>5:
   a=a-1
   if a==10:
        continue
   print(a)''' 

#pass - a special loop-it is a place holder used for OOPs concept
'''a=20
while a>5:
   print(a)
   a=a-1
   if a==10:
        pass'''
   


#nested-loops
'''for i in range(1,4):
    for j in range(1,3):
        print(i,j)'''
