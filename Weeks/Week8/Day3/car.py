class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        self.passengers = None
    
    def add_passenger(self,passenger):
        self.passengers = passenger
        passenger.passenger_of.append(self)
class Human:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.passenger_of = []

car_1 = Car("BMW","blue")
human_1 = Human("Carl",24)
print(car_1.brand)
car_1.add_passenger(human_1)
print(car_1.passengers.name)
print(human_1.passenger_of)


