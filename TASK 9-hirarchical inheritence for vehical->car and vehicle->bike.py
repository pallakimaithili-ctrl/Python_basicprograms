#TASK 9:hierarchical inheritence for vehicle->car and vehicle->bike

class car():
    def vehicle(self):
        print("thar")
class bike():
    def vehicle(self):
        print("vespa")
a=car()
b=bike()
a.vehicle()
b.vehicle()
