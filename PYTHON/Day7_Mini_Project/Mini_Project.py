# -------------------------------
# EXPENSE TRACKER MINI PROJECT
# -------------------------------

expenses = []
categories = set()

total_expense = 0


# Add Expense
def add_expense(*args, **kwargs):
    global total_expense

    amount = args[0]
    category = args[1]
    description = kwargs.get("description", "No description")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    categories.add(category)

    total_expense = total_expense + amount

    return "Expense added successfully!"


# Delete Expense
def delete_expense(index):
    global total_expense

    if index >= 0 and index < len(expenses):

        deleted_expense = expenses.pop(index)

        total_expense = total_expense - deleted_expense["amount"]

        return "Expense deleted successfully!"

    else:
        return "Invalid expense number!"


# Search Expense
def search_expense(keyword):
    result = []

    keyword = keyword.lower().strip()

    for expense in expenses:

        if (keyword in expense["category"].lower() or
                keyword in expense["description"].lower()):

            result.append(expense)

    return result


# Show All Expenses
def show_expenses():

    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n---------- ALL EXPENSES ----------")

    for i in range(len(expenses)):

        expense = expenses[i]

        print(
            i + 1,
            ".",
            expense["category"],
            "- ₹",
            expense["amount"],
            "-",
            expense["description"]
        )


# Show Categories
def show_categories():

    print("\n---------- CATEGORIES ----------")

    if len(categories) == 0:
        print("No categories available.")
    else:

        for category in categories:
            print("-", category)


# Calculate Total
def get_total():

    return total_expense


# Main Program
while True:

    print("\n================================")
    print("       EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. Delete Expense")
    print("3. Search Expense")
    print("4. Show All Expenses")
    print("5. Show Categories")
    print("6. Show Total Expense")
    print("7. Show Recent Expenses")
    print("8. Exit")

    choice = input("Enter your choice: ").strip()

    # -------------------------
    # ADD
    # -------------------------

    if choice == "1":

        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        category = input("Enter category: ").strip().lower()

        description = input("Enter description: ").strip()

        message = add_expense(
            amount,
            category,
            description=description
        )

        print(message)

    # -------------------------
    # DELETE
    # -------------------------

    elif choice == "2":

        show_expenses()

        if len(expenses) > 0:

            number = int(input("Enter expense number to delete: "))

            result = delete_expense(number - 1)

            print(result)

    # -------------------------
    # SEARCH
    # -------------------------

    elif choice == "3":

        keyword = input("Enter category or description to search: ")

        result = search_expense(keyword)

        if len(result) == 0:

            print("No matching expense found.")

        else:

            print("\n---------- SEARCH RESULT ----------")

            for expense in result:

                print(
                    expense["category"],
                    "- ₹",
                    expense["amount"],
                    "-",
                    expense["description"]
                )

    # -------------------------
    # SHOW ALL
    # -------------------------

    elif choice == "4":

        show_expenses()

    # -------------------------
    # SHOW CATEGORIES
    # -------------------------

    elif choice == "5":

        show_categories()

    # -------------------------
    # TOTAL
    # -------------------------

    elif choice == "6":

        print("\nTotal Expense: ₹", get_total())

    # -------------------------
    # RECENT EXPENSES
    # -------------------------

    elif choice == "7":

        if len(expenses) == 0:

            print("No expenses available.")

        else:

            print("\n---------- RECENT EXPENSES ----------")

            recent = expenses[-3:]

            for expense in recent:

                print(
                    expense["category"],
                    "- ₹",
                    expense["amount"],
                    "-",
                    expense["description"]
                )

    # -------------------------
    # EXIT
    # -------------------------

    elif choice == "8":

        print("Thank you for using Expense Tracker!")
        break

    # -------------------------
    # INVALID
    # -------------------------

    else:

        print("Invalid choice! Please try again.")