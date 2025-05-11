import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.config(bg="purple")

        self.tasks = []

        # Title
        title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="white")
        title.pack(pady=10)

        # Entry box
        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
        self.task_entry.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root, bg="light pink")
        button_frame.pack(pady=5)

        add_btn = tk.Button(button_frame, text="Add Task", width=12, command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        del_btn = tk.Button(button_frame, text="Delete Task", width=12, command=self.delete_task)
        del_btn.grid(row=0, column=1, padx=5)

        complete_btn = tk.Button(button_frame, text="Mark as Done", width=12, command=self.mark_done)
        complete_btn.grid(row=0, column=2, padx=5)

        # Listbox
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=45, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("✔️ "):
                self.tasks[index] = "✔️ " + task
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
