import pandas as pd
import os


EXPENSE_FILE = "data/expenses.csv"


def load_expenses():

    if os.path.exists(EXPENSE_FILE):

        try:
            df = pd.read_csv(EXPENSE_FILE)

            expenses = {}

            for _, row in df.iterrows():

                month = str(row["Month"])
                category = str(row["Category"])
                amount = float(row["Actual"])

                key = (month, category)

                if key in expenses:
                    expenses[key] += amount
                else:
                    expenses[key] = amount

            return expenses

        except Exception:
            print("Could not load expense file.")

    return {}


def add_expenses():

    expenses = {}

    print("\nEnter your actual spending.")
    print("Type 'done' when finished.")

    while True:

        month = input("\nEnter month: ")

        if month.lower() == "done":
            break

        if month == "":
            print("Month cannot be empty.")
            continue

        category = input("Enter category: ")

        if category == "":
            print("Category cannot be empty.")
            continue

        try:

            amount = float(
                input("Enter actual spending: ")
            )

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            key = (month, category)

            if key in expenses:
                expenses[key] += amount
            else:
                expenses[key] = amount

        except ValueError:

            print("Please enter a valid number.")

    return expenses


def save_expenses(expenses):

    data = []

    for (month, category), amount in expenses.items():

        data.append({
            "Month": month,
            "Category": category,
            "Actual": amount
        })

    df = pd.DataFrame(data)

    df.to_csv(
        EXPENSE_FILE,
        index=False
    )

    print("Expenses saved successfully!")