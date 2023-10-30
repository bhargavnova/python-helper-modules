#This is a simple contact book program with GUI using tkinter module in python.
#The buttons in GUI are made to hover and change color when the mouse is hovered over them.

import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_list.insert(tk.END, f"{name}: {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to save contacts to a file
def save_contacts():
    with open("contacts.txt", "w") as file:
        for item in contact_list.get(0, tk.END):
            file.write(item + "\n")

# Button hover effect functions
def on_add_hover(event):
    add_button.config(bg="lightblue")

def on_add_leave(event):
    add_button.config(bg="SystemButtonFace")

def on_save_hover(event):
    save_button.config(bg="lightblue")

def on_save_leave(event):
    save_button.config(bg="SystemButtonFace")

app = tk.Tk()
app.title("Contact Book")

name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(app, text="Phone:")
phone_label.grid(row=1, column=0)

phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2)
add_button.bind("<Enter>", on_add_hover)
add_button.bind("<Leave>", on_add_leave)

contact_list = tk.Listbox(app, width=40, height=10)
contact_list.grid(row=3, column=0, columnspan=2)

# Load contacts from the file when the application starts
try:
    with open("contacts.txt", "r") as file:
        contacts = file.read().splitlines()
        for contact in contacts:
            contact_list.insert(tk.END, contact)
except FileNotFoundError:
    pass

save_button = tk.Button(app, text="Save Contacts", command=save_contacts)
save_button.grid(row=4, column=0, columnspan=2)
save_button.bind("<Enter>", on_save_hover)
save_button.bind("<Leave>", on_save_leave)

app.mainloop()