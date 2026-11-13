#pass by value:
#a copy of the value is passed to the function, changes made inside the function don't affect the original value
'''
def data(x):
         x=10
         print("inside value is:",x)
a=1
data(a)
print("outside value is:",a)
'''
#this is mutable->we can change

#pass by reference:
#the function receives a reference to the same object, changes made to the new object can affect the original object
'''
def data(x):
    #x[0]=10
    x[1]="pooja"
    print("inside value is:",x)
a=[10,20,30,40]
data(a)
print("outside value is:",a)
'''
#immutable->can't change

