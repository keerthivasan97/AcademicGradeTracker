import tkinter as tk
from tkinter import messagebox
import storage
import re


#validate signup credentials
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
        messagebox.showinfo("Signup Failed", "Password must be at least 6 characters long and include at least one uppercase letter, one number, and one special character.")
        return False
    else:
        flag = storage.add_user(username, email, password)
        if flag == False:
            messagebox.showinfo("Signup Failed", "Username already exists.")
        else:
            messagebox.showinfo("Signup Successful", "You have successfully signed up!")
            return True


#event handler for login button
def handle_submit(username, password):
    if username == "":
        messagebox.showinfo("Login Failed", "Please enter your username.")
    elif password == "":
        messagebox.showinfo("Login Failed", "Please enter your password.")
    else:
        flag = storage.login_user(username, password)
        if flag == False:
            messagebox.showinfo("Login Failed", "Invalid username or password.")
        else:
            messagebox.showinfo("Login Successful", "You have successfully logged in!")


#event handler for signup button and the signup page
def handle_signup_page():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("400x300")

    label = tk.Label(signup_window, text="Signup Page", font=("Arial", 20), bg="lightblue", fg="darkblue")
    label.grid(row=0, column=0, columnspan=2, pady=20)
    #username label and entry
    username_label = tk.Label(signup_window, text="Username:")
    username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    username_entry = tk.Entry(signup_window)
    username_entry.grid(row=1, column=1, padx=10, pady=5)
    #email label and entry
    email_label = tk.Label(signup_window, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    email_entry = tk.Entry(signup_window)
    email_entry.grid(row=2, column=1, padx=10, pady=5)
    #password label and entry
    password_label = tk.Label(signup_window, text="Password:")
    password_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5)
    #signup button
    button_signup = tk.Button(signup_window, text="Signup", bg="lightblue", fg="darkblue",command=lambda: validate_signup(username_entry.get(), email_entry.get(), password_entry.get()))
    button_signup.grid(row=4, column=0, columnspan=2, pady=10)

# main login window and frame works
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