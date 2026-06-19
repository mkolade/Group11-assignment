# 💸 Campus Mini Budget Tracker

A simple command-line budget tracking application built with Python for students. It helps users record income and expenses, view spending summaries, and maintain a basic budget using persistent file storage.

## 📖 Overview

Managing money as a student can be challenging. This application provides an easy way to:

* Record income from allowances, scholarships, part-time jobs, and other sources.
* Track daily expenses such as food, transport, books, data plans, and provisions.
* View a complete transaction history.
* Calculate total income, total expenses, and current balance.
* Save data automatically between sessions.
* Reset all financial records when needed.

All transaction data is stored locally in a text file, making the application lightweight and easy to use without requiring a database.

---

## ✨ Features

### Income Tracking

Add income from predefined categories:

* Monthly Allowance
* Scholarship
* Night Shift
* Other (custom category)

### Expense Tracking

Record expenses under categories such as:

* Food
* Transport
* Books
* Data Plan
* Provisions
* Other (custom category)

### Budget Summary

View:

* Complete transaction history
* Total income
* Total expenses
* Net balance

The application also provides feedback on your financial status:

* ✅ Positive balance
* 😐 Balanced spending
* ⚠️ Overspending warning

### Data Persistence

All transactions are automatically saved to a local text file (`budget_data.txt`) so your records remain available even after closing the application.

### Reset Functionality

Clear all stored transactions with confirmation to prevent accidental data loss.

---

## 🛠️ Technologies Used

* Python 3
* File Handling
* Lists and Dictionaries
* Functions
* Exception Handling
* Command-Line Interface (CLI)

---

## 📂 Project Structure

```text
Campus-Mini-Budget-Tracker/
│
├── budget_tracker.py
├── budget_data.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/campus-mini-budget-tracker.git
```

### 2. Navigate to the Project Folder

```bash
cd campus-mini-budget-tracker
```

### 3. Run the Program

```bash
python budget_tracker.py
```

---

## 📋 Usage

When the application starts, the following menu appears:

```text
1. Add Income
2. Add Expense
3. View Summary
4. Reset / Clear All Data
5. Exit
```

### Add Income

Choose an income category and enter the amount:

```text
1. Monthly Allowance
2. Scholarship
3. Night Shift
4. Other
```

### Add Expense

Choose an expense category and enter the amount:

```text
1. Food
2. Transport
3. Books
4. Data Plan
5. Provisions
6. Other
```

### View Summary

Displays:

* Transaction history
* Total income
* Total expenses
* Net balance

Example:

```text
Total Income:    N5000
Total Expenses:  N2000
Net Balance:     N3000
```

---

## 💾 Data Storage

Transactions are stored in a plain text file named:

`
budget_data.txt
'

Each transaction follows the format:


income,Monthly Allowance
expense,Food

## 🔮 Possible Future Improvements

* Monthly reports
* Expense filtering by category
* Date and time tracking
* CSV export
* Graphical user interface (GUI)
* Budget limits and spending alerts
* SQLite database integration

---

## 🎓 Educational Concepts Demonstrated

This project demonstrates several fundamental Python concepts:

* Functions
* Loops
* Conditional Statements
* Lists
* Dictionaries
* File Handling
* Exception Handling
* User Input Validation

---

## 🤝 Contributing

Contributions, improvements, and feature suggestions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---
