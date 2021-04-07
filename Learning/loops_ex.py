# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

# Python conditional statements and loops [44 exercises with solution]
# [An editor is available at the bottom of the page to write and execute the scripts.]

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). Go to the editor
# Click me to see the sample solution

# def divisible():
#     number_list = []
#     for number in range(1500,2701):
#         if number % 7 == 0 and number % 5 == 0:
#             number_list.append(str(number))
#     string = ",".join(number_list)
#     print(string)

# divisible()

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
# Click me to see the sample solution

# def convert():
#     celsius = input("Enter Celsius:")
#     fahrenheit = int(celsius)/5
#     print(fahrenheit)

# convert()


# 3. Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
# Click me to see the sample solution

# import random

# def guess():
#     r_num = random.randint(1,10)
#     print(r_num)
#     user_guess = int(input("Please guess between 1 and 10:"))
#     while r_num != user_guess:
#         user_guess = int(input("Please guess between 1 and 10:"))

# guess()



# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
# Click me to see the sample solution

# def loop(max_stars):
#     n=max_stars
#     for row in range(0,n):
#         for stars in range(row):
#             print("*", end=" ")
#         print()

#     for row in range(n,0,-1):
#         for stars in range(0,row):
#             print("*", end=" ")
#         print()


# def loop():
#     for i in [0,1,2]:
#         for j in range(i):
#             print(i,j)
             


# loop()


# 5. Write a Python program that accepts a word from the user and reverse it. Go to the editor
# Click me to see the sample solution

# def rev_word():
#     word = input("Please enter a word:")
#     print(word)
#     length_word=len(word)
#     print(length_word)
#     for letter in range(len(word) -1,-1,-1):
#         print(word[letter], end="")
#     print("ha")


# rev_word()

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
# Click me to see the sample solution

# def count():
#     numbers = (1,2,3,4,5,6,7,8,9)
#     even_numbers = []
#     odd_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     even = len(even_numbers)
#     print(even)
#     odd = len(odd_numbers)
#     print(odd)

# count()

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# Click me to see the sample solution

# def print_list():
#     datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
#     for item in datalist:
#         print(item)
#         print(type(item))

# print_list()

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# Click me to see the sample solution

# def cont():
#     for item in range(7):
#         if item == 3 or item == 6:
#             continue
#         print(item, end="")
#     print("\n")

# cont()


# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
# Click me to see the sample solution

# def fibo():
    
#     x=0
#     y=1
#     while y<50:
#         print(y)
#         x=y
#         y=x+y

# fibo()




# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
# Click me to see the sample solution

# def fizz():
#     for integer in range(1,51):
#         if integer % 3 == 0 and integer % 5 == 0:
#             print("FizzBuzz")
#         elif integer % 3 == 0:
#             print("Fizz")
#         elif integer % 5 == 0:
#             print("Buzz")
#         else:
#             print(integer)
# fizz()

# 11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Go to the editor
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
# Click me to see the sample solution

# def array():
#     row_num = int(input("Input number of rows: "))
#     col_num = int(input("Input number of columns: "))
#     multi_list = [
#         [0 for col in range(col_num)] for row in range(row_num)
#         ]
#     print(multi_list)
#     for row in range(row_num):
#         for col in range(col_num):
#          multi_list[row][col]= row*col

#     print(multi_list)

# array()


# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case). Go to the editor
# Click me to see the sample solution

# def lines():
#     all_lines = []
#     line = True
#     while line:
#         user_input = input("Please enter a line. When done hit space:")
#         if user_input == " ":
#             line = False
#         else:
#             all_lines.append(user_input)
#     print("".join(all_lines))

# lines()

# 13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
# Click me to see the sample solution

# def div5():
#     user_string = input("Please enter 4 digit sequence, separated by comma:")
#     print(user_string)
#     user_list = user_string.split(",")
#     print(user_list)
#     result = []
#     for number in user_list:
#         integer = int(number)
#         if integer % 5 == 0:
#             integer = str(integer)
#             result.append(integer)
#     string_result = ",".join(result)
#     print(result)
#     print(string_result)

# div5()

# 14. Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

# Click me to see the sample solution



# 15. Write a Python program to check the validity of password input by users. Go to the editor
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Click me to see the sample solution

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence. Go to the editor
# Click me to see the sample solution

# def even():
#     items = []
        # for i in range(100, 401):
        #     s = str(i)
        #     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        #         items.append(s)
        # print( ",".join(items))

# even()

# 17. Write a Python program to print alphabet pattern 'A'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *
# Click me to see the sample solution

# def pattern():
#     result =""
#     for row in range(0,7):
#         for column in range(0,7):
#             if (row == 0 and 2 <= column < 5) or (row == 3 and (column != 0 or column != 6)) or ((row != 0 or row != 3) and (column == 1 or column == 5)):
#                 result += "*"
#             else:
#                 result += " "
#         result += "\n"
#     print(result)
# pattern()

# def pattern():
#     result = ""
#     for row in range(0,7):
#         for column in range(0,7):
#             if (row == 0 or row == 6) and (column == 1 or column <=4):
#                 result += "*"
#             else:
#                 result += " "
#         result += "\n"
#     print(result)


# pattern()

# 18. Write a Python program to print alphabet pattern 'D'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 
# Click me to see the sample solution

# 19. Write a Python program to print alphabet pattern 'E'. Go to the editor
# Expected Output:

#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****
# Click me to see the sample solution

# 20. Write a Python program to print alphabet pattern 'G'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
# Click me to see the sample solution

# 21. Write a Python program to print alphabet pattern 'L'. Go to the editor
# Expected Output:

#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****
# Click me to see the sample solution

# 22. Write a Python program to print alphabet pattern 'M'. Go to the editor
# Expected Output:

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *
# Click me to see the sample solution

# 23. Write a Python program to print alphabet pattern 'O'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
# Click me to see the sample solution

# 24. Write a Python program to print alphabet pattern 'P'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *  
# Click me to see the sample solution

# 25. Write a Python program to print alphabet pattern 'R'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *
# Click me to see the sample solution

# 26. Write a Python program to print the following patterns. Go to the editor
# Expected Output:

#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
 
#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 
# Click me to see the sample solution

# 27. Write a Python program to print alphabet pattern 'T'. Go to the editor
# Expected Output:
#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  
# Click me to see the sample solution

# 28. Write a Python program to print alphabet pattern 'U'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
# Click me to see the sample solution

# 29. Write a Python program to print alphabet pattern 'X'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *
# Click me to see the sample solution

# 30. Write a Python program to print alphabet pattern 'Z'. Go to the editor
# Expected Output:

# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******
# Click me to see the sample solution

# 31. Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73
# Click me to see the sample solution

# 32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.
# Click me to see the sample solution

# 33. Write a Python program to convert month name to a number of days. Go to the editor
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 
# Click me to see the sample solution

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor

# Click me to see the sample solution

# 35. Write a Python program to check a string represent an integer or not. Go to the editor
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.  
# Click me to see the sample solution

# 36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  
# Click me to see the sample solution

# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day. Go to the editor
# Expected Output:

# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn  
# Click me to see the sample solution

# 38. Write a Python program to display astrological sign for given date of birth. Go to the editor
# Expected Output:

# Input birthday: 15                                                      
# Input month of birth (e.g. march, july etc): may                        
# Your Astrological sign is : Taurus 
# Click me to see the sample solution

# 39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born. Go to the editor
# Expected Output:

# Input your birth year: 1973                                             
# Your Zodiac sign : Ox  
# Click me to see the sample solution

# 40. Write a Python program to find the median of three values. Go to the editor
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   
# Click me to see the sample solution

# 41. Write a Python program to get next day of a given date. Go to the editor
# Expected Output:

# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24   
# Click me to see the sample solution

# 42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish. Go to the editor

# Click me to see the sample solution

# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number. Go to the editor
# Expected Output:

# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60 
# Click me to see the sample solution

# 44. Write a Python program to construct the following pattern, using a nested loop number. Go to the editor
# Expected Output:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# Click me to see the sample solution


# def numbers():
#     i = 0
#     while i < 11:
#         print(i)
#         i += 1
# numbers()

# def pattern():
#     for i in range(3,6):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         print("")
# pattern()

# def number_sum():
#     sum_number = 0
#     user_number = int(input("Please enter a number:"))
#     for i in range(0,user_number+1):
#         sum_number += i
#     print(sum_number)
# number_sum()

# def multi_table():
#     number = int(input("Please enter a number:"))
#     for i in range(1,11):
#         print(number * i)

# multi_table()

# def iterate():
#     list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#     div5 = []
#     for i in list1:
#         if i > 150:
#             break
#         elif i % 5 == 0:
#             div5.append(i)
#     print(div5)
# iterate()


# iterate()

# def pattern():
#     for i in range(5,0,-1):
#         for j in range(i,0,-1):
#             print(j, end="")
#         print("")

# pattern()

# def pattern():
#     # list1 = [10, 20, 30, 40, 50]
#     # list1.reverse()
#     # for i in list1:
#     #     print(i)

#     list1 = [10, 20, 30, 40, 50]
#     for i in range(len(list1)-1,-1,-1):
#         print(list1[i])


# pattern()

# def pattern():
#     for i in range(-10,0,1):
#         print(i)

# pattern()

# def pattern():
#     i=0
#     while i < 5:
#         print(i)
#         i += 1
#     print("done")


# pattern()

# def prime():
#     for i in range(25,51):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# prime()


# def factorial():
#     user_input = int(input("Enter factorial:"))
#     i = user_input
#     mult_sum = 1
#     while i > 0:
#         mult_sum *= i
#         i -= 1
#     print(mult_sum)

# factorial()    

# def reverse():
#     number = input("Input a number:")
#     len_number = len(number)
#     new_number = ""
#     print(len_number)
#     for i in range(len_number,0,-1):
#         new_number += str(i)
#     print(new_number)

# reverse()

# def index_position():
#     my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     result = []
#     for i in range(0,len(my_list)):
#         if i > 0 and (i+1) % 2 == 0:
#             print(f"i is {i}")
#             print(my_list[i])
#             result.append(my_list[i])
#         else:
#             print(f"i is {i}")
#             print(f"{my_list[i]} is not part of the new list")
#     print(result)

# def index_position():
#     my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     result = []
#     for i in range(5,len(my_list)):
#             print(f"i is {i}")
#             print(my_list[i])
#             result.append(my_list[i])
        
#     print(result)

# # index_position()

# def cube():
#     input_number = int(input("Please input a number:"))
#     for i in range(1,input_number+1,1):
#         cube_number = i * i * i
#         print(f"Current number is {i}, cube_number is: {cube_number}")
# cube()

# def sum_terms():
#     number_of_terms = 5
#     start = 2
#     new_number = start
#     sum = 0
#     for i in range(0,number_of_terms,1):
#         print(new_number, end=" ")
#         sum += new_number
#         new_number = new_number * 10 +2
#     print(sum)
# sum_terms()

# def pattern():
#     pattern_rows = int(input("How many rows?:"))
#     for i in range(1,pattern_rows+1,1):
#         for j in range(0,i):
#             print("*", end="")
#         print("")
#     for i in range(pattern_rows+1,1,-1):
#         for j in range(0,i):
#             print("*", end="")
#         print("")

# pattern()

def for_loop():
    list_x = ["A","B","C"]
    for i in ["A","B","C"]:
        print(i)
    for i in range(0,len(list_x)):
        print(list_x[i])

    

for_loop()