import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

# Add new contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        contacts.append({
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        })
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required.")

# View contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        contact_list.insert(tk.END, f"{idx+1}. {contact['Name']} - {contact['Phone']}")

# Show selected contact
def show_selected_contact(event):
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["Name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["Phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["Email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["Address"])

# Search contact
def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        if query in contact["Name"].lower() or query in contact["Phone"]:
            contact_list.insert(tk.END, f"{idx+1}. {contact['Name']} - {contact['Phone']}")

# Update contact
def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts[index]["Name"] = name_entry.get().strip()
        contacts[index]["Phone"] = phone_entry.get().strip()
        contacts[index]["Email"] = email_entry.get().strip()
        contacts[index]["Address"] = address_entry.get().strip()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")

# Delete contact
def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
        if confirm:
            contacts.pop(selected_index[0])
            update_contact_list()
            clear_entries()
    else:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")
root.configure(bg="lightblue")

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=50)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="orange").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="red", fg="white").pack(pady=5)

# Search field
tk.Label(root, text="Search by Name or Phone").pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# Contact List
contact_list = tk.Listbox(root, width=60)
contact_list.pack(pady=10)
contact_list.bind('<<ListboxSelect>>', show_selected_contact)

update_contact_list()

root.mainloop()
