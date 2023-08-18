from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QTabWidget,
    QVBoxLayout, QGridLayout
    )
from tab_layouts import StudentLayout
import sys


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

        _mainLayout.addWidget(self.createTabWidget())

    def createTabWidget(self):
        _tabWidget = QTabWidget()
        initialTab = QWidget()
        initialTabLayout = QGridLayout()
        initialTab.setLayout(initialTabLayout)

        studentTab = QWidget()
        studentTabLayout = StudentLayout()
        studentTab.setLayout(studentTabLayout)

        bookTab = QWidget()
        bookTabLayout = QGridLayout()
        bookTab.setLayout(bookTabLayout)

        loanAndDevolutionTab = QWidget()
        loanAndDevolutionTabLayout = QGridLayout()
        loanAndDevolutionTab.setLayout(loanAndDevolutionTabLayout)

        reportsTab = QWidget()
        reportsTabLayout = QGridLayout()
        reportsTab.setLayout(reportsTabLayout)

        _tabWidget.addTab(initialTab, "Início")
        _tabWidget.addTab(studentTab, "Alunos")
        _tabWidget.addTab(bookTab, "Livros")
        _tabWidget.addTab(loanAndDevolutionTab, "Empréstimos e Devoluções")
        _tabWidget.addTab(reportsTab, "Relatórios")
        return _tabWidget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec())
