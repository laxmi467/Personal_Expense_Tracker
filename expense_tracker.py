print("===== Personal Expense Tracker =====")

expenses = []


# Function to add an expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Education/Other): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")


# Function to display all expenses
def display_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== Your Expenses =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']} - {expense['category']}")


# Function to calculate total expenses
def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses: ₹", total)


# Function to display category-wise expenses
def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== Category-wise Summary =====")

    if not summary:
        print("No expenses found.")
    else:
        for category, total in summary.items():
            print(f"{category}: ₹{total}")


# Function to delete an expense
def delete_expense():
    if not expenses:
        print("No expenses available to delete.")
        return

    display_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"{deleted['name']} deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category-wise Summary")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        display_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")