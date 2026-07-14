import tkinter as tk
from tkinter import ttk, messagebox
import storage
import dashboard
import re
def validate_signup(username, email, password):
    if username == "":
        messagebox.showinfo("Signup Failed", "Please enter a username.")
        return False

    elif email == "":
        messagebox.showinfo("Signup Failed", "Please enter your email.")
        return False

    elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        messagebox.showinfo("Signup Failed", "Please enter a valid email address.")
        return False

    elif password == "":
        messagebox.showinfo("Signup Failed", "Please enter a password.")
        return False

    elif not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{6,}$', password):
        messagebox.showinfo(
            "Signup Failed",
            "Password must contain:\n"
            "- At least 6 characters\n"
            "- One uppercase letter\n"
            "- One number\n"
            "- One special character"
        )
        return False

    else:
        if storage.add_user(username, email, password):
            messagebox.showinfo("Signup Successful", "Account created successfully!")
            return True
        else:
            messagebox.showinfo("Signup Failed", "Username already exists.")
            return False

def handle_submit(username, password):
    if username == "":
        messagebox.showinfo("Login Failed", "Please enter your username.")

    elif password == "":
        messagebox.showinfo("Login Failed", "Please enter your password.")

    else:
        if storage.login_user(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
            login_frame.destroy()
            dashboard.show_dashboard(root, username)
        else:
            messagebox.showinfo("Login Failed", "Invalid username or password.")

def handle_signup_page():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("420x330")
    signup_window.resizable(False, False)

    frame = ttk.Frame(signup_window, padding=20)
    frame.pack(expand=True)

    ttk.Label(
        frame,
        text="Create Account",
        style="Heading.TLabel"
    ).grid(row=0, column=0, columnspan=2, pady=20)

    ttk.Label(frame, text="Username").grid(row=1, column=0, sticky="w", pady=8)
    username_entry = ttk.Entry(frame, width=30)
    username_entry.grid(row=1, column=1)

    ttk.Label(frame, text="Email").grid(row=2, column=0, sticky="w", pady=8)
    email_entry = ttk.Entry(frame, width=30)
    email_entry.grid(row=2, column=1)

    ttk.Label(frame, text="Password").grid(row=3, column=0, sticky="w", pady=8)
    password_entry = ttk.Entry(frame, width=30, show="*")
    password_entry.grid(row=3, column=1)

    def signup():
        if validate_signup(
                username_entry.get(),
                email_entry.get(),
                password_entry.get()):
            signup_window.destroy()

    ttk.Button(
        frame,
        text="Signup",
        command=signup
    ).grid(row=4, column=0, columnspan=2, pady=20)

root = tk.Tk()
root.title("Student CGPA Manager")
root.geometry("900x600")
root.resizable(False, False)

# ttk Theme
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Heading.TLabel",
    font=("Segoe UI", 22, "bold")
)

style.configure(
    "TButton",
    font=("Segoe UI", 10)
)

style.configure(
    "TLabel",
    font=("Segoe UI", 11)
)

login_frame = ttk.Frame(root, padding=30)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

ttk.Label(
    login_frame,
    text="Student CGPA Manager",
    style="Heading.TLabel"
).grid(row=0, column=0, columnspan=2, pady=(0, 30))

ttk.Label(login_frame, text="Username").grid(
    row=1,
    column=0,
    sticky="w",
    pady=10
)

username_entry = ttk.Entry(login_frame, width=30)
username_entry.grid(row=1, column=1, padx=10)

ttk.Label(login_frame, text="Password").grid(
    row=2,
    column=0,
    sticky="w",
    pady=10
)

password_entry = ttk.Entry(login_frame, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10)

ttk.Button(
    login_frame,
    text="Login",
    command=lambda: handle_submit(
        username_entry.get(),
        password_entry.get()
    )
).grid(row=3, column=0, pady=25)

ttk.Button(
    login_frame,
    text="Signup",
    command=handle_signup_page
).grid(row=3, column=1)

root.mainloop()