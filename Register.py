import tkinter as tk
from tkinter import messagebox, ttk
import json
import Login

def register(root) :
    try:
        with open("users.json", "r") as file :
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    if governorate_cb.get() == "Select Governorate":
        messagebox.showwarning("Warning", "Please select a Governorate")
        return
    if gender_cb.get() == "Select Gender":
        messagebox.showwarning("Warning", "Please select a Gender")
        return
    if entries["Password"].get() != entries["Confirm password"].get():
        messagebox.showwarning("Warning", "Passwords do not match!")
        return
    for field, entry in entries.items():
        if entry.get().strip() == "":
            messagebox.showwarning("Warning", f"Please fill the {field}")
            return

    user = {
        "state": "user",
        "name": entries["Name"].get(),
        "phone": entries["Phone"].get(),
        "mail": entries["Mail"].get(),
        "Governorate": governorate_cb.get(),
        "Gender": gender_cb.get(),
        "Age": entries["Age"].get(),
        "Password": entries["Password"].get(),
        "National ID": entries["National ID"].get(),
        "Account_status": True,
        "Temp_failed_tries": 0,
        "perm_failed_tries": 0,
        "Lock_time": None
    }

    users.append(user)
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    messagebox.showinfo("Success", "Registered successfully!")
    root.destroy()
    Login.run_login()

def run_register():
    root = tk.Tk()
    root.title("Register Page")
    root.state("zoomed")

    frame = tk.Frame(root, bg="white", relief='raised', bd=2)
    frame.pack(expand=True, fill="both", padx=50, pady=50)

    tk.Label(frame, text="Create Account", font=("Arial", 18, "bold"),
             fg="#4e396e", bg="white").grid(row=0, column=0, columnspan=2, pady=(10, 5))

    tk.Label(frame, text="Join our community today", font=("Arial", 12),
             fg="#555555", bg="white").grid(row=1, column=0, columnspan=2, pady=(0, 20))

    fields = ["Name", "Phone", "Mail", "Age", "Password", "Confirm password", "National ID"]
    global entries, governorate_cb, gender_cb
    entries = {}
    rows = 2

    for field in fields :

        tk.Label(frame, text=field, font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(
            row=rows, column=0, sticky="w", padx=10, pady=5
        )
        if field in ["Password", "Confirm password"]:
            entry = tk.Entry(frame, show="*", relief='solid', bd=2, font=("Arial", 12), width=30)
        else:
            entry = tk.Entry(frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        entry.grid(row=rows, column=1, padx=10, pady=5, sticky="ew")
        entries[field] = entry
        rows += 1

    tk.Label(frame, text="Governorate", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(
        row=rows, column=0, sticky="w", padx=10, pady=5
    )
    governorate_cb = ttk.Combobox(frame, values=[
        "Select Governorate", "Cairo", "Alexandria", "Giza", "Luxor", "Aswan", "Asyut"
    ], font=("Arial", 12), width=28, state="readonly")
    governorate_cb.current(0)
    governorate_cb.grid(row=rows, column=1, padx=10, pady=5, sticky="ew")
    rows += 1

    tk.Label(frame, text="Gender", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(
        row=rows, column=0, sticky="w", padx=10, pady=5
    )
    gender_cb = ttk.Combobox(frame, values=["Select Gender", "Female", "Male"],
                             font=("Arial", 12), width=28, state="readonly")
    gender_cb.current(0)
    gender_cb.grid(row=rows, column=1, padx=10, pady=5, sticky="ew")
    rows += 1

    register_btn = tk.Button(frame, text="Register", font=("Arial", 15, "bold"), fg="white",
                             bg="#4e396e", relief="flat", cursor="hand2",
                             command=lambda: register(root))
    register_btn.grid(row=rows, column=0, columnspan=2, pady=20)

    frame.grid_columnconfigure(0, weight=0)
    frame.grid_columnconfigure(1, weight=1)

    root.mainloop()