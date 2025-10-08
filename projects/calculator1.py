import string

string.ascii_uppercase
string.ascii_lowercase
string.punctuation
string.digits

num1 = float(input("Enter number: "))

print("Select Operator: ")
print("Addition(+)")
print("Subtraction(-)")
print("Division(/)")
print("Multiplication(*)")

Choice = input("Enter number: ")

num2 = float(input("Enter another number: "))

    
def calculate(num1, Choice, num2):
    if Choice == '+':
        return num1 + num2 
    elif Choice == '-':
        return num1 - num2
    elif Choice == '/':
        return num1 / num2
    elif Choice == '*':
        return num1 * num2
    else:
        return "Invalid Input"

result = calculate(num1, Choice, num2)
print("Result: ", result)