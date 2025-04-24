# Author: Michael Beaudet
# Title: Program 2 Week 12 
# Date: 4/22/25

import tkinter as tk
from tkinter import messagebox

# the function to calculate and show total
def show_total():
    total = 0
    if oil_var.get():
        total += 30
    if lube_var.get():
        total += 20
    if radiator_var.get():
        total += 40
    if transmission_var.get():
        total += 100
    if inspection_var.get():
        total += 35
    if muffler_var.get():
        total += 200
    if tire_var.get():
        total += 20
    messagebox.showinfo("Total Charges", f"Total: ${total:.2f}")

# main window
main_window = tk.Tk()
main_window.title("Joe's Automotive")

# variables for each service
oil_var = tk.IntVar()
lube_var = tk.IntVar()
radiator_var = tk.IntVar()
transmission_var = tk.IntVar()
inspection_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

# top frame for checkbuttons
top_frame = tk.Frame(main_window)
tk.Checkbutton(top_frame, text="Oil Change - $30", variable=oil_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Lube Job - $20", variable=lube_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Radiator Flush - $40", variable=radiator_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Transmission Fluid - $100", variable=transmission_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Inspection - $35", variable=inspection_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Muffler Replacement - $200", variable=muffler_var).pack(anchor='w')
tk.Checkbutton(top_frame, text="Tire Rotation - $20", variable=tire_var).pack(anchor='w')
# bottom frame for buttons
bottom_frame = tk.Frame(main_window)
tk.Button(bottom_frame, text="Calculate Total", command=show_total).pack(side='left')
tk.Button(bottom_frame, text="Quit", command=main_window.destroy).pack(side='left')
# pack the frames
top_frame.pack()
bottom_frame.pack()
# run the program
main_window.mainloop()
