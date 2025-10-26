# 🛍️ Online Store Project

This is a complete online store system built with Python and a graphical user interface (GUI) using Tkinter. This project is not just a standard application; it focuses on efficiently implementing fundamental Data Structures and Algorithms without relying on built-in functions.

---

## 🚀 Key Features

The system supports two types of users: Admin and Normal User.

### 👤 For the Normal User

* **Register:** Users can register their information (name, email, phone, governorate, etc.), which is stored in a suitable data structure.
* **Login:** Access the system using an email and password.
* **Homepage (Browse Categories):** View available categories (Home Appliances, Electronics, Fashion, Books, Sports).
* **Browse Products:** Users can browse products within each category.
* **Add to Cart:** Add any product to the shopping cart.
* **View Cart:** A dedicated page to display all items added to the cart.
* **Calculate Cost:** Calculates the total price plus shipping fees (which depend on the user's governorate compared to Cairo).

### ⚙️ For the Admin

* **Secure Login:** The admin logs in with fixed credentials (`admin@gmail.com` and `admin123`).
* **Product Management:** The admin can add new products and update existing product information across all categories.
* **(Future: Add discounts)**.

---

## 💻 The Real Challenge: Data Structures & Algorithms

This project applies core CS concepts to ensure performance:

### 1. Search - $O(\log n)$
On the category page, a user can search for a specific item by name. This search operation must be efficient, running in $O(\log n)$ time complexity, which is achieved by implementing the **Binary Search** algorithm (without using built-in functions).

### 2. Sorting - (Efficiently)
The user can sort products by price (ascending or descending). This sorting process is done using a "fast" algorithm (like **Merge Sort** or **Quick Sort**) to ensure high performance (also without using built-in functions).

### 3. Navigation History - (Stack)
The "Back" button is not just a simple button. It utilizes a suitable data structure (like a **Stack**) to store the history of visited pages, allowing the user to go back one step at a time in the correct order.

### 4. Total Price Calculation - (Recursion)
In the shopping cart, the total price of the items is calculated in a "non-iterative" way, which is implemented using **Recursion** (a function that calls itself to sum the prices).

### 5. Data Storage (Data Structures)
All user data, categories, and product details (name, price, brand, model year) are stored in appropriate data structures (like Dictionaries, Lists, or custom Objects).

---

## 🛠️ Technologies Used
* **🐍 Python**
* **🖼️ Tkinter** (for the GUI)

---

