# Author: Michael Beaudet
# Title: Program 3 Week 12
# Date: 4/24/25

import tkinter as tk
from tkinter import messagebox
# charge calculation function
def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
# account for negative numbers
        if minutes < 0:
            raise ValueError("Minutes can't be negative.")

        selected_rate = rate_var.get()
# if statements for day, evening, and offpeak hours
        if selected_rate == "day":
            rate = 0.02
        elif selected_rate == "evening":
            rate = 0.12
        elif selected_rate == "offpeak":
            rate = 0.05
        else:
            return
# calculate the total
        total = minutes * rate
        messagebox.showinfo("Call Charge", f"The charge for the call is: ${total:.2f}")
# account for value errors
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")
# create the main window
root = tk.Tk()
root.title("Long-Distance Call Charges")
# radio buttons for rate 
rate_var = tk.StringVar()
# have the defult option set to day
rate_var.set("day")  

rate_label = tk.Label(root, text="Select Rate Category:")
rate_label.pack(anchor="w")

radio_day = tk.Radiobutton(root, text="Daytime (6:00 AM - 5:59 PM)", variable=rate_var, value="day")
radio_day.pack(anchor="w")

radio_evening = tk.Radiobutton(root, text="Evening (6:00 PM - 11:59 PM)", variable=rate_var, value="evening")
radio_evening.pack(anchor="w")

radio_offpeak = tk.Radiobutton(root, text="Off-Peak (Midnight - 5:59 AM)", variable=rate_var, value="offpeak")
radio_offpeak.pack(anchor="w")
# the entry for minutes
minutes_label = tk.Label(root, text="Enter call duration (minutes):")
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack()
# button to calculate charge
calculation_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculation_button.pack(pady=5)
# run the program
root.mainloop()
