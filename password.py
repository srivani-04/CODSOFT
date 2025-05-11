import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4 characters.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Heading
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold")).pack(pady=10)

# Password length input
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Enter Password Length: ").pack(side=tk.LEFT)
length_entry = tk.Entry(frame, width=5)
length_entry.pack(side=tk.LEFT)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Display generated password
password_entry = tk.Entry(root, font=("Helvetica", 12), width=30, justify="center")
password_entry.pack(pady=5)

# Run the application
root.mainloop()
