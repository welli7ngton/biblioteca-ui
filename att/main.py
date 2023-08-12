
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton,
    QDialog, QVBoxLayout,  QFormLayout,  QLineEdit
    )
import json
import sys
import qdarktheme

FILE_PATH_STUDENTS = "att/jsonfiles/students.json"
FILE_PATH_BOOKS = "att/jsonfiles/books.json"


class Student:
    def __init__(self) -> None:
        pass

    @property
    def setName(self):
        return self._name

    @setName.setter
    def setName(self, value: str):
        self._name = value.title()

    @property
    def setAge(self):
        return self._age

    @setAge.setter
    def setAge(self, value: int):
        self._age = value

    @property
    def setAdress(self):
        return self._adress

    @setAdress.setter
    def setAdress(self, value: str):
        self._adress = value.title()

    @property
    def setContactNumber(self):
        return self._contactNumber

    @setContactNumber.setter
    def setContactNumber(self, value: str):
        self._contactNumber = value

    @property
    def setShift(self):
        return self._shift

    @setShift.setter
    def setShift(self, value: str):
        self._shift = value.capitalize()

    @property
    def setGradeYear(self):
        return self._gradeYear

    @setGradeYear.setter
    def setGradeYear(self, value: str):
        self._gradeYear = value


class Book:
    def __init__(self) -> None:
        pass

    @property
    def setTitle(self):
        return self._title

    @setTitle.setter
    def setTitle(self, value: str):
        self._title = value.title()

    @property
    def setGender(self):
        return self._gender

    @setGender.setter
    def setGender(self, value: str):
        self._gender = value.title()

    @property
    def setAuthor(self):
        return self._author

    @setAuthor.setter
    def setAuthor(self, value: str):
        self._author = value.capitalize()

    @property
    def setPublishingCompany(self):
        return self._publishingCompany

    @setPublishingCompany.setter
    def setPublishingCompany(self, value: str):
        self._publishingCompany = value.capitalize()

    @property
    def setAmount(self):
        return self._amount

    @setAmount.setter
    def setAmount(self, value: int):
        self._amount = value


class Library:
    def __init__(self) -> None:
        self.studentsDatas = self.__dataImport(FILE_PATH_STUDENTS)
        self.booksDatas = self.__dataImport(FILE_PATH_BOOKS)

    def __dataImport(self, filePath: str):
        with open(filePath, "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas

    def __dataExport(self, studentOrBook: Student | Book):
        __filePath, __dict = (FILE_PATH_STUDENTS, self.studentsDatas)\
              if isinstance(studentOrBook, Student)\
              else (FILE_PATH_BOOKS, self.booksDatas)

        attributes = [
            attr for attr in dir(studentOrBook)
            if not attr.startswith("__")
            and not attr.startswith("set")
            ]

        dictionaryKeyAttributes = [
            attr.replace("set", "") for attr in dir(studentOrBook)
            if attr.startswith("set")
            ]

        objectData = dict()
        for i in range(len(attributes)):
            objectData[dictionaryKeyAttributes[i]] = getattr(
                studentOrBook,
                attributes[i]
                )

        __dict[len(__dict)] = objectData
        with open(__filePath, "w", encoding="utf-8") as file:
            json.dump(
                __dict,
                file,
                ensure_ascii=False,
                indent=2
                )


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
        _mainLayout.addWidget(_navigationBarWidget, alignment=Qt.AlignmentFlag.AlignTop)

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

        studentFunctions.clicked.connect(slot(_mainLayout, studentWIndowContent))
        bookFunctions.clicked.connect(slot(_mainLayout, bookWIndowContent))

    def addWindowStyle(self):
        self.setWindowTitle("Biblioteca")
        self.resize(800, 800)
        qdarktheme.setup_theme(theme="light", corner_shape="sharp")

    def makeStudentWindowContent(self):
        _layout = QFormLayout()
        _layout.addRow(name := QPushButton("Cadastra Aluno"))
        _layout.addRow(age := QPushButton("Altera Cadastro"))
        _layout.addRow(adress := QPushButton("Relatorio - Cadastros"))
        _layout.addRow(contact := QPushButton("Pendências"))
        return _layout

    def makeBookWindowContent(self):
        _layout = QFormLayout()
        _layout.addRow(name := QLineEdit("Livro:"))
        _layout.addRow(age := QLineEdit("Livro:"))
        _layout.addRow(adress := QLineEdit("Livro:"))
        _layout.addRow(contact := QLineEdit("Livro:"))
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
