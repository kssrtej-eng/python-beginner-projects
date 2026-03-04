import json
from datetime import datetime

FILENAME = "budget_data.json"

# Load existing data or start fresh
try:
    with open(FILENAME, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"income": [], "expenses": []}

def add_transaction(transaction_type):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    
    transaction = {"amount": amount, "category": category, "date": date}
    data[transaction_type].append(transaction)
    
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
    print(f"{transaction_type.capitalize()} added!\n")

def view_summary():
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Balance: {total_income - total_expenses}\n")

while True:
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_transaction("income")
    elif choice == "2":
        add_transaction("expenses")
    elif choice == "3":
        view_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice!\n")