
from PySide6.QtWidgets import QApplication
from ui import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
