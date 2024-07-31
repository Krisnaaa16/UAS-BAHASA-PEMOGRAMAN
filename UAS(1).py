import tkinter as tk
from tkinter import messagebox

# Room data
rooms = {
    'M': {'name': 'Melati', 'price': 650000},
    'S': {'name': 'Sakura', 'price': 550000},
    'L': {'name': 'Lily', 'price': 400000},
    'A': {'name': 'Anggrek', 'price': 350000}
}

def calculate():
    try:
        # Get input values
        staff_name = entry_staff_name.get()
        customer_name = entry_customer_name.get()
        checkin_date = entry_checkin_date.get()
        room_code = entry_room_code.get().upper()
        rental_duration = int(entry_rental_duration.get())
        payment_amount = int(entry_payment_amount.get())
        
        # Check if the room code is valid
        if room_code not in rooms:
            messagebox.showerror("Error", "Invalid room code")
            return

        # Get room details
        room_name = rooms[room_code]['name']
        room_price = rooms[room_code]['price']
        
        # Calculate the initial amount
        total_rent = room_price * rental_duration
        
        # Calculate discount
        discount = 0
        if rental_duration > 5:
            discount = 0.10 * total_rent
        elif rental_duration > 3:
            discount = 0.05 * total_rent
        
        # Calculate PPN
        ppn = 0.1 * (total_rent - discount)
        
        # Calculate total payment
        total_payment = total_rent - discount + ppn
        
        # Calculate change
        change = payment_amount - total_payment
        
        # Display results
        receipt_text = f"""
        Hotel SEJUK ASRI
        -----------------------
        Staff Name: {staff_name}
        Customer Name: {customer_name}
        Check-in Date: {checkin_date}
        Room Name: {room_name}
        Room Price per Night: Rp {room_price}
        Rental Duration: {rental_duration} nights
        Discount: Rp {discount}
        PPN 10%: Rp {ppn}
        Total Payment: Rp {total_payment}
        Amount Paid: Rp {payment_amount}
        Change: Rp {change}
        """
        receipt_label.config(text=receipt_text)
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values for rental duration and payment amount.")

# Create main window
root = tk.Tk()
root.title("Hotel SEJUK ASRI Booking System")

# Input fields
tk.Label(root, text="Input Staff Name:").grid(row=0, column=0)
entry_staff_name = tk.Entry(root)
entry_staff_name.grid(row=0, column=1)

tk.Label(root, text="Input Customer Name:").grid(row=1, column=0)
entry_customer_name = tk.Entry(root)
entry_customer_name.grid(row=1, column=1)

tk.Label(root, text="Input Check-in Date:").grid(row=2, column=0)
entry_checkin_date = tk.Entry(root)
entry_checkin_date.grid(row=2, column=1)

tk.Label(root, text="Enter Room Code [M/S/L/A]:").grid(row=3, column=0)
entry_room_code = tk.Entry(root)
entry_room_code.grid(row=3, column=1)

tk.Label(root, text="Enter Rental Duration:").grid(row=4, column=0)
entry_rental_duration = tk.Entry(root)
entry_rental_duration.grid(row=4, column=1)

tk.Label(root, text="Enter Payment Amount:").grid(row=5, column=0)
entry_payment_amount = tk.Entry(root)
entry_payment_amount.grid(row=5, column=1)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=2)

# Receipt display
receipt_label = tk.Label(root, text="", justify='left')
receipt_label.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()