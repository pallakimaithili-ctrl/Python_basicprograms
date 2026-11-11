#map()->each object from a collection and forms a new collection
'''
a=[10,5,8,9,15,30,60,90]
b=[4,6,12,14,18,25,3,90]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)
'''
#sorted
'''
a=[10,40,15,30,60,2,9,25]
b=sorted(a)
print(b)

c=["banana","mango","apple","grapes"]
d=sorted(c)
print(d)
'''

#enumerate()->we can give counter to the collection

names=["anusha","pooja","ravali","naveena","priya"]
'''
for i in range(len(names)):
    print(i,names[i])
'''
'''
b=list(enumerate(names,10))
print(b)'''

