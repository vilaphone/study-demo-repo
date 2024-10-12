# calculator.py 
# defining functions for operations
def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
 # put error in case divide by 0, and input strings
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

# Main Calculator Function 
def main():
    while True:
        print("Select operation:")
        print("1: Addition")
        print("2: Substraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {substract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} == {divide(num1, num2)}")
        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    main()   