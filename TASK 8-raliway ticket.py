#TASK 7:railway ticket with what we've learnt so far
while True:
    def railway_ticket():
            ticket=1000
            gender=input("Gender:")
            age=int(input("Age"))
            if gender=="m":
                if age>=60:
                   print("seniour citizen")
                   ticket=ticket-30/100*ticket
                   print(ticket)
                elif age<60:
                   print("normal citizen")
                   print(ticket)
            elif gender=="f":
                 if age>=60:
                   print("seniour citizen")
                   ticket=ticket-50/100*ticket
                   print(ticket)
                elif age<60:
                   print("normal citizen")
                   ticket=ticket-30/100*ticket
                   print(ticket)
    railway_ticket()
