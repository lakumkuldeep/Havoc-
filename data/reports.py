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


def display_budget(budget, expenses):

    print("\n")
    print("Budget Summary")
    print("------------------------------------------------------")
    print("Category       Planned       Actual        Status")
    print("------------------------------------------------------")

    for category, planned in budget.items():

        actual = expenses.get(category, 0)

        status = get_status(planned, actual)

        print(
            f"{category:<15}"
            f"{planned:<14.2f}"
            f"{actual:<14.2f}"
            f"{status}"
        )

    print("------------------------------------------------------")