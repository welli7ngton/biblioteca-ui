from student_and_book import Student
from student_and_book import Book
from database import DataBase
from PySide6.QtWidgets import QApplication
from ui import MainWindow
import sys

if __name__ == "__main__":
    s1 = Student()
    b1 = Book()
    db = DataBase()

    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
