import tkinter as tk
root = tk.Tk()
login_frame = tk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.geometry("600x400")

title_label = tk.Label(login_frame, text="Welcome to the login page", font=("Arial", 24),bg="lightblue", fg="darkblue")
title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=20)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=5)


password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

button1 = tk.Button(login_frame,text="login",bg="lightblue", fg="darkblue")
button1.grid(row=3,column=0, padx=10, pady=5)
button2 = tk.Button(login_frame,text="signup",bg="lightblue", fg="darkblue")
button2.grid(row=3,column=1, padx=10, pady=5)
root.mainloop()