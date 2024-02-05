from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Пример приложения')
        self.setGeometry(100, 100, 300, 200)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        self.button = QPushButton('Нажми меня', self)
        self.layout.addWidget(self.button)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()