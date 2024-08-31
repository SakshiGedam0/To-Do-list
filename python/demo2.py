import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack()

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            messagebox.showinfo("Task Completed", f"Task '{task}' completed.")
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            messagebox.showinfo("Task Deleted", f"Task '{task}' deleted.")
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
