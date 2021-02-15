"""
# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

both = zip(keys, values)
print(dict(both))


# Exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 
for age in family.values():
  if age >= 3:
    age = 12

print(list(family.values()))


# Exercise 3
brand = {
  "name": "Zara",
  "creation_date": 1975,
  "creator_name": "Amanico Ortegor Gaona",
  "type_of_clothes": ["men", "women, children, home"],
  "international_competitors": ["Gap, H&M, Benetton"],
  "number_stores": 7000,
  "major_color": {"France": "blue", "Spain": "red", "US": "pink, green"}

}

brand.update({"number_stores":2})
print(brand)

clients = ",".join(brand["type_of_clothes"])

print(f"The clients of Zara are {clients}")
"""

#Exercice 4

disney_a = {}
disney_b = {}
users = ["Mickey", "Minnie", "Donald","Ariel","Pluto"]
for index,user in enumerate(users):
  disney_a.update({user:index})
  disney_b.update({index:user})  
print(disney_a)
print(disney_b)

disney_c = {}
users_sorted = sorted(users) 
for index,user in enumerate(users_sorted):
  disney_c.update({user:index})
print(disney_c)

disney_i = {}
for index,user in enumerate(users):
  if "i" in user:
    disney_i.update({user:index})
print(disney_i)

disney_mp = {}
for index,user in enumerate(users):
  if user[0,1] == "m":
    disney_i.update({user:index})
print(disney_mp)