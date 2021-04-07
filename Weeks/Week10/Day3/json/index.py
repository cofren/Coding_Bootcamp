import json

with open("file.json","r") as rf:
    family = json.load(rf)
    family["children"][0]["color"] = "blue"
    family["children"][1]["color"] = "black"

        

print_nicely = json.dumps(family, indent=2)
print(print_nicely)


# people = {
#     1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#     2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}
# }

# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
    
#     for key in p_info:
#         print(key + ':', p_info[key])