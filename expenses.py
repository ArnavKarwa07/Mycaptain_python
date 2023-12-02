import json

# Initialize an empty dictionary to store expenses
expenses = {}

# Create a new json file
with open('expenses.json', 'w') as json_file:
    json.dump(expenses, json_file)


# Function to load expenses data from a file
def load_expenses():
    with open("expenses.json", "r") as file:
        return json.load(file)


# Function to save expenses data to a file
def save_expenses():
    with open("expenses.json", "w") as file:
        return json.dumps(expenses)


# Load expenses data if the file exists
expenses = load_expenses()

while True:
    print("\nExpense Recorder Menu:")
    print("1. Add an Expense")
    print("2. Expenses Summary")
    print("3. List Expense Categories")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        save_expenses()
        print("Expense added successfully!")

    elif choice == '2':
        print("\nExpenses Summary:")
        total_expenses = sum(expenses.values())
        if total_expenses > 0:
            for category, amount in expenses.items():
                print(f"{category}: ${amount:.2f}")
            print(f"Total Expenses: ${total_expenses:.2f}")
        else:
            print("No expenses recorded yet.")

    elif choice == '3':
        print("\nExpense Categories:")
        for category in expenses:
            print(category)

    elif choice == '4':
        print("Exiting Expense Recorder. Have a nice day!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

# Save expenses before exiting
save_expenses()
