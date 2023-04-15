import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip


class TemperatureConverter(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.master.title("Temperature Converter-Bilal Khan and Neelanjan")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.create_widgets()

    def create_widgets(self):
        # Create the input label and entry widget
        self.input_label = ttk.Label(self.master, text="Enter temperature:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_entry = ttk.Entry(self.master)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create the scale label and option menu
        self.scale_label = ttk.Label(self.master, text="Select scale:")
        self.scale_label.grid(row=1, column=0, padx=5, pady=5)
        self.scale_var = tk.StringVar(value="Celsius")
        self.scale_menu = ttk.OptionMenu(self.master, self.scale_var, "Celsius", "Celsius", "Fahrenheit", "Kelvin")
        self.scale_menu.grid(row=1, column=1, padx=5, pady=5)

        # Create the round label and entry widget
        self.round_label = ttk.Label(self.master, text="Round to decimal places:")
        self.round_label.grid(row=2, column=0, padx=5, pady=5)
        self.round_entry = ttk.Entry(self.master, width=5)
        self.round_entry.insert(tk.END, "2")
        self.round_entry.grid(row=2, column=1, padx=5, pady=5)

        # Create the convert button
        self.convert_button = ttk.Button(self.master, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(row=3, column=0, padx=5, pady=5)

        # Create the output label and copy button
        self.output_label = ttk.Label(self.master, text="")
        self.output_label.grid(row=3, column=1, padx=5, pady=5)
        self.copy_button = ttk.Button(self.master, text="Copy", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=1, padx=5, pady=5)

        # Create the dark mode button
        self.dark_mode_button = ttk.Button(self.master, text="Dark Mode", command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=4, column=0, padx=5, pady=5)

    def convert_temperature(self):
        # Get the temperature and selected scale from the input widgets
        temperature_string = self.input_entry.get()
        scale = self.scale_var.get()

        # Convert the temperature string to a number
        try:
            temperature = float(temperature_string)
        except ValueError:
            # Display an error message if the temperature is not a valid number
            messagebox.showerror("Error", "Invalid temperature Measure")
            return

        # Convert the temperature to the selected scale
        if scale == "Celsius":
            converted_temperature = (temperature - 32) * 5 / 9
        elif scale == "Fahrenheit":
            converted_temperature = temperature * 9 / 5 + 32
        else:
            converted_temperature = temperature - 273.15

        # Round the converted temperature to the specified number of decimal places
        try:
            decimal_places = int(self.round_entry.get())
            converted
        except ValueError:
            # Display an error message if the decimal places is not a valid integer
            messagebox.showerror("Error:", "Invalid number of decimal places, Please Correct")
            return

        rounded_temperature = round(converted_temperature, decimal_places)

        # Update the output label with the converted temperature
        self.output_label.config(text=f"{rounded_temperature:.{decimal_places}f} {scale}")

    def copy_to_clipboard(self):
        # Copy the converted temperature to the clipboard
        converted_temperature = self.output_label.cget("text")
        pyperclip.copy(converted_temperature)
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

    def toggle_dark_mode(self):
        # Toggle dark mode
        if self.style.theme_use() == "default":
            self.style.theme_use('alt')
        else:
            self.style.theme_use("default")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    #app.pack()
    root.mainloop()