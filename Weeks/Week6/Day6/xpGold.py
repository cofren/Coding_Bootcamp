"""
# Exercise 1
birthdays = {
  "hans": "1950/01/25",
  "fans": "1951/02/26",
  "gans": "1952/03/27",
  "rans": "1953/04/28",
  "dans": "1954/05/29",
}

bd_name = input("Hello, you can look up Birthdays here! Please enter the persons name here:\n")
found_name = False
for n,d in birthdays.items():
  if bd_name == n:
    print(n,d)
    found_name = True
    break

if found_name == False:
  print(f"Sorry, we don't know the birthday of {bd_name}")


# Exercise 2
for name in birthdays.keys():
  print(name)

# Exercise 3
user_name = input("What is your name?")
birthday = input("What´s your birthday?")

birthdays.update({user_name: birthday})
print(birthdays)


# Exercise 4

items = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

for item,price in items.items():
  print(f"{item} cost {price}")

only_items = items.keys()
print(only_items)

only_prices = list(items.values())
print(only_prices)

only_qty = [10,20,30,40]
print(only_qty)

prices_and_qty = list(zip(only_prices,only_qty))
print(prices_and_qty)

fruits_prices_qty = dict(zip(only_items,prices_and_qty))
print(fruits_prices_qty)
value = 0
for item,qty in fruits_prices_qty.values():
  value = item * qty + value
print(f"The total value is {value}")
"""

#Exercise 5
string = "Volkswagen,Toyota,Ford Motor,Honda,Chevrolet"
car_list = list(string.split(","))
print(car_list)
print(f" There are {len(car_list)} manufacturers in this list")
car_list.sort()
print(car_list)
car_list.reverse()
print(car_list)

cars_with_o = 0
for car in car_list:
  if "o" in car:
    cars_with_o += 1
print(f"{cars_with_o} have the letter \"o\" in their name")

cars_no_i = 0
for car in car_list:
  if not "i" in car:
    cars_no_i += 1
print(cars_no_i)

new_list = ["Honda","Volkswagen","Toyota","Ford Motor","Honda","Chevrolet","Toyota"]
no_duplicates = set(new_list)
print(no_duplicates)
string = ",".join(no_duplicates)
print(string)
no_cars = string.count(",")+1
print(f"There are {no_cars} companies in the list")
new_list = string.split(",")
print(new_list)
new_list.sort()
print(new_list)

for car in new_list:
  first_letter = car[0]
  last_letter = car[-1]
  middle = car[1:-2]
  new_name = last_letter+middle+first_letter
  print(new_name)



    
 
 
 
  

  
      
    



