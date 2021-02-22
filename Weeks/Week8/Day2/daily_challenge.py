class Farm:
    
    def __init__(self,farm_name):
        print(f"{farm_name}'s Farm")
        print("")
        self.animal = ""
        self.qty = 0
        self.all_animals=[]
            

    def add_animal(self,animal,qty=1):
        self.animal = animal
        self.qty = qty
        self.all_animals.append(self.animal)
        print(f"{self.animal}: {self.qty}")
        
        
    def get_animal_types(self):
        print(sorted(self.all_animals))

    def get_short_info(self):
        print("McDonald's farm has", ",".join(self.all_animals))
       
    def get_info(self):
        return print("E-I-E-I-O")

   

macdonald = Farm("McDonald")
macdonald.add_animal("cow",5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat",12)
print(macdonald.get_info())
macdonald.get_animal_types()
macdonald.get_short_info()



# class Dog():
#     Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog

#     def bark(self):
#         print("{} barks ! WAF".format(self.name))

# Dog1=Dog("Rex")
# Dog1.bark()

