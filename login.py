import tkinter as tk
from tkinter import messagebox

def handle_submit(username, password):
    if username == "" and password == "":
        messagebox.showinfo("Login Failed", "Please enter both username and password.")
    elif username == "":
        messagebox.showinfo("Login Failed", "Please enter your username.")
    elif password == "":
        messagebox.showinfo("Login Failed", "Please enter your password.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        messagebox.showinfo("login Failed","please signup to create an account")



def handle_signup_page():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("400x300")

    label = tk.Label(signup_window, text="Signup Page", font=("Arial", 20), bg="lightblue", fg="darkblue")
    label.grid(row=0, column=0, columnspan=2, pady=20)

    username_label = tk.Label(signup_window, text="Username:")
    username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    username_entry = tk.Entry(signup_window)
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    email_label = tk.Label(signup_window, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    email_entry = tk.Entry(signup_window)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    password_label = tk.Label(signup_window, text="Password:")
    password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5)

    button_signup = tk.Button(signup_window, text="Signup", bg="lightblue", fg="darkblue")
    button_signup.grid(row=4, column=0, columnspan=2, pady=10)

root = tk.Tk()
login_frame = tk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.geometry("600x400")

title_label = tk.Label(login_frame, text="Welcome to the login page", font=("Arial", 30),bg="lightgreen", fg="lightyellow")
title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=20)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=5)


password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

button1 = tk.Button(login_frame,text="login",bg="lightblue", fg="darkblue",command=lambda: handle_submit(username_entry.get(), password_entry.get()))
button1.grid(row=3,column=0, padx=10, pady=5)


button2 = tk.Button(login_frame,text="signup",command=handle_signup_page,bg="lightblue", fg="darkblue")
button2.grid(row=3,column=1, padx=10, pady=5)
root.mainloop()