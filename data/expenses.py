import pandas as pd
import os


EXPENSE_FILE = "data/expenses.csv"


def load_expenses():

    if os.path.exists(EXPENSE_FILE):

        try:
            df = pd.read_csv(EXPENSE_FILE)

            expenses = dict(
                zip(df["Category"], df["Actual"])
            )

            return expenses

        except Exception:
            print("Could not load expense file.")

    return {}


def add_expenses():

    expenses = {}

    print("\nEnter your actual spending.")
    print("Type 'done' when finished.")

    while True:

        category = input("\nEnter category: ")

        if category.lower() == "done":
            break

        if category == "":
            print("Category cannot be empty.")
            continue

        try:

            amount = float(input("Enter actual spending: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount

        except ValueError:
            print("Please enter a valid number.")

    return expenses


def save_expenses(expenses):

    data = []

    for category, amount in expenses.items():

        data.append({
            "Category": category,
            "Actual": amount
        })

    df = pd.DataFrame(data)

    df.to_csv(EXPENSE_FILE, index=False)

    print("Expenses saved successfully!")