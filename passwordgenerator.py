import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("400x200")

        self.length_label = tk.Label(self, text="Password Length:", font=('Arial', 12))
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self, font=('Arial', 12))
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password, font=('Arial', 12))
        self.generate_button.pack(pady=20)

        self.password_entry = tk.Entry(self, font=('Arial', 12), width=30)
        self.password_entry.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length should be a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError as ve:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()

