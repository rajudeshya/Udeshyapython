import tkinter as tk
from tkinter import messagebox


USERNAME = "admin"
PASSWORD = "admin123"

def login():
    user = username_entry.get()
    pw = password_entry.get()
    if user == USERNAME and pw == PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")
root.geometry("350x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)


tk.Label(root, text="Username", bg="#f0f0f0").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)


tk.Label(root, text="Password", bg="#f0f0f0").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", width=15, command=login, bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
