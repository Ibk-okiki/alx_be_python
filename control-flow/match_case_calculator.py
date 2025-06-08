# Simple Calculator with Match Case

def main():
    """
    Main function to run the calculator with match case statements.
    """
    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Get operation choice from user
    operation = input("Choose the operation (+, -, *, /): ")
    
    # Perform calculation using match case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
    main()
