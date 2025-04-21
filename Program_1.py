# Author: Michael Beaudet
# Title: Program 1 Week 12
# Date: 4/21/25

import tkinter as tk
import tkinter.messagebox

# Make the calculation function
def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        mpg = miles / gallons
        tk.messagebox.showinfo("Miles Per Gallon", f"The car gets {mpg:.2f} miles per gallon.")
# account for user error
    except ValueError:
        tk.messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        tk.messagebox.showerror("Math Error", "Gallons cannot be zero.")

# create the main window
main_window = tk.Tk()
main_window.title("Gas Mileage Calulator")

# create frames
top_frame = tk.Frame(main_window)
mid_frame = tk.Frame(main_window)
bottom_frame = tk.Frame(main_window)

# Create widgets for top frame
gallons_label = tk.Label(top_frame, text="Enter number of gallons:")
gallons_entry = tk.Entry(top_frame, width=10)

# Pack the top frame widgets
gallons_label.pack(side="left")
gallons_entry.pack(side="left")

# create widgets for the middle frame
miles_label = tk.Label(mid_frame, text="Enter number of miles:")
miles_entry = tk.Entry(mid_frame, width=10)

# pack the middle frame widgets
miles_label.pack(side="left")
miles_entry.pack(side="left")

# create buttons for the bottom frame
calc_button = tk.Button(bottom_frame, text="Calculate MPG", command=calculate_mpg)
quit_button = tk.Button(bottom_frame, text="Quit", command=main_window.destroy)

# pack the bottom frame widgets
calc_button.pack(side="left")
quit_button.pack(side="left")

# pack the frames
top_frame.pack(pady=5)
mid_frame.pack(pady=5)
bottom_frame.pack(pady=10)

# run the program
main_window.mainloop()

