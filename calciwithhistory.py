def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error: Division by zero"
    return x / y

operations = {
    '1': ("Add", add),
    '2': ("Subtract", subtract),
    '3': ("Multiply", multiply),
    '4': ("Divide", divide)
}

history = []

while True:
    print("\nChoose operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("5. View History")
    print("6. Quit")

    choice = input("Enter choice: ")
    
    if choice == '6':
        print("Exiting...")
        break
    elif choice == '5':
        print("\nCalculation History:")
        if history:
            for record in history:
                print(record)
        else:
            print("No history yet.")
        continue
    elif choice in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        result = operations[choice][1](num1, num2)
        print(f"Result: {result}")
        history.append(f"{num1} {operations[choice][0]} {num2} = {result}")
    else:
        print("Invalid choice. Try again.")
