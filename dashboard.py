import tkinter as tk
from tkinter import messagebox
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
        messagebox.showerror("Invalid Input", str(e))
        return False


def adds(sem,sgpa, credit, username):
    if sem_validation(sem,sgpa, credit):
        arr = {f"semester {sem}": {"gpa": sgpa, "credit": credit}}
        storage.add_sem(arr, username)
        messagebox.showinfo("Success", "Semester data added successfully!")
    else:
        messagebox.showinfo("Skipped", "Semester data skipped due to invalid input.")

def pre_sgpa(username):
    pass

def calculate_cgpa(username):
    global Cgpa,view,add_sem

    if Cgpa is None:
        if add_sem is not None:
            add_sem.pack_forget()
            for widget in add_sem.winfo_children():
                widget.destroy()
            add_sem = None

        if view is not None:
            view.pack_forget()
            for widget in view.winfo_children():
                widget.destroy()
            view = None
        
        Cgpa = tk.Frame(root)
        sems = storage.get_user_data(username).get('semesters',{})
        if sems == {}:
            messagebox.showinfo("No Data", "No semester data found for the user.")
        else:
            tot_cre = 0
            tot_s =0
            cgpa = 0
            for i,(sem,data) in enumerate(sems.items()):
                tot_cre += float(data['credit'])
                tot_s += float(data['credit'])*float(data['gpa'])
            cgpa = float(tot_s/tot_cre)
            label = tk.Label(Cgpa,text = f"CGPA: {cgpa}", font= ("Arial",20))
            label.grid(row=0,column=0,padx=20,pady=20)
            Cgpa.pack()
    else:
        Cgpa.pack()

def view_semester_data(username):
    global view,add_sem,Cgpa
    if view is None:

        if add_sem is not None:
            add_sem.pack_forget() # Hide the add_sem frame if it exists
            for widget in add_sem.winfo_children():
                widget.destroy()
            add_sem = None

        if Cgpa is not None:
            Cgpa.pack_forget()
            for widget in Cgpa.winfo_children():
                widget.destroy()
            Cgpa = None

        view = tk.Frame(root)
        sems = storage.get_user_data(username).get('semesters', {})
        if sems == {}:
            messagebox.showinfo("No Data", "No semester data found for the user.")
        else:
            label1 = tk.Label(view,text="Semester",font=("Arial", 10, "bold"))
            label1.grid(row=0,column=0,pady=5)
            label2 = tk.Label(view,text="SGPA",font=("Arial", 10, "bold"))
            label2.grid(row=0,column=1,pady=5)
            label3 = tk.Label(view,text="Credit Hours",font=("Arial", 10, "bold"))
            label3.grid(row=0,column=2,pady=5)
            cgpa =0
            tot_credits=0
            
            for i, (sem, data) in enumerate(sems.items()):
                tk.Label(view, text=sem).grid(row=i+1, column=0, pady=5)
                tk.Label(view, text=data['gpa']).grid(row=i+1, column=1, pady=5)
                tk.Label(view, text=data['credit']).grid(row=i+1, column=2, pady=5)
                
            view.pack()
    else:
        view.pack() # Show the view frame if it already exists


def add_semester_data(username):
    global add_sem, view,Cgpa

    if add_sem is None:

        if view is not None:
            view.pack_forget() # Hide the view frame if it exists
            for widget in view.winfo_children():
                widget.destroy() # Clear the view frame content
            view = None

        if Cgpa is not None:
            Cgpa.pack_forget()
            for widget in Cgpa.winfo_children():
                widget.destroy()
            Cgpa = None

        add_sem = tk.Frame(root)
        label = tk.Label(add_sem, text="Kindly enter your semester-wise GPA and credit hours.If the semester is not completed then leave the fields empty.", font=("Arial", 9))
        label.grid(pady=10)
        #semester data entry
        label = tk.Label(add_sem,text="semester:")
        label.grid(row=1,column=0,pady=5)
        sem = tk.Entry(add_sem)
        sem.grid(row=1,column=1,pady=5)

        label_1 = tk.Label(add_sem,text="semester gpa:")
        label_1.grid(row=2,column=0,pady=5)
        sgpa = tk.Entry(add_sem)
        sgpa.grid(row=2,column=1,pady=2)

        label1_1 = tk.Label(add_sem,text="semester credit hours:")
        label1_1.grid(row=3,column=0,pady=2)
        credit = tk.Entry(add_sem)
        credit.grid(row=3,column=1,pady=2)
        add = tk.Button(add_sem,text="Add Semester Data",bg="lightblue",fg="darkblue",command=lambda: adds(sem.get(),sgpa.get(), credit.get(), username))
        add.grid(row=4,column=0,columnspan=2,pady=10)
        add_sem.pack()
    else:
        add_sem.pack() # Show the add_sem frame if it already exists


def show_dashboard(main_root,username):
    global root
    root = main_root
    root.title("Dashboard")
    root.geometry("900x700")

    dash_frame = tk.Frame(root) # frame for dashboard content

    label = tk.Label(dash_frame, text=f"Welcome to the Dashboard, {username}!",activebackground="lightblue", font=("Arial", 20), fg="darkblue")
    label.grid(row=0,column=0,columnspan = 4,padx=20, pady=20)

    add_semester = tk.Button(dash_frame, text="Add Semester Data", activebackground="lightblue", fg="darkblue", command=lambda: add_semester_data(username))
    add_semester.grid(row=1, column=0,padx=10,pady=10)

    view_sems = tk.Button(dash_frame, text="View Semester Data", activebackground="lightblue", fg="darkblue", command=lambda: view_semester_data(username))
    view_sems.grid(row=1, column=1,padx=10,pady=10)

    calcul_cgpa = tk.Button(dash_frame, text="Calculate CGPA", activebackground="lightblue", fg="darkblue", command=lambda: calculate_cgpa(username))
    calcul_cgpa.grid(row=1, column=2,padx=10,pady=10)

    predict_sgpa = tk.Button(dash_frame,text="Predict SGPA",activebackground = "Lightblue",fg="darkblue",command=lambda: pre_sgpa(username))
    predict_sgpa.grid(row=1,column=3,padx=10,pady=10)
    dash_frame.pack()

#global var 
root = None
add_sem = None
view = None
Grade = None
Cgpa = None