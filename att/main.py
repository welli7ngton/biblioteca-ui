
from PySide6.QtWidgets import QApplication
from ui import MainWindow
import sys


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())


main()
