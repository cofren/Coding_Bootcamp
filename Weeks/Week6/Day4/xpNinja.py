"""
# Exercise 1
import math

c = 50
h = 30
d = ""


your_numbers = input("Please input 3 numbers, separated by comma: \n")
numbers_list = your_numbers.split(",")
print(numbers_list)

q1 = math.sqrt((2*c*int(numbers_list[0]))/h)
q2 = math.sqrt((2*c*int(numbers_list[1]))/h)
q3 = math.sqrt((2*c*int(numbers_list[2]))/h)


print(int(q1),int(q2),int(q3))


# Exercise 2
list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
list4 =  [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
all_lists = [list1,list2,list3,list4]

print(sorted(list1, reverse=True))
print(sum(list1))
print(list1)
new_list = [list1[0],list1[-1]]
print(new_list)

over_50 = []
for number in list1:
  if number > 50:
    over_50.append(number)
print(over_50)

smaller_10 = []
for number in list1:
  if number < 10:
    smaller_10.append(number)
print(smaller_10)

squares = []
for number in list1:
  squares.append(number*number)
print(squares)

no_duplicates = []
for number in list1:
  if number not in no_duplicates:
    no_duplicates.append(number)
print(no_duplicates)

print(sum(list1)/len(list1))

print(max(list1))

print(min(list1))

sum = 0
for number in list1:
  sum += number
print(sum)

print(sum/len(list1))

largest = 0
for number in list1:
  if number > largest:
    largest = number
print(largest)

smallest = 1000000
for number in list1:
  if number < smallest:
    smallest = number
print(smallest)

list_from_user = []
for number in range(1,11):
  number = input("Please enter a number between -100 and 100:\n")
  list_from_user.append(number)
print(list_from_user)


# Exercise 3
text = "SPD-Kanzlerkandidat Olaf Scholz verzichtet nach SPIEGEL-Informationen im Wahlkampf auf ein sogenanntes Schattenkabinett. Normalerweise versammeln Kanzlerkandidaten in einem solchen Team Leute um sich, die später Kabinettsposten erhalten sollen."
sentences = text.count(".")
words = text.count(" ")
print(f"This text is {len(text)} characters long.")
print(f"The text has {sentences -1} sentence(s).")
print(f"The text has {words} words.")
"""

# Exercise 4

str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
list = str.split(" ")
print(list)
for item in list:
  print(f"{item}:{item.count(item)}")