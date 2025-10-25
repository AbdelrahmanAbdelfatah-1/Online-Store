import tkinter as tk
from tkinter import ttk, messagebox
from pages_maneger import Stack, Purple

import json

FILE = "products.json"

stack = Stack()

def run_admin() :

    def open_add_items() :

        add_pg = tk.Toplevel()
        add_pg.title("Add Items")
        add_pg.state("zoomed")
        add_pg.configure(bg="#f0f0f0")

        stack.push(add_pg)

        main_frame = tk.Frame(add_pg, bg="white", relief='raised', bd=2)
        main_frame.pack(fill='both', expand=True, padx=30, pady=10)

        header_frame = tk.Frame(main_frame, bg="white")
        header_frame.grid(row=0, column=0,pady=10)
        back_button = tk.Button(header_frame, text=" ← Back ", font=("Arial", 15, "bold"),
                                fg=Purple, bg="white", relief='flat', cursor='hand2',
                                command=stack.pop)
        back_button.pack(side="left", padx=20)

        tk.Label(main_frame, text="Add New Product", font=("Arial", 24, "bold"),
                 fg="#4e396e", bg="white").grid(row=0, column=0, columnspan=2, pady=(20, 40))

        tk.Label(main_frame, text="Fill in the details below",
                 font=("Arial", 16, "bold"),
                 fg="#4e396e", bg="white").grid(row=2, column=0, columnspan=2, pady=(20, 30))

        tk.Label(main_frame, text="Category",font=("Arial", 14,"bold"), bg="white", fg="#333333",  anchor="w").grid(
            row=3, column=0, sticky="w", padx=10, pady=20,
        )

        category_type = ttk.Combobox(main_frame, values=["HomeAppliances", "Books", "Fashion", "Sports", "Electronics"],
                                     state="readonly", font=("Arial", 12) )
        category_type.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

        tk.Label(main_frame, text="Name:",font=("Arial", 14,"bold"), bg="white", fg="#333333",anchor="w").grid()
        name_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        name_entry.grid(row=4, column=1, padx=10, pady=20, sticky="ew")

        tk.Label(main_frame, text="Price:",font=("Arial", 14,"bold"), bg="white", fg="#333333", anchor="w").grid()
        price_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        price_entry.grid(row=5, column=1, padx=10, pady=20, sticky="ew")

        tk.Label(main_frame, text="Brand:",font=("Arial", 14,"bold"), bg="white", fg="#333333", anchor="w").grid()
        brand_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        brand_entry.grid(row=6, column=1, padx=10, pady=20, sticky="ew")

        tk.Label(main_frame, text="Year:",font=("Arial", 14,"bold"), bg="white", fg="#333333",  anchor="w").grid()
        year_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        year_entry.grid(row=7, column=1, padx=10, pady=20, sticky="ew")

        tk.Label(main_frame, text="Description:",font=("Arial", 14,"bold"), bg="white", fg="#333333", anchor="w").grid()
        desc_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        desc_entry.grid(row=8, column=1, padx=10, pady=20, sticky="ew")

        tk.Label(main_frame, text="Stock:",font=("Arial", 14,"bold"), bg="white", fg="#333333", anchor="w").grid()
        stock_entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
        stock_entry.grid(row=9, column=1, padx=10, pady=20, sticky="ew")

        main_frame.columnconfigure(1, weight=1)


        def add_product() :
            category = category_type.get()
            if not category :
                messagebox.showerror("Error", "Please select a category")
                return
            try:
                price = int(price_entry.get())
                year = int(year_entry.get())
                stock = int(stock_entry.get())
            except ValueError :
                messagebox.showerror("Error", "Price, Year, and Stock must be numbers")
                return

            try :
                with open(FILE, "r") as f :
                    data = json.load(f)
            except :
                data = {}

            if category not in data:
                data[category] = []

            cat_ids = []
            for product in data.get(category, []) :
                cat_ids.append(product["id"])

            if len(cat_ids) == 0 :
                new_id = 1
            else :
                new_id = max(cat_ids) + 1

            new_product = {
                "id": new_id,
                "name": name_entry.get(),
                "price": int(price_entry.get()),
                "brand": brand_entry.get(),
                "model year": int(year_entry.get()),
                "description": desc_entry.get(),
                "stock": int(stock_entry.get())
            }
            data[category].append(new_product)

            with open(FILE, "w") as f :
                json.dump(data, f, indent=2)

            messagebox.showinfo("Success", f"Product added to {category}")


        tk.Button(main_frame, text="Add Product", font=("Arial", 14, "bold"), bg="#4e396e", fg="white", bd=3, relief="raised",padx=50,
        pady=10, command=add_product).grid(row=10, column=0, columnspan=2, pady=(20, 40))

    def open_update_items() :

        update_pg = tk.Toplevel()
        update_pg.title("Update Items")
        update_pg.state("zoomed")
        update_pg.configure(bg="#f0f0f0")

        stack.push(update_pg)

        main_frame = tk.Frame(update_pg, bg="white", relief='raised', bd=2)
        main_frame.pack(fill='both', expand=True, padx=30, pady=10)

        header_frame = tk.Frame(main_frame, bg="white")
        header_frame.grid(row=0, column=0, pady=10)
        back_button = tk.Button(header_frame, text=" ← Back ", font=("Arial", 15, "bold"),
                                fg=Purple, bg="white", relief='flat', cursor='hand2',
                                command=stack.pop)
        back_button.pack(side="left", padx=20)


        tk.Label(main_frame, text="Update Product", font=("Arial", 24, "bold"),
                 fg="#4e396e", bg="white").grid(row=0, column=0, columnspan=2, pady=(20, 40))
        tk.Label(main_frame, text="Select category and product to update", font=("Arial", 16, "bold"),
                 fg="#4e396e", bg="white").grid(row=1, column=0, columnspan=2, pady=(0, 30))

        categories = ["HomeAppliances", "Books", "Fashion", "Sports", "Electronics"]
        tk.Label(main_frame, text="Category:", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        category_cb = ttk.Combobox(main_frame, values=categories, state="readonly", font=("Arial", 12))
        category_cb.grid(row=2, column=1, padx=20, pady=10, sticky="ew")
        tk.Label(main_frame, text="Product:", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        product_cb = ttk.Combobox(main_frame, state="readonly", font=("Arial", 12))
        product_cb.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        fields = ["Name", "Price", "Brand", "model year", "Description", "Stock"]
        entries = {}
        for i, field in enumerate(fields) :
            tk.Label(main_frame, text=f"{field}:", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(row=4+i, column=0, sticky="w", padx=10, pady=10)
            entry = tk.Entry(main_frame, relief='solid', font=("Arial", 12), bd=2, width=30)
            entry.grid(row=4+i, column=1, padx=10, pady=10, sticky="ew")
            entries[field] = entry

        main_frame.columnconfigure(1, weight=1)

        def load_products(event) :
            category = category_cb.get()
            try :
                with open(FILE, "r") as f:
                    data = json.load(f)
                product_list = []

                for product in data.get(category, []):
                    product_list.append(product["name"])

                product_cb["values"] = product_list
                product_cb.set("no items")

                for e in entries.values():
                    e.delete(0, tk.END)

            except :

                product_cb["values"] = []
                for e in entries.values():
                    e.delete(0, tk.END)

        category_cb.bind("<<ComboboxSelected>>", load_products)

        def load_product_details(event) :

            category = category_cb.get()
            product_name = product_cb.get()

            with open(FILE, "r") as f :
                data = json.load(f)

            product_data = None

            for p in data.get(category, [])  :

                if p["name"] == product_name :
                    product_data = p
                    break

            if product_data :
                for field in fields :
                    entries[field].delete(0, tk.END)
                    key = field.lower()
                    if key in product_data:
                        entries[field].insert(0, str(product_data[key]))

        product_cb.bind("<<ComboboxSelected>>", load_product_details)


        def save_changes() :
            category = category_cb.get()
            product_name = product_cb.get()
            if not category or  product_name == "no items":
                messagebox.showerror("Error", "Select a category and product")
                return
            with open(FILE, "r") as f:
                data = json.load(f)
            product_data = next((p for p in data.get(category, []) if p["name"] == product_name), None)
            if product_data:
                try :
                    product_data["name"] = entries["Name"].get()
                    product_data["price"] = float(entries["Price"].get())
                    product_data["brand"] = entries["Brand"].get()
                    product_data["model year"] = int(entries["model year"].get())
                    product_data["description"] = entries["Description"].get()
                    product_data["stock"] = int(entries["Stock"].get())
                except ValueError:
                    messagebox.showerror("Error", "Price, Year, and Stock must be numbers")
                    return

                with open(FILE, "w") as f:
                    json.dump(data, f, indent=2)
                messagebox.showinfo("Success", f"Product '{product_data['name']}' updated successfully!")

        tk.Button(main_frame, text="Save Changes", font=("Arial", 14, "bold"), bg="#4e396e",
                  fg="white", bd=3, relief="raised", command=save_changes).grid(row=10, column=0, columnspan=2,
                                                                                pady=(20, 40))

    def open_discount_items() :

        discount_pg = tk.Toplevel()
        discount_pg.title("Make Discount")
        discount_pg.state("zoomed")
        discount_pg.configure(bg="#f0f0f0")

        stack.push(discount_pg)

        main_frame = tk.Frame(discount_pg, bg="white", relief='raised', bd=2)
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)

        header_frame = tk.Frame(main_frame, bg="white")
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=10)  # خلي frame يتمدد أفقياً

        back_button = tk.Button(header_frame, text=" ← Back ", font=("Arial", 15, "bold"),
                                fg=Purple, bg="white", relief='flat', cursor='hand2',
                                command=stack.pop)
        back_button.pack(side="left", padx=0)

        tk.Label(main_frame, text="Make Discount", font=("Arial", 20, "bold"),
                 fg="#4e396e", bg="white").grid(row=0, column=0, columnspan=2, pady=(20, 30))

        categories = ["HomeAppliances", "Books", "Fashion", "Sports", "Electronics"]
        tk.Label(main_frame, text="Category:", font=("Arial", 14), fg="#333333", bg="white").grid(row=1, column=0,sticky="w", padx=10,pady=10)
        category_cb = ttk.Combobox(main_frame, values=categories, state="readonly", font=("Arial", 12))
        category_cb.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        tk.Label(main_frame, text="Product:", font=("Arial", 14), fg="#333333", bg="white").grid(row=2, column=0,sticky="w", padx=10,pady=10)
        product_cb = ttk.Combobox(main_frame, state="readonly", font=("Arial", 12))
        product_cb.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        tk.Label(main_frame, text="Discount ( % ) :", font=("Arial", 14), fg="#333333", bg="white").grid(row=3,column=0,sticky="w",pady=10)
        discount_entry = tk.Entry(main_frame, font=("Arial", 12), relief='solid', bd=2)
        discount_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        main_frame.columnconfigure(1, weight=1)


        def load_products(event):
            category = category_cb.get()
            try:
                with open(FILE, "r") as f:
                    data = json.load(f)
                product_list = [p["name"] for p in data.get(category, [])]
                product_cb["values"] = product_list
                product_cb.set("no items")
            except:
                product_cb["values"] = []
                product_cb.set("no items")

        category_cb.bind("<<ComboboxSelected>>", load_products)


        def apply_discount():
            category = category_cb.get()
            product_name = product_cb.get()
            discount_value = discount_entry.get()
            if not category or product_name == "no items" or not discount_value:
                messagebox.showerror("Error", "Please select category, product and enter discount")
                return

            try:
                discount = float(discount_value)
            except ValueError:
                messagebox.showerror("Error", "Discount must be a number")
                return

            with open(FILE, "r") as f:
                data = json.load(f)
            product_data = None
            for p in data.get(category, []):
                if p["name"] == product_name:
                    product_data = p
                    break

            if product_data:
                if 0 < discount < 100:
                    product_data["price"] = product_data["price"] * (1 - discount / 100)

                with open(FILE, "w") as f:
                    json.dump(data, f, indent=2)

                messagebox.showinfo("Success", f"Discount applied! New price: {product_data['price']}")

            else:
                messagebox.showerror("Error", "Product not found")

        tk.Button(main_frame, text="Apply Discount", font=("Arial", 14, "bold"), bg="#D17A01",
                      fg="white", bd=3, relief="raised", command=apply_discount).grid(row=4, column=0, columnspan=2, pady=30)

    def open_delete_items() :

        delete_pg = tk.Toplevel()
        delete_pg.title("Delete Items")
        delete_pg.state("zoomed")
        delete_pg.configure(bg="#f0f0f0")

        stack.push(delete_pg)

        main_frame = tk.Frame(delete_pg, bg="white", relief='raised', bd=2)
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)

        header_frame = tk.Frame(main_frame, bg="white")
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=10)  # خلي frame يتمدد أفقياً

        back_button = tk.Button(header_frame, text=" ← Back ", font=("Arial", 15, "bold"),
                                fg=Purple, bg="white", relief='flat', cursor='hand2',
                                command=stack.pop)
        back_button.pack(side="left", padx=0)

        tk.Label(main_frame, text="Delete Product", font=("Arial", 24, "bold"),
                 fg="#4e396e", bg="white").grid(row=0, column=0, columnspan=2, pady=(20, 40))
        tk.Label(main_frame, text="Select category and product to delete", font=("Arial", 16, "bold"),
                 fg="#4e396e", bg="white").grid(row=1, column=0, columnspan=2, pady=(0, 30))


        categories = ["HomeAppliances", "Books", "Fashion", "Sports", "Electronics"]
        tk.Label(main_frame, text="Category:", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(row=2, column=0, sticky="w",padx=10,pady=10)
        category_cb = ttk.Combobox(main_frame, values=categories, state="readonly", font=("Arial", 12))
        category_cb.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        tk.Label(main_frame, text="Product:", font=("Arial", 14), fg="#333333", bg="white", anchor="w").grid(row=3,column=0,sticky="w",padx=10,pady=10)
        product_cb = ttk.Combobox(main_frame, state="readonly", font=("Arial", 12))
        product_cb.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        main_frame.columnconfigure(1, weight=1)

        def load_products(event) :
            category = category_cb.get()
            try:
                with open(FILE, "r") as f:
                    data = json.load(f)
                product_list = []
                for product in data.get(category, []):
                    product_list.append(product["name"])
                product_cb["values"] = product_list
                product_cb.set("no items")
            except:
                product_cb["values"] = []
                product_cb.set("no items")

        category_cb.bind("<<ComboboxSelected>>", load_products)

        def delete_product():
            category = category_cb.get()
            product_name = product_cb.get()
            if not category or product_name == "no items":
                messagebox.showerror("Error", "Select a category and product")
                return
            with open(FILE, "r") as f:
                data = json.load(f)

            products_in_category = data.get(category, [])
            product_found = False


            for product in products_in_category:
                if product["name"] == product_name:
                    products_in_category.remove(product)
                    product_found = True
                    break

            if product_found:
                with open(FILE, "w") as f:
                    json.dump(data, f, indent=2)
                messagebox.showinfo("Success", f"Product '{product_name}' deleted successfully!")
                stack.pop()
            else:
                messagebox.showerror("Error", "Product not found")

        tk.Button(main_frame, text="Delete Product", font=("Arial", 14, "bold"),
                  bg="red", fg="white", bd=3, relief="raised", command=delete_product).grid(row=4, column=0, columnspan=2,pady=40)

    admin_pg = tk.Tk()
    admin_pg.state("zoomed")
    admin_pg.title("🔧 Administrator Panel ")
    admin_pg.configure(bg="#f0f0f0")
    admin_pg.resizable(True, True)

    stack.push(admin_pg)

    main_frame = tk.Frame(admin_pg, bg="white", relief='raised', bd=2)
    main_frame.pack(fill='both', expand=True, padx=50, pady=50)

    def go_login () :
        import Login
        admin_pg.withdraw()
        Login.run_login()

    header_frame = tk.Frame(main_frame, bg="white")
    header_frame.pack(fill="x", padx=30, pady=30)

    tk.Button(header_frame, text="Logout", font=("Arial", 14, "bold"), bg = "#C0392B",fg="white",command=go_login).pack(side="left")

    title_label = tk.Label(main_frame, text="Administrator Panel", font=("Arial", 24, "bold"),
                           fg="#4e396e", bg="white")
    title_label.pack(pady=60)

    subtitle_label = tk.Label(main_frame, text="Manage your store inventory", font=("Arial", 14),
                              fg="#555555", bg="white")
    subtitle_label.pack(pady=(0, 10))

    buttonFrame = tk.Frame(main_frame, bg="white")
    buttonFrame.pack(pady=10, fill='both')

    btn1 = tk.Button(buttonFrame, text="📦 Add Items", font=("Arial", 14),
                     fg="white", bg="#4e396e", width=25, height=2,command=open_add_items)
    btn1.pack(pady=15, fill='both', expand=True)

    btn2 = tk.Button(buttonFrame, text="✏️ Update Items", font=("Arial", 14),
                     fg="white", bg="#8B2F5A", width=25, height=2,command=open_update_items)
    btn2.pack(pady=15, fill='both', expand=True)

    btn3 = tk.Button(buttonFrame, text="💰 Make Discount", font=("Arial", 14),
                     fg="white", bg="#D17A01", width=25, height=2,command=open_discount_items)
    btn3.pack(pady=15, fill='both', expand=True)


    btn4 = tk.Button(buttonFrame, text="🗑️ Delete Items", font=("Arial", 14),
                     fg="white", bg="green", width=25, height=2, command=open_delete_items)
    btn4.pack(pady=15, fill='both', expand=True)

    admin_pg.mainloop()
