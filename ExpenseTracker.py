import json
from datetime import datetime

EXPENSE_FILE = "expenses.json"

def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Add a new expense."""
    category = input("Enter the expense category (e.g., Food, Transport, Entertainment): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses():
    """View all recorded expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add a new expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
