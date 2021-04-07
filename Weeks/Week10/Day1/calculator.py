import operations

print("Welcome to our special calculator where no result is under 0")
print("Choose an operation:")
print("a) Add")
print("b) Substract")
print("c) Multiply")
print("d) Divide")

user_choice = input("> ") # a, b, c, or d

number1 = int(input("Please give me a number: "))
number2 = int(input("Please give me another number: "))

result = 0

# You need to display the result of the operation to the user (using the functions of the "operations.py" file)

if user_choice == "a":
    result = operations.add(number1, number2)
elif user_choice == "b":
    result = operations.sub(number1, number2)
elif user_choice == "b":
    result = operations.multi(number1, number2)
elif user_choice == "b":
    result = operations.div(number1, number2)

print(result)