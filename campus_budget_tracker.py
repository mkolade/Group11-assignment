# ============================================================
# CAMPUS MINI BUDGET TRACKER
# A simple CLI app to track income and expenses as a student
# Saves data to a text file so nothing gets lost
# ============================================================

# This is the file where all our transactions will be saved
DATA_FILE = "budget_data.txt"


# ------------------------------------------------------------------
# FUNCTION: load_transactions
# Opens the text file and reads all saved transactions into a list
# Each transaction is stored as a dictionary with keys:
# "type", "category", and "amount"
# ------------------------------------------------------------------
def load_transactions():
    transactions = []  # start with an empty list

    try:
        file = open(DATA_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()  # remove any extra spaces or newlines
            if line == "":
                continue  # skip blank lines

            # each line looks like: income,Monthly Allowance,5000.0
            parts = line.split(",")

            if len(parts) == 3:
                transaction = {}
                transaction["type"] = parts[0]
                transaction["category"] = parts[1]
                transaction["amount"] = float(parts[2])
                transactions.append(transaction)

    except FileNotFoundError:
        # this just means no data has been saved yet, that's fine
        pass

    return transactions


# ------------------------------------------------------------------
# FUNCTION: save_transactions
# Takes the full list of transactions and writes them all to the file
# We overwrite the file each time so there are no duplicate entries
# ------------------------------------------------------------------
def save_transactions(transactions):
    file = open(DATA_FILE, "w")

    for t in transactions:
        # write each transaction as a comma-separated line
        line = t["type"] + "," + t["category"] + "," + str(t["amount"]) + "\n"
        file.write(line)

    file.close()


# ------------------------------------------------------------------
# FUNCTION: add_income
# Shows the income category menu and asks the user for an amount
# ------------------------------------------------------------------
def add_income(transactions):
    print("\n--- ADD INCOME ---")
    print("Select income category:")
    print("  1. Monthly Allowance")
    print("  2. Scholarship")
    print("  3. Night Shift")
    print("  4. Other")

    choice = input("Enter choice (1-4): ").strip()

    # figure out which category was chosen
    if choice == "1":
        category = "Monthly Allowance"
    elif choice == "2":
        category = "Scholarship"
    elif choice == "3":
        category = "Night Shift"
    elif choice == "4":
        # let the user type in whatever category they want
        category = input("Enter custom income description: ").strip()
        if category == "":
            category = "Other Income"  # default if they left it blank
    else:
        print("Invalid choice. Going back to main menu.")
        return  # exit the function early if invalid

    # now ask for the amount and make sure it is a valid number
    try:
        amount = float(input("Enter amount (e.g. 5000): ").strip())
        if amount <= 0:
            print("Amount must be greater than zero. Cancelling.")
            return
    except ValueError:
        print("That doesn't look like a number. Cancelling.")
        return

    # build the transaction dictionary and add it to our list
    new_transaction = {}
    new_transaction["type"] = "income"
    new_transaction["category"] = category
    new_transaction["amount"] = amount

    transactions.append(new_transaction)
    save_transactions(transactions)  # save immediately so we don't lose it

    print("Income of N" + str(amount) + " (" + category + ") recorded!")


# ------------------------------------------------------------------
# FUNCTION: add_expense
# Shows the expense category menu and asks the user for an amount
# ------------------------------------------------------------------
def add_expense(transactions):
    print("\n--- ADD EXPENSE ---")
    print("Select expense category:")
    print("  1. Food")
    print("  2. Transport")
    print("  3. Books")
    print("  4. Data Plan")
    print("  5. Provisions")
    print("  6. Other")

    choice = input("Enter choice (1-6): ").strip()

    # figure out which category was chosen
    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    elif choice == "3":
        category = "Books"
    elif choice == "4":
        category = "Data Plan"
    elif choice == "5":
        category = "Provisions"
    elif choice == "6":
        # let the user type in a custom expense description
        category = input("Enter custom expense description: ").strip()
        if category == "":
            category = "Other Expense"  # default if they left it blank
    else:
        print("Invalid choice. Going back to main menu.")
        return

    # now ask for the amount and validate it
    try:
        amount = float(input("Enter amount (e.g. 800): ").strip())
        if amount <= 0:
            print("Amount must be greater than zero. Cancelling.")
            return
    except ValueError:
        print("That doesn't look like a number. Cancelling.")
        return

    # build the transaction dictionary and add it to our list
    new_transaction = {}
    new_transaction["type"] = "expense"
    new_transaction["category"] = category
    new_transaction["amount"] = amount

    transactions.append(new_transaction)
    save_transactions(transactions)  # save to file right away

    print("Expense of N" + str(amount) + " (" + category + ") recorded!")


# ------------------------------------------------------------------
# FUNCTION: show_summary
# Prints a full history of all transactions, calculates totals,
# and shows the net balance with a warning if it goes below zero
# ------------------------------------------------------------------
def show_summary(transactions):
    print("\n========================================")
    print("         BUDGET SUMMARY")
    print("========================================")

    if len(transactions) == 0:
        print("No transactions recorded yet.")
        return

    print("\n--- TRANSACTION HISTORY ---")

    # we will add up income and expenses as we loop through
    total_income = 0.0
    total_expenses = 0.0

    count = 1  # just a simple counter to number each line

    for t in transactions:
        if t["type"] == "income":
            # show income entries with a + sign
            print(str(count) + ". [INCOME]  " + t["category"] + "  -->  +N" + str(t["amount"]))
            total_income = total_income + t["amount"]
        else:
            # show expense entries with a - sign
            print(str(count) + ". [EXPENSE] " + t["category"] + "  -->  -N" + str(t["amount"]))
            total_expenses = total_expenses + t["amount"]

        count = count + 1

    # now calculate the net balance
    net_balance = total_income - total_expenses

    print("\n--- CALCULATIONS ---")
    print("Total Income:    N" + str(round(total_income, 2)))
    print("Total Expenses:  N" + str(round(total_expenses, 2)))
    print("                 ----------")
    print("Net Balance:     N" + str(round(net_balance, 2)))

    # budget check: warn the user if they are spending more than they earn
    if net_balance < 0:
        print("\n⚠️  Wahala dey oh! You're spending more than you're earning!")
        print("   Your account is in the red by N" + str(round(abs(net_balance), 2)) + ". Time to cut back! 😬")
    elif net_balance == 0:
        print("\n😐 You've spent exactly what you earned. Nothing left over!")
    else:
        print("\n✅ You still have N" + str(round(net_balance, 2)) + " left. Keep it up! 💪")

    print("========================================")


# ------------------------------------------------------------------
# FUNCTION: reset_data
# Wipes the text file clean and clears the in-memory list
# Asks for confirmation first so the user doesn't do it by accident
# ------------------------------------------------------------------
def reset_data(transactions):
    print("\n--- RESET / CLEAR ALL DATA ---")
    confirm = input("Are you sure you want to delete ALL transactions? (yes/no): ").strip().lower()

    if confirm == "yes":
        # clear the list in memory
        transactions.clear()

        # overwrite the file with nothing
        file = open(DATA_FILE, "w")
        file.close()

        print("All data has been cleared. Starting fresh! 🗑️")
    else:
        print("Reset cancelled. Your data is safe.")


# ------------------------------------------------------------------
# MAIN PROGRAM
# This is where everything runs. The while loop keeps the menu
# showing until the user decides to quit.
# ------------------------------------------------------------------

print("====================================")
print("   CAMPUS MINI BUDGET TRACKER 💸")
print("====================================")
print("Welcome! Let's keep track of your money.")

# load any existing transactions from the file when the program starts
transactions = load_transactions()

# keep running until the user chooses to exit
running = True

while running:
    # show the main menu every time the loop restarts
    print("\n-------- MAIN MENU --------")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Reset / Clear All Data")
    print("5. Exit")
    print("---------------------------")

    menu_choice = input("What do you want to do? (1-5): ").strip()

    if menu_choice == "1":
        add_income(transactions)

    elif menu_choice == "2":
        add_expense(transactions)

    elif menu_choice == "3":
        show_summary(transactions)

    elif menu_choice == "4":
        reset_data(transactions)

    elif menu_choice == "5":
        print("\nGoodbye! Stay on top of your budget! 👋")
        running = False  # this stops the while loop and ends the program

    else:
        print("Hmm, that's not a valid option. Please enter a number from 1 to 5.")
