# main.py

import calculator

def get_numbers(operation):
    """Prompts the user for two numbers."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            if operation == "factorial":
                return num1, None  # Factorial requires only one number
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def main():
    """Runs the interactive calculator."""
    while True:
        calculator.calculator_menu()
        choice = input("Enter the operation number (1-8): ")

        if choice == '8':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4', '5', '6', '7'}:
            print("Invalid choice. Please select a valid operation.")
            continue

        if choice == '7':  # Factorial only needs one input
            num, _ = get_numbers("factorial")
            if num < 0 or not num.is_integer():
                print("Error! Factorial is only defined for non-negative integers.")
                continue
            print(f"Result: {calculator.factorial(int(num))}")
            continue

        num1, num2 = get_numbers("regular")

        if choice == '1':
            print(f"Result: {calculator.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {calculator.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {calculator.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {calculator.divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {calculator.power(num1, num2)}")
        elif choice == '6':
            print(f"Result: {calculator.modulus(num1, num2)}")

if __name__ == "__main__":
    main()
