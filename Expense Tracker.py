import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.configure(background='#7B68EE')  # Set background color to purple

        self.expenses = []

        self.amount_label = ttk.Label(root, text="Amount:", background='#7B68EE', foreground='white')  # Set label colors
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.category_label = ttk.Label(root, text="Category:", background='#7B68EE', foreground='white')
        self.category_label.grid(row=1, column=0, padx=5, pady=5)

        self.category_entry = ttk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        self.style = ttk.Style()
        self.style.configure('TButton', foreground='white', background='#483D8B')  # Set button style

        self.add_button = ttk.Button(root, text="Add Expense", command=self.add_expense, style='TButton')
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.view_button = ttk.Button(root, text="View Expenses", command=self.view_expenses, style='TButton')
        self.view_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.pattern_button = ttk.Button(root, text="View Spending Pattern", command=self.view_spending_pattern, style='TButton')
        self.pattern_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        if not amount or not category:
            messagebox.showerror("Error", "Please enter both amount and category.")
            return
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return
        date = datetime.date.today()
        self.expenses.append((date, amount, category))
        messagebox.showinfo("Success", "Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses recorded yet.")
            return
        expense_list = "\n".join([f"{date}: ${amount} - {category}" for date, amount, category in self.expenses])
        messagebox.showinfo("Expenses", expense_list)

    def view_spending_pattern(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses recorded yet.")
            return
        spending_by_category = {}
        for _, amount, category in self.expenses:
            if category in spending_by_category:
                spending_by_category[category] += amount
            else:
                spending_by_category[category] = amount
        pattern_list = "\n".join([f"{category}: ${amount}" for category, amount in spending_by_category.items()])
        messagebox.showinfo("Spending Pattern", pattern_list)

root = tk.Tk()
app = ExpenseTrackerApp(root)
root.mainloop()
