#Expressions for variables in collection/range

#print(),len(),input(),range(),max(),min(),sum(),type()

print(4+8)

a=4,5,6,7,8,9
print(len(a))

b=input("data")
print(b)

for i in range(21):
    print(i)

a=4,5,6,7,8,9
print(max(a))

print(min(a))

#print(sum(5,6))#error since we can't give direct values for sum()
#2 methods:

a=4,5,6,7,8,9
print(sum(a))
print(sum(list(a)))

c=4
print(type(c))
