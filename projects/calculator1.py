import string

string.ascii_uppercase
string.ascii_lowercase
string.punctuation
string.digits

num1 = float(input("Enter number: "))

while True:

    print("Select Operator: ")
    print("Addition(+)")
    print("Subtraction(-)")
    print("Division(/)")
    print("Multiplication(*)")

    Choice = input("Enter Operator: ")
       

    num2 = float(input("Enter another number: "))


    def calculate(num1, Choice, num2):
        if Choice == '+':
            return num1 + num2 
        elif Choice == '-':
            return num1 - num2
        elif Choice == '/':
            if num2 == 0:
                return "Cannot divide by 0"
            return num1 / num2
        elif Choice == '*':
            return num1 * num2
        else:
            return "Invalid Input"

    result = calculate(num1, Choice, num2)
    print("Result: ", result)

    print("Do you want to continue calculating? (y/n)")
    choice = input("y/n: ")
    if choice == "y":
        num1 = result
    else:
        break