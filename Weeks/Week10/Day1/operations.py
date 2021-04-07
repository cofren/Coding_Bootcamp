"""
Mathematical operation
All operations = 0 if result is negative

"""

#Addition

def add(n1,n2):
    result = n1 + n2
    if result < 0:
        return 0
    return result

#Subtraction

def sub(n1,n2):
    result = n1 - n2
    if result < 0:
        return 0
    return result

#Multiplication

def multi(n1,n2):
    result = n1 * n2
    if result < 0:
        return 0
    return result

#Division

def div(n1,n2):
    result = n1 / n2
    if result  < 0:
        return 0
    return result