import sys
#from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QHBoxLayout, QVBoxLayout
import qdarktheme
import webbrowser


class TemperatureConverter(QWidget):
	def __init__(self):
		super().__init__()

		# Apply the complete dark theme to your Qt App.
		#qdarktheme.setup_theme()
		#main_win = QMainWindow()
		#push_button = QPushButton("PyQtDarkTheme!!")
		#main_win.setCentralWidget(push_button)

		# Create UI elements
		self.temp_label = QLabel("Temperature:")
		self.temp_input = QLineEdit()
		self.scale_label = QLabel("Scale:")
		self.scale_dropdown = QComboBox()
		self.scale_dropdown.addItems(["Celsius", "Fahrenheit", "Kelvin"])
		self.convert_button = QPushButton("Convert")
		self.about = QPushButton("About")
		self.result_label = QLabel("Result:")


		# Connect the button to the conversion function
		self.convert_button.clicked.connect(self.convert_temperature)
		self.about.clicked.connect(self.open_github_profile)

		# Create layouts
		input_layout = QHBoxLayout()
		input_layout.addWidget(self.temp_label)
		input_layout.addWidget(self.temp_input)
		input_layout.addWidget(self.scale_label)
		input_layout.addWidget(self.scale_dropdown)

		result_layout = QHBoxLayout()
		result_layout.addWidget(self.result_label)

		button_layout = QHBoxLayout()
		button_layout.addWidget(self.convert_button)


		button_layout1 = QHBoxLayout()
		button_layout1.addWidget(self.about)

		main_layout = QVBoxLayout()
		main_layout.addLayout(input_layout)
		main_layout.addLayout(result_layout)
		main_layout.addLayout(button_layout)
		main_layout.addLayout(button_layout1)

		# Set the main layout for the window
		self.setLayout(main_layout)

		# Set the window properties
		self.setWindowTitle("Temperature Converter")
		self.resize(300, 150)

	def open_github_profile(self):
		# Open GitHub profile in default web browser
		webbrowser.open_new_tab("https://github.com/Neelanjan-chakraborty")

	def convert_temperature(self):
		# Get the temperature and selected scale from the input widgets
		temperature_string = self.temp_input.text()
		scale = self.scale_dropdown.currentText()

		# Convert the temperature string to a number
		try:
			temperature = float(temperature_string)
		except ValueError:
			# Display an error message if the temperature is not a valid number
			self.result_label.setText("Result: Invalid temperature")
			return

		# Convert the temperature to the selected scale
		if scale == "Celsius":
			converted_temperature = (temperature - 32) * 5 / 9
		elif scale == "Fahrenheit":
			converted_temperature = temperature * 9 / 5 + 32
		else:
			converted_temperature = temperature - 273.15

		# Round the converted temperature to 2 decimal places
		rounded_temperature = round(converted_temperature, 2)

		# Update the result label with the converted temperature
		self.result_label.setText(f"Result: {rounded_temperature:.2f} {scale}")


if __name__ == '__main__':
	app = QApplication(sys.argv)
	temperature_converter = TemperatureConverter()
	temperature_converter.show()
	sys.exit(app.exec_())
