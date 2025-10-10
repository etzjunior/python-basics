import string

# These imports are currently unused - could be removed or used for input validation
string.ascii_uppercase
string.ascii_lowercase
string.punctuation
string.digits

while True:
    # Outer session loop: restarting here gets a fresh num1 and clears prior state

    reset_loop = False  # Flag used to signal a user-triggered reset from inner loops

    # STEP 1: Get the first number from user
    while True:
        # Prompt for starting number; supports 'reset' and numeric validation
        try:
            num1_input = input("Enter number: ")
            # Check if user wants to reset the calculator
            if num1_input.lower() == "reset":
                print("Calculator reset!")
                reset_loop = True
                break
            # Convert string input to float for calculations
            num1 = float(num1_input)
            break
        except ValueError:
            # Handle non-numeric input gracefully
            print("Wrong input. Enter number")

    # Check if user requested reset during num1 input
    if reset_loop:
        # If user requested reset during num1 entry, restart the entire session
        continue

    # STEP 2: Main calculation loop - continues until user chooses to stop
    while True:
        # Main calculation loop: select operator, get num2, compute, and optionally chain

        # Display available operations to user
        print("Select Operator: ")
        print("Addition(+)")
        print("Subtraction(-)")
        print("Division(/)")
        print("Multiplication(*)")
        
        # STEP 2A: Get operator from user
        while True:
            # Operator selection; 'reset' returns to fresh num1
            Choice = input("Enter Operator: ")
            # Check if user wants to reset
            if Choice.lower() == "reset":
                print("Calculator reset!")
                reset_loop = True
                break
            # Validate operator is one of the supported operations
            elif Choice in ['+', '-', '*', '/']:
                break
            else:
                # Invalid operator - ask user to try again
                print("Invalid operator! Please enter +, -, *, or /")
        
        # Check if user requested reset during operator selection
        if reset_loop:
            # Exit calc loop so outer session loop can restart with fresh num1
            break
        
        # STEP 2B: Get second number from user
        while True:
            # Second operand input; supports 'reset' and numeric validation
            try:
                num2_input = input("Enter another number: ")
                # Check if user wants to reset
                if num2_input.lower() == "reset":
                    print("Calculator Reset!")
                    reset_loop = True
                    break
                # Convert string input to float for calculations
                num2 = float(num2_input)
                break
            except ValueError:
                # Handle non-numeric input gracefully
                print("Wrong input. Enter number again")
        
        # Check if user requested reset during num2 input
        if reset_loop:
            # Exit calc loop so outer session loop can restart with fresh num1
            break

        # STEP 2C: Perform the calculation
        def calculate(num1, Choice, num2):
            # Core arithmetic; returns a number or an error string for invalid operations
            if Choice == '+':
                return num1 + num2 
            elif Choice == '-':
                return num1 - num2
            elif Choice == '/':
                # Prevent division by zero error
                if num2 == 0:
                    return "Cannot divide by 0"
                return num1 / num2
            elif Choice == '*':
                return num1 * num2
            else:
                return "Invalid Input"

        # Execute the calculation and display result
        result = calculate(num1, Choice, num2)
        print("Result: ", result)

        # STEP 2D: Ask user if they want to continue with chained calculations
        print("Do you want to continue calculating? (y/n)")
        choice = input("y/n: ")
        if choice == "y":
            # Only chain calculations if result is a valid number
            if isinstance(result, (int, float)):
                # Use current result as num1 for next calculation
                num1 = result
            else:
                # Can't continue from error messages - restart session
                print("Cannot continue from an error result. Starting over.")
                break  # exit calc loop → restart session
        else:
            # User chose to stop - exit calculation loop
            break  # exit calc loop → end session

    # STEP 3: Handle session restart or program termination
    if reset_loop:
        # User requested reset - restart with fresh num1
        continue  # restart from fresh num1
    else:
        # User chose to end program - exit completely
        break  # end program