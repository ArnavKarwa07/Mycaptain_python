import csv
import os


def create_expense_file(file_path):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Category', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def record_expense(file_path, category, amount):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([category, amount])


def calculate_total(file_path):
    total = 0
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total += float(row['Amount'])
    return total


def main():
    expense_file = 'expenses.csv'

    if not os.path.isfile(expense_file):
        create_expense_file(expense_file)

    while True:
        print("1. Record Expense")
        print("2. View Total Expense")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")
            record_expense(expense_file, category, amount)
            print("Expense recorded successfully!\n")
        elif choice == '2':
            total = calculate_total(expense_file)
            print(f"Total Expense: ${total}\n")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
