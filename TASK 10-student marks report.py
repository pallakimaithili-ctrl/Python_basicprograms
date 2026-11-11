#TASK 10:mark analysis report

students=int(input("enter te total no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print("marks analysis report..")
print("total students:",students)
print("highest marks:",max(marks))
print("lowest marks:",min(marks))
print("total marks:",sum(marks))
print("average is:",sum(marks)/students)
    
