import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        description = entry_description.get()

        if category == "" or description == "":
            messagebox.showerror("Error", "All fields are required")
            return

        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })

        listbox.insert(tk.END, f"{category} - ₹{amount} ({description})")

        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_description.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter valid amount")

def show_summary():
    total = 0
    category_summary = {}

    for exp in expenses:
        total += exp["amount"]
        category_summary[exp["category"]] = category_summary.get(exp["category"], 0) + exp["amount"]

    summary = f"Total Expense: ₹{total}\n\nCategory-wise Summary:\n"
    for cat, amt in category_summary.items():
        summary += f"{cat}: ₹{amt}\n"

    messagebox.showinfo("Expense Summary", summary)

# GUI Window
window = tk.Tk()
window.title("Expense Tracker")
window.geometry("450x400")
window.resizable(False, False)

# Title
tk.Label(window, text="Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)

# Amount
tk.Label(window, text="Amount").pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

# Category
tk.Label(window, text="Category").pack()
entry_category = tk.Entry(window)
entry_category.pack()

# Description
tk.Label(window, text="Description").pack()
entry_description = tk.Entry(window)
entry_description.pack()

# Buttons
tk.Button(window, text="Add Expense", bg="green", fg="white", command=add_expense).pack(pady=8)
tk.Button(window, text="View Summary", bg="blue", fg="white", command=show_summary).pack()

# Expense List
tk.Label(window, text="Expenses").pack(pady=5)
listbox = tk.Listbox(window, width=50)
listbox.pack()

# Run GUI
window.mainloop()
