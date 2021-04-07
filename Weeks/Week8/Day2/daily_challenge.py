"""
Daily Challenge : Old MacDonald’s Farm
Look carefully at this code and output

File: market.py
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow',5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info())
Output

McDonald's farm

cow : 5
sheep : 2
goat : 12

    E-I-E-I-0!
Create the code that is needed to recreate the code above. Here are a few questions to help give you some direction:
1. Create a Farm class. How do we implement that?
2. Does the Farm class need an __init__ method? If so, what parameters should it take?
3. How many method does the Farm class need ?
4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
5. Test that your code works and gives the same results as the example above.
6. Bonus: line up the text nicely in columns like in the example using string formatting

Expand The Farm
Add a method to the Farm class called get_animal_types. It should return a sorted list of all the animal types (names) that the farm has in it. For the example above, the list should be: ['cow', 'goat', 'sheep']
Add another method to the Farm class called get_short_info. It should return a string like this: “McDonald’s farm has cows, goats and sheep.”
It should call the get_animal_types function.
How would we make sure each of the animal names printed has a comma after it aside from the one before last (has an and after) and the last(has a period after)?.
"""

class Farm:

    def __init__(self, farmer_name):

        self.farmer_name = farmer_name

        self.animals = {} # self.animals is not dynamic, it is set as an empty dictionary by default

    def add_animal(self, animal, count=1):

        if animal in self.animals.keys(): # This will check if <animal> appear as a key in self.animals
            # 1) The animal already exit in the farm, we just want to add some
            self.animals[animal] += count
        else:
            # 2) There is no such animal yet, we need to add it to the dict and set the count to <count>
            self.animals[animal] = count

    def get_info(self):
        msg = ""
        msg += f"{self.farmer_name}'s Farm" + "\n"
        msg += "\n"

        for animal, count in self.animals.items():
            msg += f"{animal}: {count}" + "\n"

        return msg


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())








# class Farm:
    
#     def __init__(self,farm_name):
#         print(f"{farm_name}'s Farm")
#         print("")
#         self.animal = ""
#         self.qty = 0
#         self.all_animals=[]
            

#     def add_animal(self,animal,qty=1):
#         self.animal = animal
#         self.qty = qty
#         self.all_animals.append(self.animal)
#         print(f"{self.animal}: {self.qty}")
        
        
#     def get_animal_types(self):
#         print(sorted(self.all_animals))

#     def get_short_info(self):
#         print("McDonald's farm has", ",".join(self.all_animals))
       
#     def get_info(self):
#         return print("E-I-E-I-O")

   

# macdonald = Farm("McDonald")
# macdonald.add_animal("cow",5)
# macdonald.add_animal("sheep")
# macdonald.add_animal("sheep")
# macdonald.add_animal("goat",12)
# print(macdonald.get_info())
# macdonald.get_animal_types()
# macdonald.get_short_info()



# # class Dog():
# #     Initializer / Instance Attributes
# #     def __init__(self, name_of_the_dog):
# #         print("A new dog has been initialized !")
# #         print("His name is", name_of_the_dog)
# #         self.name = name_of_the_dog

# #     def bark(self):
# #         print("{} barks ! WAF".format(self.name))

# # Dog1=Dog("Rex")
# # Dog1.bark()

