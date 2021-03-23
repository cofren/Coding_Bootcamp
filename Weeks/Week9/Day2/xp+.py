#Exercise 4
class Family:
    members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,"power":"Rolling his Eyes","incredible_name": "Eye-Roller"}
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,"power":"Rolling his Arms","incredible_name": "Arm-Roller"}
        ]
    last_name = ""

    def born(self,name,gender):
        self.name = name
        self.gender = gender
        Family.members.append({"name": self.name,"age": 0,"gender": self.gender,"is_child":True})
        print("Congrats, no more sleep for you!")
    
    @classmethod
    def is_old(cls):
        name_18 = input("Please enter a name for the 18+ check:")
        for person in Family.members:          
            for k,v in person.items():
                if person["name"] == name_18 and person["age"] > 18:
                    print("yes")

    @classmethod
    def whole_family(cls):
        for person in Family.members:
            print("The name is", person["name"], "the age is", person["age"])

class TheIncredibles(Family):

                

                
            
            
            

child1 = Family()
child1.born("Hans","Male")
# print(Family.members)
Family.is_old()
Family.whole_family()


