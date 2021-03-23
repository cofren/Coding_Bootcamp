# #Exercise 1
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

#     def walk(self):
#         return f'{self.age} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Pretty(Cat):
#     pass

# cat1 = Cat("Gato1",1)
# cat2 = Cat("Gato2",2)
# cat3 = Cat("Gato3",3)
# my_cats = [cat1,cat2,cat3]
# all_cats = Pets(my_cats)
# all_cats.walk()





# # Exercise 2

# class Dog:
#     def __init__(self,name,age,weight):
#         self.name = name 
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print(" barks")
    
#     def run_speed(self):
#         return self.weight/self.age*10
    
#     def fight(self,other_dog):
        
#         first_dog = self.run_speed()
#         second_dog = other_dog.run_speed()
#         print(first_dog)

#         if first_dog > second_dog:
#             print(f"First dog wins")
#         elif first_dog < second_dog:
#             print(f"Second dog wins")
#         else:
#             print("Both dogs win")


# dog1 = Dog("Dog1",1,10)
# dog2 = Dog("Dog2",4,20)
# dog3 = Dog("Dog3",3,30)


# dog1.fight(dog2)


#Exercise 3

class Dog:
    def __init__(self,name,age,weight):
        self.name = name 
        self.age = age
        self.weight = weight

    def bark(self):
        print(" barks")
    
    def run_speed(self):
        return self.weight/self.age*10
    
    def fight(self,other_dog):
        
        first_dog = self.run_speed()
        second_dog = other_dog.run_speed()
        

        if first_dog > second_dog:
            print(f"First dog wins")
        elif first_dog < second_dog:
            print(f"Second dog wins")
        else:
            print("Both dogs win")

class PetDog(Dog):
    dog_names = []
    def __init__(self,name):
        self.trained = False
        self.name = name


    def train(self):
        self.bark()
        self.trained = True

    def play(self):
        self.trained = False
        PetDog.dog_names.append(self.name)
        dog_names_str = ",".join(PetDog.dog_names)
        print(f"the dogs: {dog_names_str} play together ")

        
    # def play(*args):
        
    #     PetDog.dog_names.append(args)
    #     dog_names_str = ",".join(PetDog.dog_names)
    #     print(f"the dogs: {dog_names_str} play together ")


dog1 = PetDog("Harry")
dog2 = PetDog("Dougi")

dog1.play()
dog2.play()

print(PetDog.dog_names)



