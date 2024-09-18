import tkinter as tk
from tkinter import messagebox

# Personal Finance Tracker class
class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("400x400")

        # Variables to store income, expenses, savings, and budget goal
        self.income = 0.0
        self.expenses = 0.0
        self.savings = 0.0
        self.budget_goal = 0.0

        # Create and place labels and entry widgets for the UI
        self.create_widgets()

    def create_widgets(self):
        # Income
        tk.Label(self.root, text="Enter Income:").pack(pady=5)
        self.income_entry = tk.Entry(self.root)
        self.income_entry.pack(pady=5)
        tk.Button(self.root, text="Add Income", command=self.add_income).pack(pady=5)

        # Expenses
        tk.Label(self.root, text="Enter Expenses:").pack(pady=5)
        self.expenses_entry = tk.Entry(self.root)
        self.expenses_entry.pack(pady=5)
        tk.Button(self.root, text="Add Expenses", command=self.add_expenses).pack(pady=5)

        # Budget Goal
        tk.Label(self.root, text="Set Budget Goal:").pack(pady=5)
        self.budget_entry = tk.Entry(self.root)
        self.budget_entry.pack(pady=5)
        tk.Button(self.root, text="Set Budget", command=self.set_budget).pack(pady=5)

        # Savings Display
        self.savings_label = tk.Label(self.root, text="Total Savings: $0.00")
        self.savings_label.pack(pady=10)

        # Buttons to generate reports
        tk.Button(self.root, text="Generate Report", command=self.generate_report).pack(pady=5)

    # Method to add income
    def add_income(self):
        try:
            income_value = float(self.income_entry.get())
            self.income += income_value
            self.update_savings()
            messagebox.showinfo("Success", f"Added ${income_value:.2f} to income.")
            self.income_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for income.")

    # Method to add expenses
    def add_expenses(self):
        try:
            expenses_value = float(self.expenses_entry.get())
            self.expenses += expenses_value
            self.update_savings()
            messagebox.showinfo("Success", f"Added ${expenses_value:.2f} to expenses.")
            self.expenses_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for expenses.")

    # Method to set budget goal
    def set_budget(self):
        try:
            budget_value = float(self.budget_entry.get())
            self.budget_goal = budget_value
            messagebox.showinfo("Success", f"Budget goal set to ${budget_value:.2f}.")
            self.budget_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for budget goal.")

    # Method to update savings
    def update_savings(self):
        self.savings = self.income - self.expenses
        self.savings_label.config(text=f"Total Savings: ${self.savings:.2f}")

    # Method to generate financial report
    def generate_report(self):
        report = (
            f"Financial Report\n"
            f"-----------------\n"
            f"Income: ${self.income:.2f}\n"
            f"Expenses: ${self.expenses:.2f}\n"
            f"Budget Goal: ${self.budget_goal:.2f}\n"
            f"Savings: ${self.savings:.2f}\n"
        )

        # Check if budget goal is met
        if self.savings >= self.budget_goal:
            report += "\nYou have met your budget goal!"
        else:
            report += f"\nYou are ${self.budget_goal - self.savings:.2f} away from your budget goal."

        messagebox.showinfo("Financial Report", report)

# Main function to start the finance tracker app
def main():
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
