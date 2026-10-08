import matplotlib.pyplot as plt


def calculate_total_planned(budget):
    return sum(budget.values())


def calculate_total_actual(expenses):
    return sum(expenses.values())


def calculate_variance(planned, actual):
    return actual - planned


def get_status(planned, actual):

    variance = actual - planned

    if variance > 0:
        return "OVER BUDGET"

    elif variance < 0:
        return "UNDER BUDGET"

    else:
        return "ON BUDGET"


def get_budget_status(budget, expenses):

    results = []

    for category, planned in budget.items():

        actual = expenses.get(category, 0)

        variance = calculate_variance(
            planned,
            actual
        )

        status = get_status(
            planned,
            actual
        )

        results.append({
            "Category": category,
            "Planned": planned,
            "Actual": actual,
            "Variance": variance,
            "Status": status
        })

    return results


def get_over_budget_categories(budget, expenses):

    over_budget = []

    for category, planned in budget.items():

        actual = expenses.get(category, 0)

        if actual > planned:

            over_budget.append(category)

    return over_budget


def get_under_budget_categories(budget, expenses):

    under_budget = []

    for category, planned in budget.items():

        actual = expenses.get(category, 0)

        if actual < planned:

            under_budget.append(category)

    return under_budget


def planned_vs_actual_chart(budget, expenses):

    categories = list(budget.keys())

    planned = list(budget.values())

    actual = []

    for category in categories:

        actual.append(
            expenses.get(category, 0)
        )

    x = range(len(categories))


    plt.figure(figsize=(10, 6))


    plt.bar(
        [i - 0.2 for i in x],
        planned,
        width=0.4,
        label="Planned"
    )


    plt.bar(
        [i + 0.2 for i in x],
        actual,
        width=0.4,
        label="Actual"
    )


    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.title(
        "Planned vs Actual Spending"
    )


    plt.xticks(
        list(x),
        categories
    )


    plt.legend()

    plt.tight_layout()

    plt.show()


def spending_pie_chart(expenses):

    categories = list(expenses.keys())

    amounts = list(expenses.values())


    plt.figure(figsize=(8, 8))


    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )


    plt.title(
        "Spending by Category"
    )


    plt.tight_layout()

    plt.show()