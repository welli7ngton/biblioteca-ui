from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout,
                               QMenu, QHBoxLayout, QPushButton)
import json
import sys
import os


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
        self.studentsDatas = self.dataImport(FILE_PATH_STUDENTS)
        self.booksDatas = self.dataImport(FILE_PATH_BOOKS)

    def dataImport(self, filePath: str):
        with open(filePath, "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas

    def dataExport(self, studentOrBook: Student | Book):
        __filePath,__dict = (FILE_PATH_STUDENTS, self.studentsDatas)\
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
        _mainLayout = QGridLayout()

        # criando widget da barra de navegação de páginas e layout
        _navigationBarWidget = QWidget()
        _navigationBarLayout = QHBoxLayout()

        # setando o layout do widget central
        _centralWidget.setLayout(_mainLayout)

        # setando o layout da barra de navegação
        _navigationBarWidget.setLayout(_navigationBarLayout)

        #setando o widget central na janela do programa
        self.setCentralWidget(_centralWidget)

        # adicionando a barra de navegação no layout principal do programa
        _mainLayout.addWidget(
            _navigationBarWidget,
            1,
            1,
            Qt.AlignmentFlag.AlignTop
            )

        _navigationBarLayout.addWidget(NavigationBarButtons("Cadastro"))
        _navigationBarLayout.addWidget(NavigationBarButtons("Empréstimo"))
        _navigationBarLayout.addWidget(NavigationBarButtons("Devolução"))



    def addWindowStyle(self):
        self.setWindowTitle("Biblioteca")
        self.setMinimumSize(800, 800)
        # self.setStyleSheet("background-color: #000")
        

class NavigationBarButtons(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        qss = """
            QpushButton: {
            font-size: 80px
            margin: 0px
            padding: 0px
            background-color: #000
            }
        """

        self.setStyleSheet(qss)

        # self.setStyleSheet("font-size: 50px")
        # self.setStyleSheet("color: f00")
        # self.setStyleSheet("border-radius: 20px")
        
        #TODO: estilizar barra de navegação.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()


    mainWindow.show()
    sys.exit(app.exec())
