class Human():
    def __init__(self, name, eye_color3, age, height,speed):
        print("a new human is born")
        self.name = name
        self.eye_color = eye_color3
        self.age = age
        self.height = height
        self.speed=speed
        self.

    def introduce(self):
        print(f"{self.name} is {self.age} years old, {self.height}cm tall and has {self.eye_color} eyes. Pretty, right? Oh he also walks {self.speed} per hour")

    def set_eye_color(self, new_color):
        self.eye_color = new_color

    def birthday(self):
        print(f"Happy Birthday {self.name} you are {self.age} years old today.")
        self.age += 1

    def run(self,distance):
        return distance/self.speed
    
    def race(self,other,distance):
        print(f"{self.name} arrived after {self.run} seconds. {other.name} later")


matt = Human("Matt", "blue", 12, 180,7)
print(matt.eye_color)

rick = Human("Rick", "green", 30, 190,8)
print(rick.eye_color)

dan = Human("Dan", "red", 40, 170,9)
print(dan.eye_color)


rick.introduce()
matt.introduce()
matt.set_eye_color("yellow")
matt.introduce()
matt.birthday()
matt.birthday()
matt.distance(30)
matt.race(dan)
