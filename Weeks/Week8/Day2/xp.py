# #Exercise 1
# class cat:
    
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
        
    
#     def list_cats(self):
#         all_cats.update({self.name: self.age})
#         print(all_cats)

    

# cat1 = cat("Harry",1)
# cat2 = cat("Sally",2)
# cat3 = cat("Dairy",3)
# cat1.list_cats()
# cat2.list_cats()
# cat3.list_cats()


# #Exercise 2
# class Dog:
#     def __init__(self,name,height):
#         self.name = name 
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes woof")

#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm heigh!")


# davids_dog = Dog("Rex",50)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup",20)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print("David´s dog is bigger")
# elif davids_dog.height < sarahs_dog.height:
#     print("Sarahs´s dog is bigger")
# else:
#     print("Both dogs are equally heigh")

# #Exercise 3
# class Song:
#     def __init__(self,lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song (self):
#         for i in self.lyrics:
#            print(self.lyrics[i])

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

#Exercise 4
class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(self.animals)
    
    def sort_animals(self):
        self.animals.sort()
        print(self.animals)


the_zoo = Zoo("Wonder-Zoo")
the_zoo.add_animal("Cat")
the_zoo.add_animal("Duck")
the_zoo.add_animal("Eel")
the_zoo.add_animal("Bear")
the_zoo.add_animal("Ape")
the_zoo.add_animal("Cougar")
the_zoo.add_animal("Baboon")
the_zoo.add_animal("Emu")
the_zoo.get_animals()
the_zoo.sell_animal("Duck")
the_zoo.sort_animals()