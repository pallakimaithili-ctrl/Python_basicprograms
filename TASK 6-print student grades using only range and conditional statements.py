#TASK 6-print student grade using only range and conditional statements
marks=int(input("enter the marks"))
if marks in range(91,101):
    print("Grade-A")
elif marks in range(81,91):
    print("Grade-B")
elif marks in range(71,81):
    print("Grade-C")
elif marks in range(50,71):
    print("Grade-D")
else:
    print("FAIL")
