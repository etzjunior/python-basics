import string

string.ascii_uppercase
string.ascii_lowercase
string.punctuation
string.digits

while True:
    try:
        num1 = float(input("Enter number: "))
        break
    except ValueError:
        print("Wrong input. Enter number")

while True:

    print("Select Operator: ")
    print("Addition(+)")
    print("Subtraction(-)")
    print("Division(/)")
    print("Multiplication(*)")
    while True:
            Choice = input("Enter Operator: ")
            if Choice in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid operator! Please enter +, -, *, or /")
    
    while True:
        try:
            num2 = float(input("Enter another number: "))
            break
        except ValueError:
            print("Wrong input. Enter another number")


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