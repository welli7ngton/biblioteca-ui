from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QTabWidget,
    QGridLayout
    )
from tab_layouts import StudentLayout
from tab_layouts import BookLayout
from tab_layouts import loanAndDevolutionLayout
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Biblioteca")
        self.resize(900, 800)
        self.setCentralWidget(self.createTabWidget())

    def createTabWidget(self) -> QTabWidget:
        _tabWidget = QTabWidget()
        initialTab = QWidget()
        initialTabLayout = QGridLayout()
        initialTab.setLayout(initialTabLayout)

        studentTab = QWidget()
        studentTabLayout = StudentLayout()
        studentTab.setLayout(studentTabLayout)

        bookTab = QWidget()
        bookTabLayout = BookLayout()
        bookTab.setLayout(bookTabLayout)

        loanAndDevolutionTab = QWidget()
        loanAndDevolutionTabLayout = loanAndDevolutionLayout()
        loanAndDevolutionTab.setLayout(loanAndDevolutionTabLayout)

        _tabWidget.addTab(initialTab, "Início")
        _tabWidget.addTab(studentTab, "Alunos")
        _tabWidget.addTab(bookTab, "Livros")
        _tabWidget.addTab(loanAndDevolutionTab, "Empréstimos e Devoluções")
        return _tabWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec())
