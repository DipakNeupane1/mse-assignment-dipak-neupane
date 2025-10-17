# Week 11 - Activity 2: Personal Expense Tracker with Using Unit Testing
# Develop a program using Object-Oriented Programming (OOP)  and Unit-testing to create a simple Personal Expense Tracker.
# The system should include at least two main functionalities:
# Add Expense : Allow the user to add a new expense with a description and an amount.
# Calculate Total Expense :  Compute and display the total amount of all recorded expenses.
# Share your GitHub Link at the end here.

import unittest


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.expenses.append({"description": description, "amount": amount})

    def calculate_total_expense(self):
        return sum(item["amount"] for item in self.expenses)


class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Lunch", 15.50)
        tracker.add_expense("Transport", 5.75)
        self.assertEqual(len(tracker.expenses), 2)  # assert the length of expenses list

    def test_calculate_total_expense(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Lunch", 15.50)
        tracker.add_expense("Transport", 5.75)
        self.assertEqual(
            tracker.calculate_total_expense(), 21.25
        )  # assert the total expense


if __name__ == "__main__":
    unittest.main()
