import tkinter as tk
from tkinter import messagebox

from budget import load_budget, save_budget
from expenses import load_expenses, save_expenses
from reports import (
    calculate_total_planned,
    calculate_total_actual,
    calculate_variance,
    get_status,
    get_over_budget_categories,
    get_under_budget_categories,
    planned_vs_actual_chart,
    spending_pie_chart
)


# ============================================================
# LOAD SAVED DATA
# ============================================================

budget = load_budget()
expenses = load_expenses()


# ============================================================
# MAIN WINDOW
# ============================================================

window = tk.Tk()

window.title("Personal Budget Tracker")
window.geometry("900x720")

window.configure(bg="white")

window.resizable(True, True)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    window,
    bg="white",
    height=80
)

header.pack(
    fill="x",
    padx=15,
    pady=(15, 10)
)

header.pack_propagate(False)


tk.Label(
    header,
    text="PERSONAL BUDGET TRACKER",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="black"
).pack(pady=20)


# ============================================================
# MAIN CONTENT
# ============================================================

content = tk.Frame(
    window,
    bg="white"
)

content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=5
)


# ============================================================
# INPUT SECTION
# ============================================================

input_frame = tk.LabelFrame(
    content,
    text="  ADD / UPDATE BUDGET & EXPENSE  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="black",
    padx=15,
    pady=12
)

input_frame.pack(
    fill="x",
    pady=5
)


# Month

tk.Label(
    input_frame,
    text="Month:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

month_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 10)
)

month_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Category

tk.Label(
    input_frame,
    text="Category:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=8,
    sticky="e"
)

category_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 10)
)

category_entry.grid(
    row=0,
    column=3,
    padx=10,
    pady=8
)


# Planned amount

tk.Label(
    input_frame,
    text="Planned Amount:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="e"
)

planned_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 10)
)

planned_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# Actual spending

tk.Label(
    input_frame,
    text="Actual Spending:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=1,
    column=2,
    padx=10,
    pady=8,
    sticky="e"
)

actual_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 10)
)

actual_entry.grid(
    row=1,
    column=3,
    padx=10,
    pady=8
)


# Add / Update button

tk.Button(
    input_frame,
    text="Add / Update Record",
    command=add_record if "add_record" in globals() else None,
    width=25,
    font=("Arial", 10, "bold")
).grid(
    row=2,
    column=1,
    columnspan=2,
    pady=10
)


# ============================================================
# GET MONTH EXPENSES
# ============================================================

def get_month_expenses(month):

    month_expenses = {}

    for (saved_month, category), amount in expenses.items():

        if saved_month.lower() == month.lower():

            if category in month_expenses:

                month_expenses[category] += amount

            else:

                month_expenses[category] = amount

    return month_expenses


# ============================================================
# ADD / UPDATE RECORD
# ============================================================

def add_record():

    month = month_entry.get().strip()
    category = category_entry.get().strip()

    planned_text = planned_entry.get().strip()
    actual_text = actual_entry.get().strip()


    if month == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a month."
        )

        return


    if category == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a category."
        )

        return


    try:

        planned = float(planned_text)
        actual = float(actual_text)

    except ValueError:

        messagebox.showerror(
            "Input Error",
            "Please enter valid numbers."
        )

        return


    if planned <= 0:

        messagebox.showerror(
            "Input Error",
            "Planned amount must be greater than 0."
        )

        return


    if actual < 0:

        messagebox.showerror(
            "Input Error",
            "Actual spending cannot be negative."
        )

        return


    budget[category] = planned

    expenses[(month, category)] = actual


    save_budget(budget)
    save_expenses(expenses)


    messagebox.showinfo(
        "Success",
        "Record saved successfully!"
    )


    month_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    planned_entry.delete(0, tk.END)
    actual_entry.delete(0, tk.END)


# ============================================================
# REPORT SECTION
# ============================================================

report_frame = tk.LabelFrame(
    content,
    text="  REPORTS & ANALYSIS  ",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="black",
    padx=15,
    pady=10
)

report_frame.pack(
    fill="both",
    expand=True,
    pady=5
)


# Report month

tk.Label(
    report_frame,
    text="Report Month:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8
)


report_month_entry = tk.Entry(
    report_frame,
    width=25,
    font=("Arial", 10)
)

report_month_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# Search category

tk.Label(
    report_frame,
    text="Search Category:",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="black"
).grid(
    row=0,
    column=2,
    padx=10,
    pady=8
)


search_entry = tk.Entry(
    report_frame,
    width=25,
    font=("Arial", 10)
)

search_entry.grid(
    row=0,
    column=3,
    padx=10,
    pady=8
)


# ============================================================
# SUMMARY BOX
# ============================================================

summary_text = tk.Text(
    report_frame,
    width=95,
    height=11,
    font=("Consolas", 10),
    bg="white",
    fg="black",
    relief="solid",
    borderwidth=1
)

summary_text.grid(
    row=1,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="nsew"
)


# ============================================================
# SHOW MONTHLY SUMMARY
# ============================================================

def display_summary():

    month = report_month_entry.get().strip()


    if month == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a report month."
        )

        return


    month_expenses = get_month_expenses(month)


    summary_text.delete(
        "1.0",
        tk.END
    )


    summary_text.insert(
        tk.END,
        f"MONTHLY SUMMARY: {month}\n"
    )

    summary_text.insert(
        tk.END,
        "=" * 75 + "\n\n"
    )


    summary_text.insert(
        tk.END,
        f"{'CATEGORY':<18}"
        f"{'PLANNED':<15}"
        f"{'ACTUAL':<15}"
        f"{'STATUS'}\n"
    )

    summary_text.insert(
        tk.END,
        "-" * 75 + "\n"
    )


    for category, planned in budget.items():

        actual = month_expenses.get(
            category,
            0
        )

        status = get_status(
            planned,
            actual
        )


        summary_text.insert(
            tk.END,
            f"{category:<18}"
            f"{planned:<15.2f}"
            f"{actual:<15.2f}"
            f"{status}\n"
        )


    total_planned = calculate_total_planned(
        budget
    )

    total_actual = calculate_total_actual(
        month_expenses
    )

    variance = calculate_variance(
        total_planned,
        total_actual
    )


    summary_text.insert(
        tk.END,
        "\n" + "-" * 75 + "\n"
    )

    summary_text.insert(
        tk.END,
        f"Total Planned : {total_planned:.2f}\n"
    )

    summary_text.insert(
        tk.END,
        f"Total Actual  : {total_actual:.2f}\n"
    )

    summary_text.insert(
        tk.END,
        f"Total Variance: {variance:.2f}\n"
    )


    over_budget = get_over_budget_categories(
        budget,
        month_expenses
    )

    under_budget = get_under_budget_categories(
        budget,
        month_expenses
    )


    summary_text.insert(
        tk.END,
        "\nOver-Budget Categories:\n"
    )


    if over_budget:

        for category in over_budget:

            summary_text.insert(
                tk.END,
                f"  - {category}\n"
            )

    else:

        summary_text.insert(
            tk.END,
            "  None\n"
        )


    summary_text.insert(
        tk.END,
        "\nUnder-Budget Categories:\n"
    )


    if under_budget:

        for category in under_budget:

            summary_text.insert(
                tk.END,
                f"  - {category}\n"
            )

    else:

        summary_text.insert(
            tk.END,
            "  None\n"
        )


# ============================================================
# SEARCH
# ============================================================

def search_category():

    search_text = search_entry.get().strip().lower()

    month = report_month_entry.get().strip()


    if month == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a report month."
        )

        return


    if search_text == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a category to search."
        )

        return


    month_expenses = get_month_expenses(month)


    summary_text.delete(
        "1.0",
        tk.END
    )


    found = False


    summary_text.insert(
        tk.END,
        f"SEARCH RESULTS FOR: {search_text}\n"
    )

    summary_text.insert(
        tk.END,
        "=" * 75 + "\n\n"
    )


    for category, planned in budget.items():

        if search_text in category.lower():

            actual = month_expenses.get(
                category,
                0
            )

            status = get_status(
                planned,
                actual
            )


            summary_text.insert(
                tk.END,
                f"Category : {category}\n"
                f"Planned  : {planned:.2f}\n"
                f"Actual   : {actual:.2f}\n"
                f"Status   : {status}\n\n"
            )


            found = True


    if not found:

        summary_text.insert(
            tk.END,
            "No matching category found."
        )


# ============================================================
# CLEAR SEARCH
# ============================================================

def clear_search():

    search_entry.delete(
        0,
        tk.END
    )

    display_summary()


# ============================================================
# CHART FUNCTIONS
# ============================================================

def show_bar_chart():

    month = report_month_entry.get().strip()


    if month == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a report month."
        )

        return


    month_expenses = get_month_expenses(month)


    planned_vs_actual_chart(
        budget,
        month_expenses
    )


def show_pie_chart():

    month = report_month_entry.get().strip()


    if month == "":

        messagebox.showerror(
            "Input Error",
            "Please enter a report month."
        )

        return


    month_expenses = get_month_expenses(month)


    if len(month_expenses) == 0:

        messagebox.showerror(
            "No Data",
            "No expenses found for this month."
        )

        return


    spending_pie_chart(
        month_expenses
    )


# ============================================================
# BUTTON AREA
# ============================================================

# Re-create the Add button command now that add_record exists
# The button above is replaced with a properly connected button.

for widget in input_frame.grid_slaves(row=2):

    widget.destroy()


tk.Button(
    input_frame,
    text="Add / Update Record",
    command=add_record,
    width=25,
    font=("Arial", 10, "bold")
).grid(
    row=2,
    column=1,
    columnspan=2,
    pady=10
)


button_frame = tk.Frame(
    report_frame,
    bg="white"
)

button_frame.grid(
    row=2,
    column=0,
    columnspan=4,
    pady=5
)


# Show Summary

tk.Button(
    button_frame,
    text="Show Monthly Summary",
    command=display_summary,
    width=24,
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


# Search

tk.Button(
    button_frame,
    text="Search",
    command=search_category,
    width=18,
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Clear Search

tk.Button(
    button_frame,
    text="Clear Search",
    command=clear_search,
    width=18,
    font=("Arial", 10, "bold")
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


# Planned vs Actual Chart

tk.Button(
    button_frame,
    text="Planned vs Actual Chart",
    command=show_bar_chart,
    width=24,
    font=("Arial", 10, "bold")
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


# Spending by Category

tk.Button(
    button_frame,
    text="Spending by Category",
    command=show_pie_chart,
    width=24,
    font=("Arial", 10, "bold")
).grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# FOOTER
# ============================================================

tk.Label(
    window,
    text="Personal Budget Tracker - Budget Management System",
    font=("Arial", 9),
    bg="white",
    fg="grey"
).pack(
    pady=(3, 8)
)


# ============================================================
# START APPLICATION
# ============================================================

window.mainloop()

