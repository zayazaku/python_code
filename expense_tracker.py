import csv 
from datetime import datetime
class ExpenseTracker:
    def __init__(self, filename = 'total_expenses_new.csv'):
        self.filename = filename

    def add_expense(self, date, description, category, amount):
        with open(self.filename, mode = 'a', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow([date, description, category, amount])

    def view_expenses(self):
        with open(self.filename, mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Description: {row[1]}, Category: {row[2]}, Amount: {row[3]} yen")

    def total_expenses(self):
        total = 0
        with open(self.filename, mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += int(row[3])
        print(f"Total expenses: {total} yen")

    def expenses_by_category(self, category):
        total = 0
        with open(self.filename, mode = 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == category:
                    total += int(row[3])
        print(f"Total expenses in {category}: {total} yen")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. View Expense")
        print("3. View Total Expense")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            category = input("Enter the category: ")
            amount = input("Enter the amount (in yen) ")
            tracker.add_expense(date, description, category, amount)
            print("Expense Added!")

        elif choice == "2":
            print("\nExpenses:")
            tracker.view_expenses()

        elif choice == "3":
            tracker.total_expenses()

        elif choice == "4":
            category = input("Enter the category: ")
            tracker.expenses_by_category(category)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
