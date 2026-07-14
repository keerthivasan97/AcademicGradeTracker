import tkinter as tk
from tkinter import ttk
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

def calcul(arr):
    grade_p = {
        "S":10,
        "A":9,
        "B":8,
        "C":7,
        "D":6,
        "E":5,
        "F":0
    }
    total_point=0
    total_credit=0
    for g,c in arr:
        grade = g.get()
        credit=c.get()
        if grade == "--select--" or credit == "--select--":
            continue
        credit = float(credit)
        point = grade_p[grade]

        total_point += point*credit
        total_credit +=credit

    if total_credit == 0:
        messagebox.showerror("Error", "Please select at least one subject.")
        return

    sgpa = total_point / total_credit
    messagebox.showinfo("Predicted SGPA", f"Predicted SGPA: {sgpa:.2f}")

def select(event):
    combo = event.widget
    print(combo.get())

def pre_sgpa(username):
    global Cgpa,view,add_sem,grade

    if grade is None:
        grade = ttk.Frame(root, padding=25)

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

        if Cgpa is not None:
            Cgpa.pack_forget()
            for widget in Cgpa.winfo_children():
                widget.destroy()
            Cgpa = None
        arr = []

        for i in range(10):
            ttk.Label(grade,text="grade").grid(row=i,column=0,padx=10,pady=4)

            g = ttk.Combobox(grade,values=["--select--","S","A", "B", "C","D","E","F"],state="readonly")
            g.grid(row=i,column=1,padx=10,pady=4)
            g.set("--select--")
            g.bind("<<ComboboxSelected>>", select)

            ttk.Label( grade,text="credit").grid(row=i,column=2,padx=10,pady=4)

            c = ttk.Combobox(grade,values=["--select--","1", "1.5", "2","3","4","5"],state="readonly")
            c.grid(row=i,column=3,padx=10,pady=4)
            c.set("--select--")
            c.bind("<<ComboboxSelected>>", select)

            arr.append([g,c])
            

        btn = ttk.Button(grade,text = "calculate",command=lambda:calcul(arr))
        btn.grid(row=11,column=2,pady=15)
        grade.pack(pady=20)
    else:
        grade.pack(pady=20)




def calculate_cgpa(username):
    global Cgpa,view,add_sem,grade

    if Cgpa is None:
        if add_sem is not None:
            add_sem.pack_forget()
            for widget in add_sem.winfo_children():
                widget.destroy()
            add_sem = None
        if grade is not None:
            grade.pack_forget()
            for w in grade.winfo_children():
                w.destroy()
            grade = None

        if view is not None:
            view.pack_forget()
            for widget in view.winfo_children():
                widget.destroy()
            view = None
        
        Cgpa = ttk.Frame(root, padding=30)
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
            label = ttk.Label(Cgpa,text = f"CGPA: {cgpa:.2f}", font= ("Segoe UI",22,"bold"))
            label.grid(row=0,column=0,padx=20,pady=20)
            Cgpa.pack(pady=40)
    else:
        Cgpa.pack()


def view_semester_data(username):
    global view, add_sem, Cgpa, grade

    if view is None:

        if add_sem is not None:
            add_sem.pack_forget()
            for widget in add_sem.winfo_children():
                widget.destroy()
            add_sem = None

        if grade is not None:
            grade.pack_forget()
            for widget in grade.winfo_children():
                widget.destroy()
            grade = None

        if Cgpa is not None:
            Cgpa.pack_forget()
            for widget in Cgpa.winfo_children():
                widget.destroy()
            Cgpa = None

        view = ttk.Frame(root, padding=20)

        sems = storage.get_user_data(username).get("semesters", {})

        if sems == {}:
            messagebox.showinfo("No Data", "No semester data found for the user.")
            return

        heading = ttk.Label(
            view,
            text="Semester Records",
            font=("Segoe UI", 16, "bold")
        )
        heading.pack(pady=(0, 15))

        tree = ttk.Treeview(
            view,
            columns=("Semester", "SGPA", "Credits"),
            show="headings",
            height=8
        )

        tree.heading("Semester", text="Semester")
        tree.heading("SGPA", text="SGPA")
        tree.heading("Credits", text="Credit Hours")

        tree.column("Semester", width=150, anchor="center")
        tree.column("SGPA", width=100, anchor="center")
        tree.column("Credits", width=120, anchor="center")

        for sem, data in sems.items():
            tree.insert(
                "",
                tk.END,
                values=(sem, data["gpa"], data["credit"])
            )

        tree.pack()

        view.pack(pady=20)

    else:
        view.pack()

def add_semester_data(username):
    global add_sem, view,Cgpa,grade

    if add_sem is None:

        if view is not None:
            view.pack_forget() # Hide the view frame if it exists
            for widget in view.winfo_children():
                widget.destroy() # Clear the view frame content
            view = None

        if grade is not None:
            grade.pack_forget()
            for w in grade.winfo_children():
                w.destroy()
            grade = None
            
        if Cgpa is not None:
            Cgpa.pack_forget()
            for widget in Cgpa.winfo_children():
                widget.destroy()
            Cgpa = None

        add_sem = ttk.Frame(root, padding=30)
        label = ttk.Label(add_sem, text="Kindly enter your semester-wise GPA and credit hours.If the semester is not completed then leave the fields empty.", font=("Segoe UI", 9))
        label.grid(pady=10)
        #semester data entry
        label = ttk.Label(add_sem,text="semester:")
        label.grid(row=1,column=0,pady=5)
        sem = ttk.Entry(add_sem)
        sem.grid(row=1,column=1,pady=5)

        label_1 = ttk.Label(add_sem,text="semester gpa:")
        label_1.grid(row=2,column=0,pady=5)
        sgpa = ttk.Entry(add_sem)
        sgpa.grid(row=2,column=1,pady=2)

        label1_1 = ttk.Label(add_sem,text="semester credit hours:")
        label1_1.grid(row=3,column=0,pady=2)
        credit = ttk.Entry(add_sem)
        credit.grid(row=3,column=1,pady=2)
        add = ttk.Button(add_sem,text="Add Semester Data",command=lambda: adds(sem.get(),sgpa.get(), credit.get(), username))
        add.grid(row=4,column=0,columnspan=2,pady=10)
        add_sem.pack()
    else:
        add_sem.pack() # Show the add_sem frame if it already exists


def show_dashboard(main_root,username):
    global root
    root = main_root
    root.title("Dashboard")
    root.geometry("900x700")
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Heading.TLabel", font=("Segoe UI", 22, "bold"))
    style.configure("TButton", font=("Segoe UI", 10))
    style.configure("TLabel", font=("Segoe UI", 11))

    dash_frame = ttk.Frame(root, padding=30) # frame for dashboard content

    label = ttk.Label(dash_frame, text=f"Welcome to the Dashboard, {username}!", style="Heading.TLabel")
    label.grid(row=0,column=0,columnspan = 4,padx=20, pady=(0, 30))

    add_semester = ttk.Button(dash_frame, text="Add Semester Data", command=lambda: add_semester_data(username))
    add_semester.grid(row=1, column=0,padx=10,pady=10)

    view_sems = ttk.Button(dash_frame, text="View Semester Data", command=lambda: view_semester_data(username))
    view_sems.grid(row=1, column=1,padx=10,pady=10)

    calcul_cgpa = ttk.Button(dash_frame, text="Calculate CGPA", command=lambda: calculate_cgpa(username))
    calcul_cgpa.grid(row=1, column=2,padx=10,pady=10)

    predict_sgpa = ttk.Button(dash_frame,text="Predict SGPA",command=lambda: pre_sgpa(username))
    predict_sgpa.grid(row=1,column=3,padx=10,pady=10)
    dash_frame.pack()
    
#global var 
root = None
add_sem = None
view = None
grade = None
Cgpa = None