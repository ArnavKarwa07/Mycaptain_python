class Expense:

    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<expense: {self.name},{self.category},Rs{self.amount:.2f}>"


def main():
    print(f"RUNNING EXPENSE TRACKER!")
    expense_file_path = "expenses.csv"

    # get user input
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expense(expense_file_path)


def get_user_expense():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "FOOD",
        "HOME",
        "WORK",
        "FUN",
        "MISC",
    ]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}.{category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}:")) - 1

        if i in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category.Please enter valid entry")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"SAVING USER EXPENSE : {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path):
    print(f"SUMMARIZING  USER EXPENSE")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category, )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expense by category :")
    for key, amount in amount_by_category.items():
        print(f" {key}:Rs{amount:.2f}")
    total_spent = sum(x.amount for x in expenses)

    print(f"You have spent {total_spent:.2f} this month")


if __name__ == "__main__":
    main()
