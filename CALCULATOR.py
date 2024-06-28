#VAISHNAVI.K_PYTHON INTERNSHIP
#CALCULATOR_TASK2

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"
    else:
        return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("=================")
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        option = input("\nEnter option (1:2:3:4:5): ")

        if option == '1':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif option == '2':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif option == '3':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif option == '4':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
        elif option == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid data entered. Please select a valid operation.")

if __name__ == "__main__":
    main()

