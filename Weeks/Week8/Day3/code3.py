# Fruit
# Attributes:
# -name(str)
# -price (int)

# Cart:
#Attributes:
# - Size (int)
# content (list of fruits) --> initilaized as []

# Methods:
# - add_fruit(self,fruit) --> adds the fruit to the content list


class Fruit:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        

class Cart:
    def __init__(self,size):
        self.size=size
        self.content=[]

    def add_fruit(self,fruit)
        self.content.append(fruit)




    

