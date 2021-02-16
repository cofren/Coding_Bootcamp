"""
# Exercise 1
def display_message():
    print("Functions")

display_message()

# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Python for beginners")



# Exercise 3:
def describe_city(city="Amsterdam",country="Netherlands"):
    print(city + " is in " + country)

describe_city("Berlin","Germany")
describe_city("New York","USA")
describe_city("Paris","France")
describe_city()



# Exercise 4
import random
rand = random.randrange(1,101)
print(rand)

def rand_user(num):
    if rand == num:
        return True

user_number = input("Please enter a number")
if rand_user(user_number):
    print("You guessed correctly!")
else: print("Wrong guess. You thought it is " + str(user_number) + ", but it was " + str(rand))



#Exercise 5

def make_shirt(size="L",text="I love Python"):
    print("Size of shirt is " + size + ". The text is " + text +".")

make_shirt("L","Super-Duper-T-Shirt")
make_shirt(text="Great Shirt", size="XL")
make_shirt()
make_shirt("M")
make_shirt("S","New Shirt Text")

"""
# Exercise 6
magicians = ["Merlin","David","Houdini"]

def show_magicians(names):
    for name in names:
        print(name)
show_magicians(magicians)

def make_great(magicians):
    great_magician=[]
    for name in magicians:
        name += " the Great"
        great_magician.append(name)
    return ", ".join(great_magician)

print(make_great(magicians))
