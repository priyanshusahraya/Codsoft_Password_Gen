import string
import random
import tkinter as tk
from tkinter import messagebox


def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all required character types.")

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure the password contains at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + punctuation
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the resulting password to avoid any predictable patterns
    random.shuffle(password)

    return ''.join(password)


def on_generate_password():
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        label_password.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter the desired length of the password:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=on_generate_password)
button_generate.pack(pady=5)

label_password = tk.Label(root, text="Generated Password: ")
label_password.pack(pady=5)

# Start the GUI event loop
root.mainloop()
