import json
import os

print("===== Personal Expense Tracker =====")

FILE_NAME = "expenses.json"


# Load previously saved expenses
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses. Starting with an empty list.")
    return []


# Save expenses permanently
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Load expenses when the program starts
expenses = load_expenses()


# Add an expense
def add_expense():
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nChoose a category:")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Education")
    print("5. Other")

    categories = {
        "1": "Food",
        "2": "Travel",
        "3": "Shopping",
        "4": "Education",
        "5": "Other"
    }

    category_choice = input("Enter category number: ")

    if category_choice not in categories:
        print("Invalid category choice.")
        return

    category = categories[category_choice]

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added and saved successfully!")


# Display all expenses
def display_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== Your Expenses =====")

    for i, expense in enumerate(expenses, start=1):
        category = expense.get("category", "Uncategorized")

        print(f"{i}. Name: {expense['name']}")
        print(f"   Amount: ₹{expense['amount']}")
        print(f"   Category: {category}")
        print("------------------------")


# Calculate total expenses
def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: ₹{total:.2f}")


# Display category-wise summary
def category_summary():
    if not expenses:
        print("No expenses available for summary.")
        return

    summary = {}

    for expense in expenses:
        category = expense.get("category", "Uncategorized")
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== Category-wise Summary =====")

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


# Delete an expense
def delete_expense():
    if not expenses:
        print("No expenses available to delete.")
        return

    display_expenses()

    try:
        number = int(input("Enter the expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses()

            print(f"'{deleted['name']}' deleted successfully!")
            print("Updated expenses saved permanently.")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid whole number.")


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