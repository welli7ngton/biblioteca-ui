from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QTabWidget,
    QVBoxLayout, QGridLayout
    )
import sys

# My imports
# from mybuttons import MyButtons
from studentlayout import StudentLayout


class MainWindow(QMainWindow):
    def __init__(self, ) -> None:
        super().__init__()
        self.setWindowTitle("Biblioteca")
        self.resize(800, 800)
        self.__initUI()

    def __initUI(self):
        _centralWidget = QWidget()
        self.setCentralWidget(_centralWidget)

        _mainLayout = QVBoxLayout()
        _centralWidget.setLayout(_mainLayout)

        _tabWidget = QTabWidget()
        _mainLayout.addWidget(_tabWidget)

        initialTab = QWidget()
        self.initialTabLayout = QGridLayout()
        initialTab.setLayout(self.initialTabLayout)

        studentTab = QWidget()
        self.studentTabLayout = StudentLayout()
        studentTab.setLayout(self.studentTabLayout)

        bookTab = QWidget()
        self.bookTabLayout = QGridLayout()
        bookTab.setLayout(self.bookTabLayout)

        loanAndDevolutionTab = QWidget()
        self.loanAndDevolutionTabLayout = QGridLayout()
        loanAndDevolutionTab.setLayout(self.loanAndDevolutionTabLayout)

        reportsTab = QWidget()
        reportsTabLayout = QGridLayout()
        reportsTab.setLayout(reportsTabLayout)

        _tabWidget.addTab(initialTab, "Início")
        _tabWidget.addTab(studentTab, "Alunos")
        _tabWidget.addTab(bookTab, "Livros")
        _tabWidget.addTab(loanAndDevolutionTab, "Empréstimos e Devoluções")
        _tabWidget.addTab(reportsTab, "Relatórios")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec())
