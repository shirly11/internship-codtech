# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 22:18:57 2025

@author: ADMIN
"""

import tkinter as tk
from tkinter import messagebox

class BasicToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("300x400")

        # Input field
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        # Add task button
        tk.Button(root, text="Add Task", command=self.add_task).pack()

        # Task list display
        self.task_box = tk.Listbox(root, width=35, height=15)
        self.task_box.pack(pady=10)

        # Delete task button
        tk.Button(root, text="Delete Task", command=self.delete_task).pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_box.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def delete_task(self):
        selected = self.task_box.curselection()
        if selected:
            self.task_box.delete(selected)
        else:
            messagebox.showerror("Error", "Please select a task to delete.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BasicToDoApp(root)
    root.mainloop()
