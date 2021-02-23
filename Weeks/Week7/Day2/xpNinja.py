# Exercise 1
list_of_strings = []

def box_printer(strings):
    list_of_strings = string_to_list(strings)
    longest_word = longest_string(list_of_strings)
    stars_print = "".join(stars_top_bottom(longest_word))
    add_spaces(longest_word,list_of_strings)
    print(list_of_strings)
    print(longest_word)
    print(stars_print)
    for rows in add_spaces:
        print(string_row)
    

def string_to_list(strings):
    list_of_strings = strings.split(",")
    return list_of_strings

def longest_string(list_of_strings):
    longest_string =""
    for string in list_of_strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

def stars_top_bottom(longest_word):
    stars = ["*","*","*","*"]
    for letter in longest_word:
        stars.append("*")
    return stars

def add_spaces(longest_word,list_of_string):
    for word in list_of_strings:
        letter_list = ["*"," "]
        for letter in word:
            letter_list.append(letter)
        letter_list.append(" ")
        letter_list.append("*")
        string_row = "".join(letter_list)
        return string_row


strings = input("Please input words, separated by comma:")

box_printer(strings)

# print(list_of_strings)


# print(longest_word)


# print(stars_print) 





