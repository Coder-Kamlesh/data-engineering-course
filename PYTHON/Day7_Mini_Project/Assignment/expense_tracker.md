# 💰 Expense Tracker

A beginner-friendly Python Mini Project for managing daily expenses.

## Features

- Add Expense
- Delete Expense
- Search Expense
- Show All Expenses
- Calculate Total Expense
- Calculate Monthly Expense
- Show Categories
- Show Recent Expenses
- Save Expenses to CSV
- Load Expenses from CSV

## Python Concepts Used

### 1. Functions

Functions are used to divide the project into small reusable parts.

Examples:

- add_expense()
- delete_expense()
- search_expense()
- get_total_expense()
- monthly_expense()
- save_to_csv()
- load_from_csv()

### 2. *args

Used in the add_expense() function.

Example:

def add_expense(*args, **kwargs):

*args stores multiple positional arguments in a tuple.

### 3. **kwargs

Used for the description parameter.

Example:

add_expense(
    amount,
    category,
    date,
    description=description
)

**kwargs stores keyword arguments in a dictionary.

### 4. return

Functions return results to the main program.

Example:

return total

### 5. Scope

Global variables:

- expenses
- categories
- total_expense

Local variables are created inside functions.

## Dictionaries

Each expense is stored as a dictionary.

Example:

{
    "amount": 250,
    "category": "food",
    "date": "2026-10-05",
    "description": "Lunch"
}

## Lists

The main expenses are stored in a list.

Example:

expenses = []

List methods used:

- append()
- pop()

List slicing:

expenses[-3:]

This returns the last 3 expenses.

## Tuples

*args stores positional arguments as a tuple.

## Sets

Categories are stored using a set.

Example:

categories = set()

Set method used:

add()

Sets automatically avoid duplicate categories.

## String Methods

The project uses:

lower()
strip()

Example:

category = category.lower().strip()

## Loops

### while

Used for the main menu.

### for

Used for displaying and searching expenses.

### range()

Used to access expense indexes.

## Conditional Statements

if / elif / else are used for menu selection and validation.

## Operators

The project uses:

- +
- -
- <=
- >=
- ==
- in

## CSV

The Python csv module is used to save and load expenses.

File name:

expenses.csv

## How to Run

1. Install Python.
2. Open the project folder.
3. Run:

python expense_tracker.py

4. Select options from the menu.

## Project Structure

Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md

## Future Improvements

- Add budget limit
- Add income tracking
- Add monthly reports
- Add category-wise total
- Add graphical reports
- Add login system
- Connect with database