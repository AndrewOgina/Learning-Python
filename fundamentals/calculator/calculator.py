import math

# A custom error
class InvalidOperation(Exception):
    "Please enter a valid operation!"
    pass

# This is a basic calculator program to help me get through with the basics of coding.
def add(num1:int,num2:int)->int:
    """Adds two numbers together"""
    summed:int = num1 + num2
    print(f"Answer:{summed}")
    
    return summed

def subtract(num1:int,num2:int)->int:
    """Subtracts two numbers"""
    subtracted = num1-num2
    print("Answer:",subtracted)
    
    return subtracted

def multiply(num1:int,num2:int)->int:
    """Multiplys the two numbers together"""
    multiplied = num1*num2
    print("Answer:",multiplied)
    
    return multiplied

def divide(num1:int,num2:int)->int:
    """Divides the two numbers"""
    
    try:
        divided = num1/num2
        print("Answer:",divided)
        return divided
    except ZeroDivisionError:
        print("You cannot divide a number by zero")
    finally:
        return None

def main():
    username = input("What is your name: ")
    print(f"Welcome {username} to the Calculator!")
    print("The answers you seek lies ahead!")
    print("ADD / SUBTRACT / MULTIPLY / DIVIDE")
    
    
    while 1 == 1:
        try:
            operation = input("SELECT ONE:")
            operation = operation.upper()
            if operation == "ADD" or operation == "SUBTRACT" or operation == "MULTIPLY" or operation == "DIVIDE":
                pass
            else:
                raise InvalidOperation
            num1 = int(input("First number:"))
            num2 = int(input("Second number:"))
            break
        except InvalidOperation:
            print("Please enter a valid operation!")
        except TypeError:
            print("Please Provide an integer!")
    
    if(operation == "ADD"):
        added = add(num1,num2)
    elif operation == "SUBTRACT":
        subtracted = subtract(num1,num2)
    elif operation == "MULTIPLY":
        multiplied = multiply(num1,num2)
    elif operation == "DIVIDE":
        divided = divide(num1,num2)
    else:
        raise InvalidOperation
    
    return None

main()