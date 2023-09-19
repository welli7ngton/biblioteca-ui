from PySide6.QtWidgets import (
    QMainWindow, QWidget, QTabWidget, QGridLayout, QCalendarWidget, QGroupBox,
    QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QLabel
)

from function_windows import (
    StudentRegisterWindow,
    BookRegisterWindow,
    DeleteRegisterWindow,
    LoanANdDevolutionWindow
)

from PySide6.QtCore import Qt

from mybuttons import MyButtons
from database import DataBase
import qdarktheme
import json


db = DataBase()
STUDENTS_INFO = db._getTableInfo("students")
BOOKS_INFO = db._getTableInfo("books")
LOAN_INFO = db._getTableInfo("loan")
db._closeConnectionAndCursor()

with open("./att/theme_configs/theme.json", "r") as file:
    THEME = json.load(file)


def changeTheme(func, theme: str):
    def slot():
        func(theme)
        with open(
            "./att/theme_configs/theme.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(theme, file, ensure_ascii=False, indent=2)
    return slot


def createTable(headerLabels: list[str], infos: list[tuple]) -> QTableWidget:
    table = QTableWidget()
    table.setColumnCount(len(headerLabels))
    table.setHorizontalHeaderLabels(headerLabels)
    table.horizontalHeader().setStretchLastSection(True)
    table.setEditTriggers(QTableWidget.NoEditTriggers)
    table.setFixedHeight(500)
    table.setFixedWidth(1300)
    table.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch
    )
    for i in range(0, len(infos)):
        table.insertRow(i)
        for j in range(0, len(infos[i])):
            table.setItem(
                i,
                j,
                QTableWidgetItem(str(infos[i][j]))
            )
    return table


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Biblioteca")
        self.resize(900, 800)
        self.setCentralWidget(self.createTabWidget())
        qdarktheme.setup_theme(THEME)

    def createTabWidget(self) -> QTabWidget:
        _tabWidget = QTabWidget()
        initialTab = QWidget()
        initialTabLayout = InitialLayout()
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


class StudentLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.registerWindow = StudentRegisterWindow()
        self.changeRegisterWindow = StudentRegisterWindow(changeRegister=True)
        self.deleteRefisterWindow = DeleteRegisterWindow("Aluno")

        register = MyButtons("Cadastro")
        changeRegister = MyButtons("Alterar Cadastro")
        deleteRegister = MyButtons("Apagar Cadastro")
        tableIndex = [
                "ID",
                "NOME",
                "IDADE",
                "CONTATO",
                "ENDEREÇO",
                "TURNO",
                "SÉRIE"
        ]
        self.studentTable = createTable(tableIndex, STUDENTS_INFO)

        self.addWidget(
            self.studentTable, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.addWidget(register, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(changeRegister, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(deleteRegister, alignment=Qt.AlignmentFlag.AlignCenter)

        register.clicked.connect(self.registerWindow.show)
        changeRegister.clicked.connect(self.changeRegisterWindow.show)
        deleteRegister.clicked.connect(self.deleteRefisterWindow.show)


class BookLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.registerWindow = BookRegisterWindow()
        self.changeRegisterWindow = BookRegisterWindow(changeRegister=True)
        self.deleteRegisterwindow = DeleteRegisterWindow("Livro")
        tableIndex = [
            "ID",
            "TÍTULO",
            "AUTOR",
            "EDITORA",
            "GÊNERO",
            "QUANTIDADE"
        ]
        self.bookTable = createTable(tableIndex, BOOKS_INFO)

        self.addWidget(
            self.bookTable, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        register = MyButtons("Cadastro")
        changeRegister = MyButtons("Alterar Cadastro")
        deleteRegister = MyButtons("Apagar Cadastro")

        self.addWidget(register, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(changeRegister, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(deleteRegister, alignment=Qt.AlignmentFlag.AlignCenter)

        register.clicked.connect(self.registerWindow.show)
        changeRegister.clicked.connect(self.changeRegisterWindow.show)
        deleteRegister.clicked.connect(self.deleteRegisterwindow.show)


class loanAndDevolutionLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.makeLoanWindow = LoanANdDevolutionWindow(True)
        self.makeDevolution = LoanANdDevolutionWindow()
        tableIndex = [
                "ID EMPŔESTIMO",
                "ID ALUNO",
                "ID LIVRO",
                "DATA EMPRÉSTIMO",
                "DATA DEVOLUÇÃO"
            ]
        self.loanTable = createTable(tableIndex, LOAN_INFO)

        self.addWidget(
            self.loanTable, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        loan = MyButtons("Realizar Empréstimo")
        devolution = MyButtons("Realizar Devolução")

        self.addWidget(loan, alignment=Qt.AlignmentFlag.AlignCenter)
        self.addWidget(devolution, alignment=Qt.AlignmentFlag.AlignCenter)

        loan.clicked.connect(self.makeLoanWindow.show)
        devolution.clicked.connect(self.makeDevolution.show)


class InitialLayout(QVBoxLayout):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        label = QLabel("Escolha o tema:")

        font = label.font()

        font.setPixelSize(32)
        label.setFont(font)
        label.setFixedHeight(40)
        self.addWidget(label, 2, Qt.AlignmentFlag.AlignHCenter)

        theme_group = QGroupBox()
        theme_layout = QGridLayout()
        theme_group.setLayout(theme_layout)
        theme_group.setFixedHeight(120)
        theme_group.setFixedWidth(900)
        dark_btn = MyButtons("Tema Escuro")
        light_btn = MyButtons("Tema Claro")

        dark_btn.setFixedWidth(400)
        light_btn.setFixedWidth(400)

        theme_layout.addWidget(dark_btn, 0, 0)
        theme_layout.addWidget(light_btn, 0, 1)

        dark_btn.clicked.connect(changeTheme(qdarktheme.setup_theme, "dark"))
        light_btn.clicked.connect(changeTheme(qdarktheme.setup_theme, "light"))

        self.addWidget(theme_group, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.addWidget(
            self.myCalendar(), 1, Qt.AlignmentFlag.AlignHCenter
        )

    def myCalendar(self):
        c = QCalendarWidget()
        c.setFixedWidth(500)
        c.setFixedHeight(500)
        return c
