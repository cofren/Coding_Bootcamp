import string
import random
"""
# Exercise 1
list1 = [1, 2, 3, 4]
list2 = [6, 7, 8, 9]
list1.extend(list2)
print(list1)


# Exercise 2
list = []
for i in range(1, 4):
  number = input("Please enter a number:")
  list.append(int(number))
print(list)
print(f"The max number is {max(list)}")


# Exercise 3
letter_string = string.ascii_lowercase
for letter in letter_string:
  if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f"{letter} is a vowel")
  else:
    print(f"{letter} is a consonant")


#Exercise 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input("What´s your name?")
if user in names:
  print(names.index(user))
else:
  print("not in")


#Exercise 5
words = []
while len(words) < 7:
  word = input("Please enter a word:")
  words.append(word)
print(words)

letter = input("Please enter 1 single Character:")

print(letter)

for word in words:
    position = word.find(letter)
    if position != -1:
        print(f"Your Character is in position {position} of the word {word}")
    else:
        print(f"The letter {letter} is not in the word {word}")  


# Exercise 6
numbers = []
for number in range(1,1000001):
    numbers.append(number)

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# Exercise 7
string = input("Please enter some numbers, separated by comma:")
new_list = string.split(",")
new_tuple = tuple(new_list)
print(new_list)
print(new_tuple)


# Exercise 8
user_number = ""
random_number = random.randint(1,9)
guess_counter = 0
guess_success = 0
guess_or_not = True
print(random_number)
user_number = int(input("Please enter a number between 1 and 9:"))

while guess_or_not:
    guess_counter += 1
    if user_number == random_number:
        guess_success += 1
        guess_counter += 1
        print("You guessed correct!")
        play_again = input("Want to play again? Enter \"y\\n\"")
        if play_again != "y":
            break
        else:
            user_number = int(input("Enter a number between 1 and 9:"))
            guess_or_not = True
       
    else:
        guess_counter += guess_counter
        play_again = input("Number was wrong. Want to play again? Enter \"y\\n\"")
        if play_again != "y":
            break
        else:
            user_number = int(input("Enter a number between 1 and 9:"))
            guess_or_not = True
        
print(f"You guessed {guess_success} time(s) correct out of a total of {guess_counter} guesses")
"""


# Exercise 9
user_info = {
  "customer_name": "",
  "waiter": "",
  "item": "",
  "price": "",
  "qty": "",
  "discount": ""
}

user_info["customer_name"] = input("Whats your name?\n")
user_info["waiter"] = input("Who was your waiter?\n")
user_info["item"] = input("What did you order \n")
user_info["price"] = input("What was the price? \n")
user_info["qty"] = input("How many did you have?\n")
user_info["discount"] = input("How much discount did you get?\n")

total_charge = int(user_info["price"]) * int(user_info["qty"])

print(f"The total charge excluding VAT is ${total_charge}.\n Including VAT is ${total_charge * 1.16}. You had: \n blablabla ")
print(user_info)



# while guess_or_not == True:
#     if user_number == random_number:
#         print("Congrats you guessed the right number!")
#         guess_counter += 1
#         break
#     else:
#         guess_or_not = input("Sorry, not the right number. If you want to guess again, please enter a number between 1 and 9. If you want to stop, please enter \"done\".")

#  print(f"You guessed {guess_counter} times until you hit the right number!")   




# letter = "g"
# word = "dfsgdfsd"
# position = word.index(letter)
# print(position)


# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)
