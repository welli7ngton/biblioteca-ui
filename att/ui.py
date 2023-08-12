
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton,
    QDialog, QVBoxLayout, QFormLayout, QLineEdit
    )
import sys
import qdarktheme


class MainWindow(QMainWindow):
    def __init__(self, ) -> None:
        super().__init__()

        self.initUI()
        self.addWindowStyle()

    def initUI(self):
        # criando widget central e layout central
        _centralWidget = QWidget()
        _mainLayout = QVBoxLayout()

        # criando widget da barra de navegação de páginas e layout
        _navigationBarWidget = QWidget()
        _navigationBarLayout = QHBoxLayout()

        # setando o layout do widget central
        _centralWidget.setLayout(_mainLayout)

        # setando o layout da barra de navegação
        _navigationBarWidget.setLayout(_navigationBarLayout)

        # setando o widget central na janela do programa
        self.setCentralWidget(_centralWidget)

        # adicionando a barra de navegação no layout principal do programa
        _mainLayout.addWidget(
            _navigationBarWidget,
            alignment=Qt.AlignmentFlag.AlignTop
            )

        studentFunctions = QPushButton("Alunos")
        bookFunctions = QPushButton("Livros")
        loanOrDevolutionFunctions = QPushButton("Empréstimos | Devoluções")
        reportsFunctions = QPushButton("Relatórios")

        _navigationBarLayout.addWidget(studentFunctions)
        _navigationBarLayout.addWidget(bookFunctions)
        _navigationBarLayout.addWidget(loanOrDevolutionFunctions)
        _navigationBarLayout.addWidget(reportsFunctions)

        # test = makeWindow("Alunos")
        # studentFunctions.clicked.connect(slot(test))

        studentWIndowContent = self.makeStudentWindowContent()
        bookWIndowContent = self.makeBookWindowContent()

        studentFunctions.clicked.connect(
            slot(_mainLayout, studentWIndowContent)
            )
        bookFunctions.clicked.connect(
            slot(_mainLayout, bookWIndowContent)
            )

    def addWindowStyle(self):
        self.setWindowTitle("Biblioteca")
        self.resize(800, 800)
        qdarktheme.setup_theme(theme="light", corner_shape="sharp")

    def makeStudentWindowContent(self):
        _layout = QFormLayout()
        _layout.addRow(QPushButton("Cadastra Aluno"))
        _layout.addRow(QPushButton("Altera Cadastro"))
        _layout.addRow(QPushButton("Relatorio - Cadastros"))
        _layout.addRow(QPushButton("Pendências"))
        return _layout

    def makeBookWindowContent(self):
        _layout = QFormLayout()
        _layout.addRow(QLineEdit("Livro:"))
        _layout.addRow(QLineEdit("Livro:"))
        _layout.addRow(QLineEdit("Livro:"))
        _layout.addRow(QLineEdit("Livro:"))
        return _layout


def slot(theMainLayout: QVBoxLayout, otherLayout: QFormLayout):
    def addOtherLayout():
        theMainLayout.addLayout(otherLayout, 1)
    return addOtherLayout


def makeWindow(windowTitle: str):
    dialog = QDialog()
    dialog.setWindowTitle(windowTitle)
    dialog.resize(300, 300)
    return dialog


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec())
