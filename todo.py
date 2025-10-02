import tkinter as tk
from tkinter import messagebox

# Task list to store all tasks
tasks = []

# Functions for the To-Do List functionality

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        list_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def remove_task():
    task = task_listbox.get(tk.ACTIVE)
    if task in tasks:
        tasks.remove(task)
        list_tasks()

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index[0]] = new_task
            list_tasks()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def mark_task_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        tasks[selected_task_index[0]] = task + " (Done)"
        list_tasks()
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def clear_tasks():
    tasks.clear()
    list_tasks()

def list_tasks():
    # Clear the listbox
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI setup
window = tk.Tk()
window.title("To-Do List App")

# Set the window background color
window.configure(bg="white")

# Title label
title_label = tk.Label(window, text="To-Do List", font=("Helvetica", 24), bg="white", fg="orange")
title_label.pack(pady=10)

# Task entry field
task_entry = tk.Entry(window, width=40)
task_entry.pack(pady=10)

# Task list display area
task_listbox = tk.Listbox(window, height=10, width=50, font=("Helvetica", 14))
task_listbox.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(window, bg="white")
button_frame.pack(pady=20)

# Buttons for various operations
add_button = tk.Button(button_frame, text="Add Task", width=15, command=add_task, bg="orange", fg="white")
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", width=15, command=remove_task, bg="orange", fg="white")
remove_button.grid(row=0, column=1, padx=5)

update_button = tk.Button(button_frame, text="Update Task", width=15, command=update_task, bg="orange", fg="white")
update_button.grid(row=1, column=0, padx=5, pady=5)

mark_done_button = tk.Button(button_frame, text="Mark Task Done", width=15, command=mark_task_done, bg="orange", fg="white")
mark_done_button.grid(row=1, column=1, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", width=15, command=clear_tasks, bg="orange", fg="white")
clear_button.grid(row=2, column=0, columnspan=2, pady=5)

# Start the GUI event loop
window.mainloop()
