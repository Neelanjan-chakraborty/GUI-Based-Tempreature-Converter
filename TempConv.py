import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip

class TemperatureConverter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Set the window title
        self.master.title("Temperature Converter")

        # Set the window size
        self.master.geometry("300x250")

        # Create a style for the frame and widgets
        self.style = ttk.Style(self)
        self.style.theme_use("default")
        self.style.configure("TFrame", background="#f2f2f2")
        self.style.configure("TLabel", background="#f2f2f2")
        self.style.configure("TRadiobutton", background="#f2f2f2")
        self.style.configure("TButton", background="#f2f2f2")
        self.style.configure("TEntry", background="#fff")

        # Create the widgets
        self.temperature_label = ttk.Label(self, text="Temperature:")
        self.temperature_entry = ttk.Entry(self, width=8)
        self.celsius_button = ttk.Radiobutton(self, text="Celsius", variable=self.scale_var, value="Celsius")
        self.fahrenheit_button = ttk.Radiobutton(self, text="Fahrenheit", variable=self.scale_var, value="Fahrenheit")
        self.kelvin_button = ttk.Radiobutton(self, text="Kelvin", variable=self.scale_var, value="Kelvin")
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_temperature)
        self.round_label = ttk.Label(self, text="Round to:")
        self.round_entry = ttk.Entry(self, width=3)
        self.round_entry.insert(tk.END, "1")
        self.copy_button = ttk.Button(self, text="Copy to clipboard", command=self.copy_to_clipboard)
        self.output_label = ttk.Label(self, text="", font=("Arial", 16))

        # Position the widgets using the grid layout manager
        self.temperature_label.grid(row=0, column=0, padx=5, pady=5)
        self.temperature_entry.grid(row=0, column=1, padx=5, pady=5)
        self.celsius_button.grid(row=1, column=0, padx=5, pady=5)
        self.fahrenheit_button.grid(row=1, column=1, padx=5, pady=5)
        self.kelvin_button.grid(row=1, column=2, padx=5, pady=5)
        self.convert_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        self.round_label.grid(row=3, column=0, padx=5, pady=5)
        self.round_entry.grid(row=3, column=1, padx=5, pady=5)
        self.copy_button.grid(row=3, column=2, padx=5, pady=5)
        self.output_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # Set the focus to the temperature entry widget
        self.temperature_entry.focus()

    def convert_temperature(self):
        try:
            # Get the temperature and scale from the user
            temperature = float(self.temperature_entry.get())
            scale = self.scale_var.get()
        except ValueError:
            # Display an error message if the temperature is not a valid number
            messagebox.showerror("Error", "Invalid temperature")
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
            converted_temperature = round(converted_temperature, decimal_places)
        except ValueError:
            pass

        # Display the converted temperature
        self.output_label.configure(text=f"{converted_temperature:.2f} {scale}")

    def copy_to_clipboard(self):
        # Copy the converted temperature to the clipboard
        converted_temperature = self.output_label.cget("text")
        pyperclip.copy(converted_temperature)
        messagebox.showinfo("Information", "Temperature copied to clipboard")

if name == "main":
    root = tk.Tk()
    app = TemperatureConverter(root)
    app.mainloop()

