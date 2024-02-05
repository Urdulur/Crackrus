import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
             
class CrackGrowthCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Crack Growth Calculator")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self, text="Input Parameters")
        input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Geometry selection
        ttk.Label(input_frame, text="Select Geometry:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.geometry_var = tk.IntVar(value=1)
        geometry_combobox = ttk.Combobox(input_frame, textvariable=self.geometry_var, values=[1, 2, 3, 4])
        geometry_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Equation selection
        ttk.Label(input_frame, text="Select Equation:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.equation_var = tk.IntVar(value=1)
        equation_combobox = ttk.Combobox(input_frame, textvariable=self.equation_var, values=[1, 2, 3])
        equation_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Radius entry
        ttk.Label(input_frame, text="Radius (Rad):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.rad_entry = ttk.Entry(input_frame)
        self.rad_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Output Frame
        output_frame = ttk.LabelFrame(self, text="Results")
        output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=output_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Calculate Button
        calculate_button = ttk.Button(self, text="Calculate", command=self.calculate)
        calculate_button.pack(pady=10)

    def calculate(self):
        try:
            # Retrieve user input
            geometry_choice = self.geometry_var.get()
            equation_choice = self.equation_var.get()
            rad_value = float(self.rad_entry.get())

            # Call calculation function based on user input
            result = self.calculate_crack_growth(geometry_choice, equation_choice, rad_value)

            # Update the Matplotlib figure with the results
            self.update_plot(result)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def calculate_crack_growth(self, geometry_choice, equation_choice, rad_value):
        if equation_choice == 1:
            return self.equation_1_calculation(geometry_choice, rad_value)
        elif equation_choice == 2:
            return self.equation_2_calculation(geometry_choice, rad_value)
        elif equation_choice == 3:
            return self.equation_3_calculation(geometry_choice, rad_value)
        else:
            # Default placeholder calculation
            return np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100))

    def equation_1_calculation(self, geometry_choice, rad_value):
        # Replace this with your actual calculation logic for Equation 1
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        return x, y

    def equation_2_calculation(self, geometry_choice, rad_value):
        # Replace this with your actual calculation logic for Equation 2
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        return x, y

    def equation_3_calculation(self, geometry_choice, rad_value):
        # Replace this with your actual calculation logic for Equation 3
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        return x, y

    def update_plot(self, results):
        x, y = results
        self.ax.clear()
        self.ax.plot(x, y, label='Result Plot')
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = CrackGrowthCalculator()
    app.mainloop()
