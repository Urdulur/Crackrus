import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox)
from PyQt5.QtCore import Qt

# Assuming your script's function is named 'betta' and requires certain parameters
from tempfile_test import betta

class ExampleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create layout
        layout = QVBoxLayout()

        # Input fields with labels
        self.a_input = self.create_input_field("a:", layout)
        self.b_input = self.create_input_field("b:", layout)
        self.choice_geom_input = self.create_input_field("Choice Geometry:", layout)
        self.Rad_input = self.create_input_field("Rad:", layout)

        # Button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.on_calculate)
        layout.addWidget(self.calculate_button)

        # Output display
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        # Set the layout
        self.setLayout(layout)
        self.setWindowTitle('Calculation Interface')

    def create_input_field(self, label_text, layout):
        layout.addWidget(QLabel(label_text))
        line_edit = QLineEdit()
        layout.addWidget(line_edit)
        return line_edit

    def on_calculate(self):
        try:
            a = self.validate_input(self.a_input.text(), float)
            b = self.validate_input(self.b_input.text(), float)
            choice_geom = self.validate_input(self.choice_geom_input.text(), int)
            Rad = self.validate_input(self.Rad_input.text(), float)

            result = betta(a, b, choice_geom, Rad)
            self.result_display.setText(str(result))
        except ValueError as e:
            QMessageBox.critical(self, "Input Error", f"Invalid input: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Calculation Error", f"Error during calculation: {str(e)}")

    def validate_input(self, input_str, data_type):
        if data_type == int:
            return int(input_str)
        elif data_type == float:
            return float(input_str)
        return input_str

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ExampleApp()
    window.show()

    sys.exit(app.exec_())
