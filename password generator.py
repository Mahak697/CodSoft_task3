import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        use_lowercase = lowercase_var.get()
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Lowercase checkbox
lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

# Uppercase checkbox
uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

# Digits checkbox
digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

# Special characters checkbox
special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="Generated Password: ")
result_label.pack()

# Run the application
root.mainloop()
