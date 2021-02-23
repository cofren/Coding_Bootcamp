# Exercise 1
import random
def get_random_temp(season):
    if season == "winter":
        temp = random.randrange(-10,-1)
    elif season == "fall":
        temp = random.randrange(0,16)
    elif season == "spring":
        temp = random.randrange(17,23)
    elif season == "summer":
        temp = random.randrange(24,40)
    else: print("You entered a non valid season")
    
    return temp

def main(user_season):
    temp = get_random_temp(user_season)
    print("The temperatur is " + str(temp) + " degrees Celsius")
    if temp < 0:
        print("Below 0")
    elif 0 <= temp <= 16:
        print("Between 0 and 16")
    else:
        print("Over 16")

user_season = input("Please input \"winter\" or \"spring\" or \"fall\" or \"summer\".")
main(user_season)