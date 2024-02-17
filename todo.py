import tkinter as tk
from tkinter import messagebox
import random

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x600")
        self.root.configure(bg="#FFFFFF")  

        self.tasks = []

        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#FF69B4")
        self.title_label.pack(pady=(20, 10))

        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(ipady=10, padx=20, pady=10, fill=tk.X)

        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 14, "bold"), command=self.add_task, bg="#FF69B4", fg="#FFFFFF", relief=tk.GROOVE)
        self.add_button.pack(pady=(0, 10), padx=20, ipadx=10, ipady=5, fill=tk.X)

        self.task_listbox = tk.Listbox(root, font=("Arial", 14), selectbackground="#FF69B4", bg="#FFFFFF", fg="#000000", relief=tk.GROOVE)
        self.task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14, "bold"), command=self.delete_task, bg="#FF69B4", fg="#FFFFFF", relief=tk.GROOVE)
        self.delete_button.pack(padx=20, pady=(0, 10), ipadx=10, ipady=5, fill=tk.X)

        self.complete_button = tk.Button(root, text="Mark as Completed", font=("Arial", 14, "bold"), command=self.mark_as_completed, bg="#FF69B4", fg="#FFFFFF", relief=tk.GROOVE)
        self.complete_button.pack(padx=20, ipadx=10, ipady=5, fill=tk.X)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

    def mark_as_completed(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.task_listbox.itemconfig(index, {'bg': '#FFFFFF', 'fg': '#808080', 'font': ('Arial', 14, 'italic')})

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
