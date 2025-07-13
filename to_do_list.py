import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize list
to_do_list = []

# Functions
def add_task():
    task = simpledialog.askstring("Add Task", "Enter a task:")
    if task:
        to_do_list.append(task)
        update_list()
        messagebox.showinfo("Success", "Task added.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        to_do_list.remove(task)
        update_list()
        messagebox.showinfo("Deleted", "Task deleted.")
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_list():
    listbox.delete(0, tk.END)
    for task in to_do_list:
        listbox.insert(tk.END, task)

# GUI setup
window = tk.Tk()
window.title("To-Do List")

title_label = tk.Label(window, text="📝 To-Do List App", font=("Arial", 16))
title_label.pack(pady=10)

listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

add_button = tk.Button(window, text="➕ Add Task", command=add_task, width=20)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="🗑️ Delete Selected", command=delete_task, width=20)
delete_button.pack(pady=5)

window.mainloop()
