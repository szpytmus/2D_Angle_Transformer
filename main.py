import tkinter as tk
from rotation import PointRotation

def submit_form():
    # Get the values from the entries
    real_centre_Z = float(entry1.get())
    real_centre_Y = float(entry2.get())
    point_to_rotate_Z = float(entry3.get())
    point_to_rotate_Y = float(entry4.get())
    angle_begin = int(line_entry1.get())
    angle_end = int(line_entry2.get())
    angle_step = int(angle_step_entry.get())  # New entry for angle step

    # Create an instance of PointRotation
    rotation = PointRotation(real_centre_Z, real_centre_Y, point_to_rotate_Z, point_to_rotate_Y)

    # Set the angle range and step
    rotation.set_angle_step(angle_step)
    rotation.generate_rotation_matrix(angle_begin, angle_end)

    # Generate rotation matrix and plot
    rotation.plot_rotation()
    rotation.show_dataframe()

# Create the main window
window = tk.Tk()
window.title("Tkinter Form Template")

# Create Entry widgets
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)
line_entry1 = tk.Entry(window)
line_entry2 = tk.Entry(window)
angle_step_entry = tk.Entry(window)  # New entry for angle step

# Create labels
label1 = tk.Label(window, text="Z - center of rotation:")
label2 = tk.Label(window, text="Y - center of rotation:")
label3 = tk.Label(window, text="Z - point to rotate:")
label4 = tk.Label(window, text="Y - point to rotate:")
line_label1 = tk.Label(window, text="Angle Range (begin):")
line_label2 = tk.Label(window, text="Angle Range (end):")
angle_step_label = tk.Label(window, text="Angle Step:")

# Create a button to submit the form
submit_button = tk.Button(window, text="Submit", command=submit_form)

# Arrange widgets in the grid
label1.grid(row=0, column=0, sticky="e")
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky="e")
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0, sticky="e")
entry3.grid(row=2, column=1)
label4.grid(row=3, column=0, sticky="e")
entry4.grid(row=3, column=1)
line_label1.grid(row=4, column=0, sticky="e")
line_entry1.grid(row=4, column=1)
line_label2.grid(row=4, column=2, sticky="e")
line_entry2.grid(row=4, column=3)
angle_step_label.grid(row=5, column=3, sticky="e")
angle_step_entry.grid(row=5, column=4)
submit_button.grid(row=6, column=2)

# Start the Tkinter event loop
window.mainloop()