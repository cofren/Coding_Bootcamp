class User:
    users = []
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        self.info = (self.name,self.age,self.score)
        User.users.append(self.info)

    # @classmethod
    # def sort_tuple(cls):
    #     for name,age,score in User.users:
    #         for name,age,score in User.users:
    #             print(name,age,score)
            
            


user_1 = User("Tom",19,80)
user_2 = User("John",20,90)
user_3 = User("Jony",17,91)
user_4 = User("Jony",17,93)
user_5 = User("Json",21,85)


print(User.users)
# User.sort_tuple()