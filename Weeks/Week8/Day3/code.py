"""
Car Class
Attributes
    - color
    - manufacturer
    -travelled_km


Methodes
    - print_info --> Print some info about the car
    - travel(self,distance) --> Travel the given distance (print "the car travelled 65 km and increment the travelled distance by 65 )

"""

class Car:
    def __init__(self, color, manufacturer):
        self.color = color 
        self.manufacturer = manufacturer
        self.travelled_km = 0

    def travel(self,distance):
        self.travelled_km += distance
    
    def print_info(self):
        print(f"The car is {self.color} from {self.manufacturer} and travelled {self.travelled_km} km")

car1 = Car("yellow","Ford")
car2 = Car("brown","BMW")
car1.travel(65)
car1.travel(20)
car1.travel(10)
car1.print_info()