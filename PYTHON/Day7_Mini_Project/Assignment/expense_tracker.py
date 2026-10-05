import csv


# ==========================================
# GLOBAL VARIABLES
# ==========================================

expenses = []
categories = set()
total_expense = 0


# ==========================================
# ADD EXPENSE
# ==========================================

def add_expense(*args, **kwargs):

    global total_expense

    amount = args[0]
    category = args[1]
    date = args[2]

    description = kwargs.get("description", "No description")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)
    categories.add(category)

    total_expense = total_expense + amount

    return "Expense added successfully!"


# ==========================================
# DELETE EXPENSE
# ==========================================

def delete_expense(index):

    global total_expense

    if index >= 0 and index < len(expenses):

        deleted_expense = expenses.pop(index)

        total_expense = total_expense - deleted_expense["amount"]

        return "Expense deleted successfully!"

    else:

        return "Invalid expense number!"


# ==========================================
# SEARCH EXPENSE
# ==========================================

def search_expense(keyword):

    result = []

    keyword = keyword.lower().strip()

    for expense in expenses:

        category = expense["category"].lower()
        description = expense["description"].lower()

        if keyword in category or keyword in description:

            result.append(expense)

    return result


# ==========================================
# SHOW ALL EXPENSES
# ==========================================

def show_expenses():

    if len(expenses) == 0:

        print("\nNo expenses available.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i in range(len(expenses)):

        expense = expenses[i]

        print(
            i + 1,
            "|",
            expense["date"],
            "|",
            expense["category"],
            "| ₹",
            expense["amount"],
            "|",
            expense["description"]
        )


# ==========================================
# TOTAL EXPENSE
# ==========================================

def get_total_expense():

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    return total


# ==========================================
# MONTHLY EXPENSE
# ==========================================

def monthly_expense(month):

    total = 0

    month = month.strip()

    for expense in expenses:

        date = expense["date"]

        # Date format: YYYY-MM-DD
        expense_month = date[0:7]

        if expense_month == month:

            total = total + expense["amount"]

    return total


# ==========================================
# SHOW CATEGORIES
# ==========================================

def show_categories():

    print("\n========== CATEGORIES ==========")

    if len(categories) == 0:

        print("No categories available.")

    else:

        for category in categories:

            print("-", category)


# ==========================================
# RECENT EXPENSES
# ==========================================

def recent_expenses():

    print("\n========== RECENT EXPENSES ==========")

    if len(expenses) == 0:

        print("No expenses available.")

        return

    # Last 3 expenses
    recent = expenses[-3:]

    for expense in recent:

        print(
            expense["date"],
            "|",
            expense["category"],
            "| ₹",
            expense["amount"],
            "|",
            expense["description"]
        )


# ==========================================
# SAVE TO CSV
# ==========================================

def save_to_csv(filename="expenses.csv"):

    with open(filename, "w", newline="") as file:

        fieldnames = [
            "amount",
            "category",
            "date",
            "description"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for expense in expenses:

            writer.writerow(expense)

    return "Expenses saved to CSV successfully!"


# ==========================================
# LOAD FROM CSV
# ==========================================

def load_from_csv(filename="expenses.csv"):

    global total_expense

    try:

        with open(filename, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                expense = {
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"],
                    "description": row["description"]
                }

                expenses.append(expense)

                categories.add(row["category"])

                total_expense = total_expense + float(row["amount"])

        return "Expenses loaded from CSV successfully!"

    except FileNotFoundError:

        return "CSV file not found. Starting with empty tracker."


# ==========================================
# MAIN PROGRAM
# ==========================================

load_message = load_from_csv()

print(load_message)


while True:

    print("\n======================================")
    print("          EXPENSE TRACKER")
    print("======================================")

    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Search Expense")
    print("4. Show All Expenses")
    print("5. Total Expense")
    print("6. Monthly Expense")
    print("7. Show Categories")
    print("8. Recent Expenses")
    print("9. Save to CSV")
    print("10. Exit")

    choice = input("Enter your choice: ").strip()


    # ======================================
    # ADD
    # ======================================

    if choice == "1":

        amount = float(input("Enter amount: "))

        if amount <= 0:

            print("Amount must be greater than 0.")

            continue

        category = input("Enter category: ").strip().lower()

        date = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        description = input(
            "Enter description: "
        ).strip()

        message = add_expense(
            amount,
            category,
            date,
            description=description
        )

        print(message)


    # ======================================
    # DELETE
    # ======================================

    elif choice == "2":

        show_expenses()

        if len(expenses) > 0:

            number = int(
                input("Enter expense number to delete: ")
            )

            result = delete_expense(number - 1)

            print(result)


    # ======================================
    # SEARCH
    # ======================================

    elif choice == "3":

        keyword = input(
            "Enter category or description: "
        )

        result = search_expense(keyword)

        if len(result) == 0:

            print("No matching expense found.")

        else:

            print("\n========== SEARCH RESULT ==========")

            for expense in result:

                print(
                    expense["date"],
                    "|",
                    expense["category"],
                    "| ₹",
                    expense["amount"],
                    "|",
                    expense["description"]
                )


    # ======================================
    # SHOW ALL
    # ======================================

    elif choice == "4":

        show_expenses()


    # ======================================
    # TOTAL
    # ======================================

    elif choice == "5":

        total = get_total_expense()

        print("\nTotal Expense: ₹", total)


    # ======================================
    # MONTHLY EXPENSE
    # ======================================

    elif choice == "6":

        month = input(
            "Enter month (YYYY-MM): "
        ).strip()

        total = monthly_expense(month)

        print(
            "Expense for",
            month,
            ": ₹",
            total
        )


    # ======================================
    # CATEGORIES
    # ======================================

    elif choice == "7":

        show_categories()


    # ======================================
    # RECENT
    # ======================================

    elif choice == "8":

        recent_expenses()


    # ======================================
    # SAVE CSV
    # ======================================

    elif choice == "9":

        result = save_to_csv()

        print(result)


    # ======================================
    # EXIT
    # ======================================

    elif choice == "10":

        save_to_csv()

        print(
            "\nExpenses automatically saved."
        )

        print(
            "Thank you for using Expense Tracker!"
        )

        break


    # ======================================
    # INVALID
    # ======================================

    else:

        print(
            "Invalid choice! Please select 1-10."
        )