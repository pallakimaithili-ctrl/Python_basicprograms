#Exception handling

#try->instructions from which we are expecting the exceptions
#except->exceptions are raised in try block and it will be handled by this block
#else->optional(no exceptions)
#finally->always
'''
a=int(input("a value:"))
b=int(input("b value:"))
try:
    c=a/b
    print(c)
except:
    print("exception is raised")
else:
    print("no exceptions")
finally:
    print("program ends...")
'''

#file handling
#write()
'''
a.open("print.txt","w")
a.write("codegnan")
a.close()

a.open("print.txt","w")
a.write("python")
a.close()
'''
#this will not give any output but we can find the output in the mentioned file
#but, in write() if we give another input in the same file the previous output will no tbe stored anymore


#append()

#method-1
'''
a=open("print.txt","a")
a.write("\tcoding")
a.close()
'''
#this will allow showing both previous and changed output in the mentioned file

#method-2->using run_time input
'''
a=open("print.txt","w")
b=input("data:")
a.write(b)
a.close()
'''
#or
'''
a=open("print.txt","w")
a.write(input("data"))
a.close()
'''

#method in file handling->readlines()
'''
a=open("print.txt")
print(a.readlines)#it will display with \n
print(a.read())#it will display entire content
print(a.read(8))#it will display no of characters given
print(a.readline())# it will display first line
'''
#method in file handling->writelines()->it makes every object appear one after the other which readlines can't do
'''
a=["pooja","anu","apu","sweety"]
b=open("print.txt","w")
b.writelines("\n".join(a))
b.close()
'''

'''
a=open("map,sorted,enumerate.py")
print(a.read())
'''#this will open and print the code directly

'''using path
a=open("C:\\Users\\rampallaki\\OneDrive\\Desktop\\edge\\run_time input.py")
#only add double slash when we get unique code error
print(a.read())
'''
