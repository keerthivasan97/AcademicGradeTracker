import tkinter as tk
import storage

#validation semester data function
def sem_validation(sem,sgpa, credit):
    if sgpa == "" or credit == "" or sem == "":
        return False
    try:
        sgpa = float(sgpa)
        credit = float(credit)
        sem = int(sem)
        if sgpa < 0.0 or sgpa > 10.0 or sem <= 0 or sem > 8:
            raise ValueError("SGPA must be between 0.0 and 10.0.")
        elif credit <= 0.0 or credit > 30.0:
            raise ValueError("Credit hours must be a positive float.")
        else:
            return True
    except ValueError as e:
        tk.messagebox.showerror("Invalid Input", str(e))
        return False


def adds(sem,sgpa, credit, username):
    if sem_validation(sem,sgpa, credit):
        arr = {f"semester {sem}": {"gpa": sgpa, "credit": credit}}
        storage.add_sem(arr, username)
        tk.messagebox.showinfo("Success", "Semester data added successfully!")
    else:
        tk.messagebox.showinfo("Skipped", "Semester data skipped due to invalid input.")


def add_semester_data(username):
    # Implementation for adding semester data
    root = tk.Tk()
    root.withdraw()
    dashboard_win = tk.Toplevel(root)
    dashboard_win.title("Add Semester Data")
    dashboard_win.geometry("800x600")
    label = tk.Label(dashboard_win, text="Kindly enter your semester-wise GPA and credit hours.If the semester is not completed then leave the fields empty.", font=("Arial", 9))
    label.grid(pady=10)
    #semester data entry
    label = tk.Label(dashboard_win,text="semester:")
    label.grid(row=1,column=0,pady=5)
    sem = tk.Entry(dashboard_win)
    sem.grid(row=1,column=1,pady=5)

    label_1 = tk.Label(dashboard_win,text="semester gpa:")
    label_1.grid(row=2,column=0,pady=5)
    sgpa = tk.Entry(dashboard_win)
    sgpa.grid(row=2,column=1,pady=2)

    label1_1 = tk.Label(dashboard_win,text="semester credit hours:")
    label1_1.grid(row=3,column=0,pady=2)
    credit = tk.Entry(dashboard_win)
    credit.grid(row=3,column=1,pady=2)
    add = tk.Button(dashboard_win,text="Add Semester Data",bg="lightblue",fg="darkblue",command=lambda: adds(sem.get(),sgpa.get(), credit.get(), username))
    add.grid(row=4,column=0,columnspan=2,pady=10)
    dashboard_win.mainloop()
    root.mainloop()


def view_cgpa_data(username):
    pass


def show_dashboard(username):
    root = tk.Tk()
    root.withdraw()  
    dashboard_win = tk.Toplevel(root) #frame for the dashboard
    dashboard_win.title("Dashboard")
    dashboard_win.geometry("900x700")

    label = tk.Label(dashboard_win, text=f"Welcome to the Dashboard, {username}!", font=("Arial", 20), bg="lightblue", fg="darkblue")
    label.grid(pady=20)

    add_semester = tk.Button(dashboard_win, text="Add Semester Data", bg="lightblue", fg="darkblue",command = lambda:add_semester_data(username))
    add_semester.grid(row=1, column=0, padx=10, pady=10)

    view_cgpa = tk.Button(dashboard_win, text="View CGPA", bg="lightblue", fg="darkblue",command = lambda:view_cgpa_data(username))
    view_cgpa.grid(row=1, column=1, padx=10, pady=10)

    #logout button  

    tk.mainloop()