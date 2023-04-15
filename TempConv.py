import tkinter as tk
import webbrowser

def convert_temperature():
    # Get the temperature and scale from the user
    temperature = float(temperature_entry.get())
    scale = scale_var.get()

    # Convert the temperature
    if scale == "Celsius":
        converted_temperature = (temperature * 9/5) + 32
        result_scale = "Fahrenheit"
    else:
        converted_temperature = (temperature - 32) * 5/9
        result_scale = "Celsius"

    # Display the result in the output label
    output_label.config(text=f"{temperature:.1f} {scale} is {converted_temperature:.1f} {result_scale}.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create the label and entry widgets for the temperature
temperature_label = tk.Label(root, text="Enter the temperature:")
temperature_label.pack()
temperature_entry = tk.Entry(root)
temperature_entry.pack()

# Create the radio button widgets for the scale
scale_var = tk.StringVar()
scale_var.set("Celsius")
celsius_button = tk.Radiobutton(root, text="Celsius", variable=scale_var, value="Celsius")
celsius_button.pack()
fahrenheit_button = tk.Radiobutton(root, text="Fahrenheit", variable=scale_var, value="Fahrenheit")
fahrenheit_button.pack()

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create the output label
output_label = tk.Label(root, text="")
output_label.pack()

# Create the about label and link to GitHub profile
about_label = tk.Label(root, text="About", fg="blue", cursor="hand2")
about_label.pack()
about_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Neelanjan-chakraborty"))
bout_label.bind("<Button-2>", lambda e: webbrowser.open_new("https://github.com/BilalKhanlol"))

# Start the main event loop
root.mainloop()