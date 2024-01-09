import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QDockWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Main Window settings
        self.setWindowTitle('Interface Example')
        self.setGeometry(100, 100, 800, 600)

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Файл')
        view_menu = menubar.addMenu('Вид')

        # Status Bar
        self.statusBar().showMessage('Ready')

        # Tool Bar
        toolbar = self.addToolBar('MainToolBar')
        star_action = QAction('Star', self)
        toolbar.addAction(star_action)
        
        # Adding icons to the toolbar
        # Here you would add your icons
        # star_action.setIcon(QIcon('path_to_star_icon.png'))

        # Central Widget
        text_edit = QTextEdit(self)
        self.setCentralWidget(text_edit)

        # Dock Widget
        dock = QDockWidget('Проекты', self)
        dock_label = QLabel('Here are projects')
        dock.setWidget(dock_label)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        # Show the main window
        self.show()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
