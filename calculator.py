def calculator():
    print("Welcome to the Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the calculation
        if operation == "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid operation. Please select +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
