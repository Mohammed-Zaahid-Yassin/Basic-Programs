# Basic Expense Tracker

expenses = []

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Quit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = input("Enter expense amount: ")
        try:
            amount = float(amount)
            expenses.append({"name": name, "amount": amount})
            print("Expense added!")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "2":
        if not expenses:
            print("No expenses logged.")
        else:
            print("\nExpense List:")
            for idx, expense in enumerate(expenses, 1):
                print(f"{idx}. {expense['name']}: ₹{expense['amount']:.2f}")
    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"\nTotal spending: ₹{total:.2f}")
    elif choice == "4":
        print("Goodbye! Track your spending wisely.")
        break
    else:
        print("Invalid option. Please try again.")
