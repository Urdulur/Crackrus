import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QLineEdit, QPushButton, QGridLayout, QGroupBox, QFormLayout,
                             QSizePolicy, QFileDialog, QAction) 
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import csv

class CrackGrowthGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.crack_analyzer = CrackGrowthAnalyzer()  # Create an instance of the business logic class

    def initUI(self):
        # Main layout
        mainLayout = QVBoxLayout()

        # Apply a stylesheet for the entire application
        self.setStyleSheet("""
            QGroupBox {
                font: bold;
                border: 1px solid silver;
                border-radius: 6px;
                margin-top: 6px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QLineEdit {
                border: 1px solid gray;
                border-radius: 4px;
                padding: 2px;
                height: 20px;
            }
            QPushButton {
                background-color: #5cacee;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 14px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #1c86ee;
                border-style: inset;
            }
        """)

        # Set the font for the entire window
        font = QFont('Arial', 10)
        self.setFont(font)

        # Group box for crack model selection
        crackModelGroup = QGroupBox("Расчетная схема для сквозной трещины")
        crackModelLayout = QVBoxLayout()
        self.crackModelCombo = QComboBox()
        self.crackModelCombo.addItems(["односторонняя краевая трещина в прямоугольной пластине",
                                        "центральная трещина в прямоугольной пластине",
                                        "центральное круговое или эллиптическое отверстие с трещиной, выходящей на его контур",
                                        "односторонняя угловая трещина в прямоугольной пластине",
                                        "центральная круговое или эллиптическое отверстие с угловой трещиной"])
        crackModelLayout.addWidget(self.crackModelCombo)
        crackModelGroup.setLayout(crackModelLayout)
        mainLayout.addWidget(crackModelGroup)
                

        # Group box for method selection
        methodGroup = QGroupBox("Управление для расчета роста трещины")
        methodLayout = QVBoxLayout()
        self.methodCombo = QComboBox()
        self.methodCombo.addItems(["NASGRO", "Paris-Walker", "NASGRO and Paris-Walker"])
        methodLayout.addWidget(self.methodCombo)
        methodGroup.setLayout(methodLayout)
        mainLayout.addWidget(methodGroup)


        # Group box for geometry input fields
        geometryGroup = QGroupBox("Геометрия")
        geometryLayout = QFormLayout()
        self.geometryLabels = ['adet, mm', 'acrit, mm', 'W, mm', 'p, mm', 'R, mm', 'b, mm']
        self.geometryInputs = {}
        for label in self.geometryLabels:
            edit = QLineEdit()
            geometryLayout.addRow(QLabel(label), edit)
            self.geometryInputs[label] = edit
        geometryGroup.setLayout(geometryLayout)
        mainLayout.addWidget(geometryGroup)

        # Group box for NASGRO material parameters
        self.nasgroGroup = QGroupBox("NASGRO Constants")
        nasgroGroup = QGroupBox("NASGRO Constants")
        nasgroLayout = QGridLayout()
        self.nasgroLabels = ['C', 'n', 'p', 'q', 'K1c', 'Δk', 'Bk', 'K0', 'alpha', 'C_th+', 'C_th-']
        self.nasgroInputs = {}
        for i, label in enumerate(self.nasgroLabels):
            edit = QLineEdit()
            nasgroLayout.addWidget(QLabel(label), i // 2, 2 * (i % 2))
            nasgroLayout.addWidget(edit, i // 2, 2 * (i % 2) + 1)
            self.nasgroInputs[label] = edit
        nasgroGroup.setLayout(nasgroLayout)
        mainLayout.addWidget(nasgroGroup)

        # Group box for Paris-Walker material parameters
        self.parisWalkerGroup = QGroupBox("Paris-Walker Constants")
        parisWalkerGroup = QGroupBox("Paris-Walker Constants")
        parisWalkerLayout = QGridLayout()
        self.parisWalkerLabels = ['n', 'C', 'R', 'm']
        self.parisWalkerInputs = {}
        for i, label in enumerate(self.parisWalkerLabels):
            edit = QLineEdit()
            parisWalkerLayout.addWidget(QLabel(label), i // 2, 2 * (i % 2))
            parisWalkerLayout.addWidget(edit, i // 2, 2 * (i % 2) + 1)
            self.parisWalkerInputs[label] = edit
        parisWalkerGroup.setLayout(parisWalkerLayout)
        mainLayout.addWidget(parisWalkerGroup)

        # Method selection with event handling
        self.methodCombo = QComboBox()
        self.methodCombo.addItems(["NASGRO", "Paris-Walker", "NASGRO and Paris-Walker"])
        self.methodCombo.currentIndexChanged.connect(self.on_method_changed)

        # Disconnect the signal-slot connection to prevent on_method_changed from being triggered
        # self.methodCombo.currentIndexChanged.disconnect(self.on_method_changed) 

        # Group box for stress input field
        stressMaxGroup = QGroupBox("Максимальные напряжения")
        stressMaxLayout = QHBoxLayout()
        self.stressMaxInput = QLineEdit()
        stressMaxLayout.addWidget(QLabel("Smax, ksi"))
        stressMaxLayout.addWidget(self.stressMaxInput)
        stressMaxGroup.setLayout(stressMaxLayout)
        mainLayout.addWidget(stressMaxGroup)

        # Calculate button with an icon
        self.calculateButton = QPushButton(QIcon('calculate-icon.png'), 'Рассчитать')
        self.calculateButton.clicked.connect(self.on_calculate_clicked)
        self.calculateButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        mainLayout.addWidget(self.calculateButton)

        # Set margins and spacing
        mainLayout.setSpacing(10)
        mainLayout.setContentsMargins(10, 10, 10, 10)

        # Set the main widget and layout
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        # Window settings
        self.setWindowTitle('Crack Growth Analysis Tool')
        self.setWindowIcon(QIcon('app-icon.png'))
        self.setGeometry(300, 300, 800, 600)
        self.show()
        
        # Menubar creation
        menubar = self.menuBar()

        # File menu
        fileMenu = menubar.addMenu('File')

        # Add 'Save' action
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.save_data)
        fileMenu.addAction(saveAction)

        # Add 'Load' action
        loadAction = QAction('Load', self)
        loadAction.triggered.connect(self.load_data)
        fileMenu.addAction(loadAction)

        # Edit menu (placeholder for future functionality)
        editMenu = menubar.addMenu('Edit')

        # Help menu (placeholder for future functionality)
        helpMenu = menubar.addMenu('Help')
        
        # Initially set visibility based on the default selection
        # self.on_method_changed()
    
    def on_method_changed(self):
        selected_method = self.methodCombo.currentText()
        self.nasgroGroup.setVisible('NASGRO' in selected_method)
        self.parisWalkerGroup.setVisible('Paris-Walker' in selected_method)

    def on_calculate_clicked(self):
        # Retrieve inputs from GUI components
        geometry_inputs = {label: edit.text() for label, edit in self.geometryInputs.items()}
        nasgro_constants = {label: edit.text() for label, edit in self.nasgroInputs.items()}
        pariswalker_constants = {label: edit.text() for label, edit in self.parisWalkerInputs.items()}
        stress_max = self.stressMaxInput.text()

        # Perform calculations using business logic
        result = self.crack_analyzer.calculate_growth({
            'geometry_inputs': geometry_inputs,
            'nasgro_constants': nasgro_constants,
            'pariswalker_constants': pariswalker_constants,
            'stress_max': stress_max,
        })
        print("Calculate button clicked")
        print(result)
    
    def save_data(self):
        # Open a file dialog to specify the filename and location to save
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Data", "",
                                                "CSV Files (*.csv);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Save selected crack model and method
                writer.writerow(['Crack Model', self.crackModelCombo.currentText()])
                writer.writerow(['Method', self.methodCombo.currentText()])
                
                # Save geometry inputs
                writer.writerow(['Geometry Inputs'])
                for label in self.geometryLabels:
                    writer.writerow([label, self.geometryInputs[label].text()])
                
                # Save NASGRO constants
                writer.writerow(['NASGRO Constants'])
                for label in self.nasgroLabels:
                    writer.writerow([label, self.nasgroInputs[label].text()])
                    
                # Save Paris-Walker constants
                writer.writerow(['Paris-Walker Constants'])
                for label in self.parisWalkerLabels:
                    writer.writerow([label, self.parisWalkerInputs[label].text()])

    def load_data(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load Data", "",
                                                "CSV Files (*.csv);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row or len(row) < 2:  # Skip empty rows
                        continue
                    label, value = row
                    if label in self.geometryLabels:
                        self.geometryInputs[label].setText(value)
                    elif label in self.nasgroLabels:
                        self.nasgroInputs[label].setText(value)
                    elif label in self.parisWalkerLabels:
                        self.parisWalkerInputs[label].setText(value)
                    elif label == 'Crack Model':
                        index = self.crackModelCombo.findText(value)
                        if index >= 0:
                            self.crackModelCombo.setCurrentIndex(index)
                    elif label == 'Method':
                        index = self.methodCombo.findText(value)
                        if index >= 0:
                            self.methodCombo.setCurrentIndex(index)



def main():
    app = QApplication(sys.argv)
    ex = CrackGrowthGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
