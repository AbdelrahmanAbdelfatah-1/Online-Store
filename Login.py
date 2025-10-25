import json
import tkinter as tk
from tkinter import messagebox
import time
import Register

def run_login() :

    try :
        with open("users.json", "r") as file :
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) :
        users = []

    root = tk.Tk()
    root.title("Login - Online Shopping System")
    root.state("zoomed")
    root.configure(bg="white")


    Purple = "#4e396e"

    frame = tk.Frame(root, bg="white", relief='raised', bd=2)
    frame.pack(expand=True, fill="both", padx=50, pady=50)

    tk.Label(frame, text="Welcome Back", font=("Arial", 24, "bold"), fg=Purple, background="white").pack(pady=10)
    tk.Label(frame, text="Sign in to your account", font=("Arial", 10), background="white").pack(pady=3)

    tk.Label(frame, text="Email Address", font=("Arial", 12, "bold"), anchor='w', background="white").pack(fill='x', padx=40, pady=20)
    user_email = tk.Entry(frame, font=("Arial", 12), width=30, background="white")
    user_email.pack(fill='x', padx=40, ipady=5)

    tk.Label(frame, text="Password", font=("Arial", 12, "bold"), anchor='w', background="white").pack(fill='x', padx=40, pady=20)
    user_password = tk.Entry(frame, font=("Arial", 12), show="*", width=30, background="white")
    user_password.pack(fill='x', padx=40, ipady=5)

    def check_login() :

        email = user_email.get().strip()
        password = user_password.get().strip()

        if not email or not password :
            messagebox.showwarning("Error", "Please enter both email and password")
            return

        user_found = None

        for user in users :

            if user["mail"] == email :
                user_found = user
                break

        if not user_found :
            messagebox.showerror("Error", "Invalid email or password\nPlease try again.")
            return

        if not user_found.get("Account_status") :
            messagebox.showerror("Account Locked", "Your account has been closed please call the customer services.")
            return

        lock_time = user_found.get("Lock_time")

        if lock_time :
            remaining_time = time.time() - lock_time
            if remaining_time < 35 :
                messagebox.showwarning("Locked",f"Your account is locked. Try again after {int(35 - remaining_time)} seconds.")
                user_email.delete(0, 'end')
                user_password.delete(0, 'end')
                return
            else :
                user_found["Lock_time"] = None
                user_found["Temp_failed_tries"] = 0

        if user_found["Password"] == password :

            if email == "admin@gmail.com" and password == "admin123" :
                messagebox.showinfo("Admin Login", "Welcome Admin")
                user_found["Temp_failed_tries"] = 0
                user_found["perm_failed_tries"] = 0
                root.destroy()
                import admin
                admin.run_admin()
                return

            messagebox.showinfo("Login Successful", f"Welcome {user_found['name']}")
            user_found["Temp_failed_tries"] = 0
            user_found["perm_failed_tries"] = 0

            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

            root.destroy()

            from pages_maneger import pages_manager_fun
            pages_manager_fun(user_found)

        else :

            messagebox.showerror("Error", "Wrong password")

            user_email.delete(0, 'end')
            user_password.delete(0, 'end')

            user_found["Temp_failed_tries"] = user_found.get("Temp_failed_tries") + 1
            user_found["perm_failed_tries"] = user_found.get("perm_failed_tries") + 1

            if user_found["Temp_failed_tries"] >= 3 :
                user_found["Lock_time"] = time.time()

            if user_found["perm_failed_tries"] >= 10 :
                user_found["Account_status"] = False
                messagebox.showerror("Account Closed","Your account has been permanently locked due to too many failed attempts.")

            with open("users.json", "w") as f :
                json.dump(users, f, indent=4)

    def open_reg() :

        root.destroy()
        Register.run_register()

    tk.Button(frame, text='Sign In', font=("Arial", 10, "bold"), fg="white", width=15,
              command=check_login, background=Purple).pack(pady=20, ipady=3)

    tk.Label(frame, text="Don't have an account ?", font=("Arial", 11), background="white").pack()
    tk.Button(frame, text='Create Account', font=("Arial", 11, "bold"), fg=Purple, bg="white",
              relief='flat', bd=0, activeforeground=Purple, activebackground="white",
              command=open_reg).pack()

    root.mainloop()