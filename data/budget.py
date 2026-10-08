import pandas as pd
import os


BUDGET_FILE = "data/budget.csv"


def load_budget():

    if os.path.exists(BUDGET_FILE):

        try:
            df = pd.read_csv(BUDGET_FILE)

            budget = dict(
                zip(df["Category"], df["Planned"])
            )

            return budget

        except Exception:
            print("Could not load budget file.")

    return {}


def add_budget():

    budget = {}

    print("\nEnter your planned budget.")
    print("Type 'done' when finished.")

    while True:

        category = input("\nEnter category: ")

        if category.lower() == "done":
            break

        if category == "":
            print("Category cannot be empty.")
            continue

        try:

            amount = float(input("Enter planned amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            budget[category] = amount

        except ValueError:
            print("Please enter a valid number.")

    return budget


def save_budget(budget):

    data = []

    for category, amount in budget.items():

        data.append({
            "Category": category,
            "Planned": amount
        })

    df = pd.DataFrame(data)

    df.to_csv(BUDGET_FILE, index=False)

    print("Budget saved successfully!")