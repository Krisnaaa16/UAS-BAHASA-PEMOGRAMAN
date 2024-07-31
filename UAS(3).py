import tkinter as tk
from tkinter import messagebox

# Class for the Product Management System
class ProductManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")

        self.products = {}

        self.create_widgets()

    def create_widgets(self):
        # Input product data
        tk.Label(self.root, text="Input Product Name:").grid(row=0, column=0)
        self.entry_product_name = tk.Entry(self.root)
        self.entry_product_name.grid(row=0, column=1)

        tk.Label(self.root, text="Input Product Price:").grid(row=1, column=0)
        self.entry_product_price = tk.Entry(self.root)
        self.entry_product_price.grid(row=1, column=1)

        tk.Label(self.root, text="Input Product Stock:").grid(row=2, column=0)
        self.entry_product_stock = tk.Entry(self.root)
        self.entry_product_stock.grid(row=2, column=1)

        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2)

        # Display products
        tk.Button(self.root, text="Display Products", command=self.display_products).grid(row=4, column=0, columnspan=2)

        # Search product
        tk.Label(self.root, text="Search Product by Name:").grid(row=5, column=0)
        self.entry_search_name = tk.Entry(self.root)
        self.entry_search_name.grid(row=5, column=1)
        tk.Button(self.root, text="Search", command=self.search_product).grid(row=6, column=0, columnspan=2)

        # Delete product
        tk.Label(self.root, text="Delete Product by Name:").grid(row=7, column=0)
        self.entry_delete_name = tk.Entry(self.root)
        self.entry_delete_name.grid(row=7, column=1)
        tk.Button(self.root, text="Delete", command=self.delete_product).grid(row=8, column=0, columnspan=2)

        # Purchase product
        tk.Label(self.root, text="Purchase Product by Name:").grid(row=9, column=0)
        self.entry_purchase_name = tk.Entry(self.root)
        self.entry_purchase_name.grid(row=9, column=1)

        tk.Label(self.root, text="Quantity to Purchase:").grid(row=10, column=0)
        self.entry_purchase_quantity = tk.Entry(self.root)
        self.entry_purchase_quantity.grid(row=10, column=1)

        tk.Button(self.root, text="Purchase", command=self.purchase_product).grid(row=11, column=0, columnspan=2)

        # Output area
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.grid(row=12, column=0, columnspan=2)

    def add_product(self):
        name = self.entry_product_name.get()
        try:
            price = int(self.entry_product_price.get())
            stock = int(self.entry_product_stock.get())
            if name in self.products:
                messagebox.showerror("Error", "Product already exists.")
            else:
                self.products[name] = {'price': price, 'stock': stock}
                messagebox.showinfo("Success", "Product added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid price or stock value.")

    def display_products(self):
        self.output_text.delete('1.0', tk.END)
        if not self.products:
            self.output_text.insert(tk.END, "No products available.")
        else:
            for name, details in self.products.items():
                self.output_text.insert(tk.END, f"Name: {name}, Price: {details['price']}, Stock: {details['stock']}\n")

    def search_product(self):
        name = self.entry_search_name.get()
        if name in self.products:
            details = self.products[name]
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, f"Name: {name}, Price: {details['price']}, Stock: {details['stock']}\n")
        else:
            messagebox.showerror("Error", "Product not found.")

    def delete_product(self):
        name = self.entry_delete_name.get()
        if name in self.products:
            del self.products[name]
            messagebox.showinfo("Success", "Product deleted successfully.")
        else:
            messagebox.showerror("Error", "Product not found.")

    def purchase_product(self):
        name = self.entry_purchase_name.get()
        try:
            quantity = int(self.entry_purchase_quantity.get())
            if name in self.products:
                if self.products[name]['stock'] >= quantity:
                    self.products[name]['stock'] -= quantity
                    total_price = self.products[name]['price'] * quantity
                    self.output_text.delete('1.0', tk.END)
                    self.output_text.insert(tk.END, f"Purchased {quantity} of {name}. Total Price: {total_price}\n")
                else:
                    messagebox.showerror("Error", "Insufficient stock.")
            else:
                messagebox.showerror("Error", "Product not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity.")

# Create the main window
root = tk.Tk()
app = ProductManagementSystem(root)
root.mainloop()
