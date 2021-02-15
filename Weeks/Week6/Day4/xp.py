import string

# Exercise XP
# Exercise 1

my_fav_numbers = [8, 12, 9, 21]
print(my_fav_numbers)
my_fav_numbers.extend([33, 65])
print(my_fav_numbers)
my_fav_numbers.pop(-1)
print(my_fav_numbers)
friend_fav_numbers = [1, 2, 3, 8]
print(friend_fav_numbers)
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(sorted(our_fav_numbers))

# Exercise 2

# no a tuble is immutable

# Exercise 3

for number in range(1, 21):
    print(number)

# Exercise 4
# 1. A float is a number with decimals
# 2. by multiplacation/addition etc
number = 1.5
float_list = []
while number <= 5:
    float_list.append(number)
    number += 0.5
print(float_list)

# Exercise 5
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.pop(0)
print(basket)
basket.pop(-1)
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercise 6
my_name = "Amit"
while True:
  user_name = input("Whats your name?\n")
  if user_name == my_name:
    break

# Exercise 7
list = ["Hi", "Elephant", "Bread", "Car", "Vaccine"]
list = list[::2]
print(list)

# Exercise 8
number = 3
list = []
while number <= 30:
  list.append(number)
  number *= 3
print(list)

# Exercise 9
list = []
for number in range(1500, 2701):
  if number % 7 == 0 and (number*5) % 5 == 0:
    list.append(number)
print(list)

# Exercise 10
fruits = input("Please enter your favorite fruits separated by space\n")
print(fruits)
fruit_list = fruits.split(" ")
print(fruit_list)
while True:
  name_fruit = input("Please name 1 fruit:\n")
  if name_fruit in fruit_list:
    print("You chose one of your favorite fruits!")
    break
  else:
    print("You did not choose your favorite fruit, but enjoy!")
    break

# Exercise 11
all_toppings = []
while True:
  topping = input(
      "Please enter your topping. When you are done please enter \"quit\":")
  if topping == "quit":
    break
  print(f"{topping} has been added to your pizza")
  all_toppings.append(topping)
string = ", ".join(all_toppings)
price = 10 + len(all_toppings) * 2.5

print(
    f"Your pizza has the following topics: {string}. Your total price is {price}.")

# Exercise 12
age = ""
age_list = []
sum = 0
while True:
  age = input(
      "How old is the person that you want to buy a ticket for? When you´re done please type \"done\".\n")
  if age == "done":
    break
  age_list.append(int(age))

for age in age_list:
  if 3 >= int(age) <= 12:
    sum += 10
  elif int(age) > 12:
    sum += 15
print(f"You need to pay {sum}. Cash only, no \"Check Mesuman\"!")


# Exercise 14

menu = ["Add", "Remove", "View", "Exit"]
names = []
while True:
  to_do = input("Please choose \"Add\", \"Remove\", \"View\" or \"Exit\".")
  if to_do == "Exit":
    break
  elif to_do == "Add":
    name = input("Please enter a name:")
    names.append(name)
  elif to_do == "View":
    print(f"Here are all the names {names}.")
  elif to_do == "Remove":
    remove = input("Who do you want to remove?")
    names.remove(remove)
  else:
    print("Please enter a valid command!")
print(f"Here are all the names {names}.")


