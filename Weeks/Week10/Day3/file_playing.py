# with open ("test.txt","r") as rf:
#     for line in rf:
#         print(rf.readline())


# with open ("test.txt","r") as rf:
#     line_to_print = 5
#     for index, line in enumerate(rf,start=1):
#             if index == 5:
#                 print(index,line)


# with open("test.txt","r") as rf:
#     print(rf.read(5))
  
# with open("test.txt","r") as rf:
#     str_list = rf.readlines()
#     str_str = "".join(str_list)
#     print(str_str)
   

# with open("test.txt","r") as rf:
#     str_list = rf.readlines()
#     print(str_list.count("Lea\n"))

# with open("test.txt","r") as rf:
#     str_list = rf.readlines()
#     str_list.append("Amit")
#     print(str_list)


with open("test.txt","r") as rf:
    str_list = rf.readlines()
    for index, name in enumerate(str_list,0):
        if name == "Luke\n":
            str_list.insert(index,"SkyWalker")
        else:
            break
    print(str_list)
