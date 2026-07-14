import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import storage

def _setup_styles():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Heading.TLabel",
        font=("Segoe UI", 22, "bold"),
        foreground="#5e82c6"
    )

    style.configure(
        "SubHeading.TLabel",
        font=("Segoe UI", 13, "bold"),
        foreground="#31569b"
    )

    style.configure(
        "TLabel",
        font=("Segoe UI", 11)
    )

    style.configure(
        "Hint.TLabel",
        font=("Segoe UI", 9),
        foreground="#645555"
    )

    style.configure(
        "TButton",
        font=("Segoe UI", 10),
        padding=8
    )

    style.configure(
        "Accent.TButton",
        font=("Segoe UI", 10, "bold"),
        padding=10
    )
    style.map(
        "Accent.TButton",
        foreground=[("!disabled", "#ffffff")],
        background=[("!disabled", "#1a73e8"), ("active", "#155ab6")]
    )

    style.configure(
        "Card.TFrame",
        background="#f7f9fc",
        relief="flat"
    )

    style.configure(
        "TEntry",
        padding=6
    )

    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold")
    )
    style.configure(
        "Treeview",
        font=("Segoe UI", 10),
        rowheight=26
    )

    style.configure("TCombobox", padding=4)


def sem_validation(sem, sgpa, credit):
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


def adds(sem, sgpa, credit, username):
    if sem_validation(sem, sgpa, credit):
        arr = {f"semester {sem}": {"gpa": sgpa, "credit": credit}}
        storage.add_sem(arr, username)
        messagebox.showinfo("Success", "Semester data added successfully!")
    else:
        messagebox.showinfo("Skipped", "Semester data skipped due to invalid input.")


def calcul(arr):
    grade_p = {
        "S": 10,
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6,
        "E": 5,
        "F": 0
    }
    total_point = 0
    total_credit = 0
    for g, c in arr:
        grade = g.get()
        credit = c.get()
        if grade == "--select--" or credit == "--select--":
            continue
        credit = float(credit)
        point = grade_p[grade]

        total_point += point * credit
        total_credit += credit

    if total_credit == 0:
        messagebox.showerror("Error", "Please select at least one subject.")
        return

    sgpa = total_point / total_credit
    messagebox.showinfo("Predicted SGPA", f"Predicted SGPA: {sgpa:.2f}")


def select(event):
    combo = event.widget
    print(combo.get())


def _clear_frame(frame):
    """Destroy all children of a frame and hide it."""
    if frame is not None:
        frame.pack_forget()
        for widget in frame.winfo_children():
            widget.destroy()
    return None


def pre_sgpa(username):
    global Cgpa, view, add_sem, grade

    if grade is None:
        add_sem = _clear_frame(add_sem)
        view = _clear_frame(view)
        Cgpa = _clear_frame(Cgpa)

        grade = ttk.Frame(root, style="Card.TFrame", padding=25)

        heading = ttk.Label(grade, text="Predict Your SGPA", style="SubHeading.TLabel")
        heading.grid(row=0, column=0, columnspan=4, pady=(0, 15), sticky="w")

        ttk.Label(grade, text="Grade", style="Hint.TLabel").grid(row=1, column=0, padx=10)
        ttk.Label(grade, text="Credit", style="Hint.TLabel").grid(row=1, column=2, padx=10)

        arr = []
        for i in range(10):
            g = ttk.Combobox(
                grade,
                values=["--select--", "S", "A", "B", "C", "D", "E", "F"],
                state="readonly",
                width=12
            )
            g.grid(row=i + 2, column=0, columnspan=2, padx=10, pady=4, sticky="ew")
            g.set("--select--")
            g.bind("<<ComboboxSelected>>", select)

            c = ttk.Combobox(
                grade,
                values=["--select--", "1", "1.5", "2", "3", "4", "5"],
                state="readonly",
                width=12
            )
            c.grid(row=i + 2, column=2, columnspan=2, padx=10, pady=4, sticky="ew")
            c.set("--select--")
            c.bind("<<ComboboxSelected>>", select)

            arr.append([g, c])

        btn = ttk.Button(grade, text="Calculate", style="Accent.TButton",
                          command=lambda: calcul(arr))
        btn.grid(row=12, column=0, columnspan=4, pady=(15, 0), sticky="ew")
        grade.pack(pady=20)
    else:
        grade.pack(pady=20)


def calculate_cgpa(username):
    global Cgpa, view, add_sem, grade

    if Cgpa is None:
        add_sem = _clear_frame(add_sem)
        grade = _clear_frame(grade)
        view = _clear_frame(view)

        Cgpa = ttk.Frame(root, style="Card.TFrame", padding=30)
        sems = storage.get_user_data(username).get('semesters', {})
        if sems == {}:
            messagebox.showinfo("No Data", "No semester data found for the user.")
        else:
            tot_cre = 0
            tot_s = 0
            for i, (sem, data) in enumerate(sems.items()):
                tot_cre += float(data['credit'])
                tot_s += float(data['credit']) * float(data['gpa'])
            cgpa = float(tot_s / tot_cre)

            heading = ttk.Label(Cgpa, text="Your Overall CGPA", style="SubHeading.TLabel")
            heading.grid(row=0, column=0, pady=(0, 10))

            label = ttk.Label(Cgpa, text=f"{cgpa:.2f}", style="Heading.TLabel")
            label.grid(row=1, column=0, padx=20, pady=10)

            Cgpa.pack(pady=40)
    else:
        Cgpa.pack(pady=40)


def view_semester_data(username):
    global view, add_sem, Cgpa, grade

    if view is None:
        add_sem = _clear_frame(add_sem)
        grade = _clear_frame(grade)
        Cgpa = _clear_frame(Cgpa)

        view = ttk.Frame(root, style="Card.TFrame", padding=25)

        sems = storage.get_user_data(username).get("semesters", {})

        if sems == {}:
            messagebox.showinfo("No Data", "No semester data found for the user.")
            view = None
            return

        heading = ttk.Label(
            view,
            text="Semester Records",
            style="SubHeading.TLabel"
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

        tree.column("Semester", width=180, anchor="center")
        tree.column("SGPA", width=120, anchor="center")
        tree.column("Credits", width=140, anchor="center")

        for sem, data in sems.items():
            tree.insert(
                "",
                tk.END,
                values=(sem, data["gpa"], data["credit"])
            )

        tree.pack()

        view.pack(pady=20)

    else:
        view.pack(pady=20)


def add_semester_data(username):
    global add_sem, view, Cgpa, grade

    if add_sem is None:
        view = _clear_frame(view)
        grade = _clear_frame(grade)
        Cgpa = _clear_frame(Cgpa)

        add_sem = ttk.Frame(root, style="Card.TFrame", padding=30)

        heading = ttk.Label(add_sem, text="Add Semester Data", style="SubHeading.TLabel")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

        label = ttk.Label(
            add_sem,
            text="Enter your semester-wise GPA and credit hours.\n"
                 "If the semester is not completed, leave the fields empty.",
            style="Hint.TLabel",
            justify="left"
        )
        label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="w")

        ttk.Label(add_sem, text="Semester").grid(row=2, column=0, sticky="w", pady=8)
        sem = ttk.Entry(add_sem, width=25)
        sem.grid(row=2, column=1, pady=8)

        ttk.Label(add_sem, text="Semester GPA").grid(row=3, column=0, sticky="w", pady=8)
        sgpa = ttk.Entry(add_sem, width=25)
        sgpa.grid(row=3, column=1, pady=8)

        ttk.Label(add_sem, text="Semester Credit Hours").grid(row=4, column=0, sticky="w", pady=8)
        credit = ttk.Entry(add_sem, width=25)
        credit.grid(row=4, column=1, pady=8)

        add = ttk.Button(
            add_sem,
            text="Add Semester Data",
            style="Accent.TButton",
            command=lambda: adds(sem.get(), sgpa.get(), credit.get(), username)
        )
        add.grid(row=5, column=0, columnspan=2, pady=(20, 0), sticky="ew")

        add_sem.pack(pady=30)
    else:
        add_sem.pack(pady=30)


def show_dashboard(main_root, username):
    global root
    root = main_root
    root.title("Dashboard")
    root.geometry("900x700")
    root.resizable(False, False)

    _setup_styles()

    dash_frame = ttk.Frame(root, padding=30)

    label = ttk.Label(
        dash_frame,
        text=f"Welcome back, {username}!",
        style="Heading.TLabel"
    )
    label.grid(row=0, column=0, columnspan=4, padx=20, pady=(0, 25))

    add_semester = ttk.Button(
        dash_frame, text="Add Semester Data", style="TButton",
        command=lambda: add_semester_data(username)
    )
    add_semester.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    view_sems = ttk.Button(
        dash_frame, text="View Semester Data", style="TButton",
        command=lambda: view_semester_data(username)
    )
    view_sems.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    calcul_cgpa = ttk.Button(
        dash_frame, text="Calculate CGPA", style="TButton",
        command=lambda: calculate_cgpa(username)
    )
    calcul_cgpa.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    predict_sgpa = ttk.Button(
        dash_frame, text="Predict SGPA", style="TButton",
        command=lambda: pre_sgpa(username)
    )
    predict_sgpa.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

    dash_frame.pack()

root = None
add_sem = None
view = None
grade = None
Cgpa = None