import math
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk, scrolledtext, Button, filedialog, messagebox, END


class PointRotation:
    def __init__(self, real_centre_z, real_centre_y, point_to_rotate_z, point_to_rotate_y):
        self.real_centre_Z = real_centre_z
        self.real_centre_Y = real_centre_y
        self.Z_shift = point_to_rotate_z - real_centre_z
        self.Y_shift = point_to_rotate_y - real_centre_y
        self.rotation_array = []
        self.angle_step = 15

    def calculate_rotation(self, angle):
        angle_radians = math.radians(angle)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)

        rotated_z = self.real_centre_Z + self.Z_shift * cos_angle + self.Y_shift * sin_angle
        rotated_y = self.real_centre_Y - self.Z_shift * sin_angle + self.Y_shift * cos_angle
        return angle, rotated_z, rotated_y  # Return angle, new_Z, new_Y

    def generate_rotation_matrix(self, angle_begin=0, angle_end=360):
        angle_range = range(angle_begin, angle_end, self.angle_step)
        self.rotation_array = [self.calculate_rotation(angle) for angle in angle_range]
        print(self.rotation_array)

    def set_angle_step(self, angle_step):
        self.angle_step = angle_step

    def plot_rotation(self):
        values_x = [item[1] for item in self.rotation_array]
        values_y = [item[2] for item in self.rotation_array]
        angle_descriptions = [item[0] for item in self.rotation_array]
        centre_of_rotation = [self.real_centre_Z, self.real_centre_Y]

        fig, ax = plt.subplots()
        ax.scatter(values_x, values_y)
        for i, txt in enumerate(angle_descriptions):
            ax.annotate(txt, (values_x[i], values_y[i]))

        ax.scatter(centre_of_rotation[0], centre_of_rotation[1])
        ax.annotate('Centre of Rotation', (centre_of_rotation[0], centre_of_rotation[1]))
        plt.show()

    def show_dataframe(self):
        df = pd.DataFrame(self.rotation_array, columns=['angle', 'new_Z', 'new_Y'])

        # Create a new window
        df_window = Tk()
        df_window.title("Rotation Dataframe")

        # Create a scrolled text widget to display the DataFrame
        text_widget = scrolledtext.ScrolledText(df_window, width=50, height=20)
        text_widget.insert(END, df.to_string(index=False))

        # Save button
        save_button = Button(df_window, text="Save as File", command=self.save_dataframe_as_file)

        # Pack widgets
        text_widget.pack()
        save_button.pack()

        # Start the Tkinter event loop for the new window
        df_window.mainloop()

    def df_and_plot(self):
        self.generate_rotation_matrix()
        self.plot_rotation()
        self.show_dataframe()

    def save_dataframe_as_file(self):
        # Ask user for file path and name
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("CSV files", "*.csv"),
                                                            ("All files", "*.*")])

        # If the user cancels the dialog, do nothing
        if not file_path:
            return

        # Determine the file format based on the selected file type
        file_format = file_path.split(".")[-1].lower()

        if file_format == "csv":
            # Save DataFrame to the chosen CSV file
            pd.DataFrame(self.rotation_array, columns=['angle', 'new_Z', 'new_Y']).to_csv(file_path, index=False)
        elif file_format == "txt":
            # Save DataFrame to the chosen text file
            pd.DataFrame(self.rotation_array, columns=['angle', 'new_Z', 'new_Y']).to_csv(file_path, sep='\t',
                                                                                          index=False)
        else:
            messagebox.showwarning("Unsupported File Type", "Unsupported file type. Please choose a CSV or TXT file.")
            return

        messagebox.showinfo("Save Successful", f"DataFrame saved as {file_path}")
