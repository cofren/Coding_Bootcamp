# #Exercise 1
# from datetime import date
# print(date.today())

#Exercise 2
# from datetime import datetime,timedelta

# today = datetime.today()
# print(today)
# new_date = datetime(2022,1,1,0,0,1,1)
# print(new_date)
# time_to_new_date = new_date - today
# print("The", new_date.day, "st. of January is in", time_to_new_date.days,"days and",time_to_new_date.seconds/3600,"hours")

#Exercise 3

from datetime import datetime,timedelta

# b_date_input = input("Please enter your birthdate in the format yyyy-mm-dd:")
# b_date_list = b_date_input.split("-")
# print(b_date_list)
# b_date_result = datetime(int(b_date_list[0]),int(b_date_list[1]),int(b_date_list[2]))
# print(b_date_result)
# today = datetime.today()
# print(today)
# days_of_life = today - b_date_result
# print(days_of_life)
# minutes_of_life = days_of_life.total_seconds() / 60
# print(minutes_of_life)

# # Exercise 4
# from datetime import datetime
# print(f"Today is: {datetime.today().strftime('%Y-%m-%d')}. The next holiday is April 20, 2021")
# holiday = datetime(2021,4,20)
# print(holiday)
# time_to_holiday = holiday - datetime.today()
# print(time_to_holiday)
# help(datetime)

# Exercise 6

from faker import Faker


class User:
    users = []
    def __init__(self):
        self.info = Faker()
        self.name = self.info.name()
        self.address = self.info.address()
        self.language_code = "EN"
        User.users.append(self)
        print(self.name)
    
user_1 = User()
user_2 = User()
user_3 = User()
print(User.users)

