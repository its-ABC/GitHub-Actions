import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(x)

def power(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        raise ValueError("Cannot compute the factorial of a negative number.")
    return math.factorial(int(x))

def log(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm base must be greater than zero.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be greater than zero and not equal to one.")
    return math.log(x, base)

def main():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. Logarithm")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '6', '7', '8']:
            try:
                num1 = float(input("Enter first number: "))
                if choice in ['1', '2', '3', '4', '6', '7']:
                    num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"The result is: {divide(num1, num2)}")
                    except ValueError as e:
                        print(e)
                elif choice == '6':
                    print(f"The result is: {power(num1, num2)}")
                elif choice == '7':
                    try:
                        print(f"The result is: {factorial(num1)}")
                    except ValueError as e:
                        print(e)
                elif choice == '8':
                    base = float(input("Enter base for logarithm: "))
                    try:
                        print(f"The result is: {log(num1, base)}")
                    except ValueError as e:
                        print(e)
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == '5':
            try:
                num = float(input("Enter number: "))
                print(f"The result is: {square_root(num)}")
            except ValueError as e:
                print(f"Invalid input: {e}")

        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()


