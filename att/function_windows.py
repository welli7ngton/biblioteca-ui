from PySide6.QtWidgets import (
    QFormLayout, QDialogButtonBox, QLineEdit, QSpinBox, QDialog, QMessageBox
)
from student_and_book import (
    Student, Book
)
from database import DataBase

STUDENT = Student()
BOOK = Book()
DATABASE = DataBase()


class BaseWindow(QDialog):
    def __init__(self, windowName: str, fields: list[tuple]) -> None:
        super().__init__()
        self.setWindowTitle(windowName)
        self.setFixedSize(600, 400)
        _layout = QFormLayout()
        self.setLayout(_layout)
        self.fields = {}

        for field_name, field_widget in fields:
            field_widget = field_widget()
            self.fields[field_name] = field_widget
            if "ID" in field_name or "Quantidade" in field_name:
                field_widget.setRange(0, 9999999)
            _layout.addRow(field_name + ":", field_widget)

        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        _layout.addWidget(self.buttonBox)

        if windowName == "Cadastro de Aluno":
            self.buttonBox.accepted.connect(self._getNewStundetInfos)
        elif windowName == "Altera Cadastro - Aluno":
            self.buttonBox.accepted.connect(self._getChangesStudent)
        elif windowName == "Cadastro de Livro":
            self.buttonBox.accepted.connect(self._getNewBookInfos)
        elif windowName == "Altera Cadastro - Livro":
            self.buttonBox.accepted.connect(self._getChangesBook)
        elif windowName == "Apagar Cadastro - Aluno":
            self.buttonBox.accepted.connect(self._deleteStudentRegister)
        elif windowName == "Apagar Cadastro - Livro":
            self.buttonBox.accepted.connect(self._deleteBookRegister)
        elif windowName == "Realizar Empréstimo":
            self.buttonBox.accepted.connect(self._registerLoan)
        elif windowName == "Realizar Devolução":
            self.buttonBox.accepted.connect(self._deleteLoan)

        self.buttonBox.rejected.connect(self.reject)

    def _getNewStundetInfos(self):
        attributes = []
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()

        STUDENT.setName = attributes[0]
        STUDENT.setAge = int(attributes[1])
        STUDENT.setAdress = attributes[2]
        STUDENT.setContactNumber = attributes[3]
        STUDENT.setShift = attributes[4]
        STUDENT.setGradeYear = attributes[5]
        DATABASE.registerStudent(STUDENT)
        self._makeMessageBox("Cadastro Realizado!", attributes)

    def _getNewBookInfos(self):
        attributes = []
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()

        BOOK.setTitle = attributes[0]
        BOOK.setAuthor = attributes[1]
        BOOK.setPublishingCompany = attributes[2]
        BOOK.setGender = attributes[3]
        BOOK.setAmount = int(attributes[4])
        DATABASE.registerBook(BOOK)
        self._makeMessageBox("Cadastro Realizado!", attributes)

    def _getChangesStudent(self):
        attributes = []
        STUDENT = Student()
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        print(attributes)
        _id = int(attributes[0])
        STUDENT.setName = attributes[1]
        STUDENT.setAge = int(attributes[2])
        STUDENT.setAdress = attributes[3]
        STUDENT.setContactNumber = attributes[4]
        STUDENT.setShift = attributes[5]
        STUDENT.setGradeYear = attributes[6]
        DATABASE.changeRegisterStudent(_id, STUDENT)
        self._makeMessageBox("Cadastro Atualizado!", attributes[1:])

    def _getChangesBook(self):
        attributes = []

        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        _id = int(attributes[0])
        BOOK.setTitle = attributes[1]
        BOOK.setAuthor = attributes[2]
        BOOK.setPublishingCompany = attributes[3]
        BOOK.setGender = attributes[4]
        BOOK.setAmount = int(attributes[5])
        DATABASE.changeRegisterBook(_id, BOOK)
        self._makeMessageBox("Cadastro Atualizado!", attributes[1:])

    def _deleteStudentRegister(self):
        for field in self.fields.values():
            _id = field.text()
        try:
            DATABASE.deleteRegister(int(_id), "students", "student_id")
        except Exception as e:
            if "ID NÃO EXISTE" in str(e):
                self._makeMessageBox(
                    "Cadastro Não Encontrado!",
                    "O ID informado aparenta não existir, "
                    "revise o ID e tente novamente."
                )
                return
        self._makeMessageBox(
            "Cadastro Apagado!",
            "Registros do Aluno foram apagados do sistema."
        )

    def _deleteBookRegister(self):
        for field in self.fields.values():
            _id = field.text()

        try:
            DATABASE.deleteRegister(int(_id), "books", "book_id")
        except Exception as e:
            if "ID NÃO EXISTE" in str(e):
                self._makeMessageBox(
                    "Cadastro Não Encontrado!",
                    "O ID informado aparenta não existir, "
                    "revise o ID e tente novamente."
                )
                return
        self._makeMessageBox(
            "Cadastro Apagado!",
            "Registros do Livro foram apagados do sistema."
        )

    def _registerLoan(self):
        attributes = []

        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        studentID = int(attributes[0])
        bookID = int(attributes[0])
        devolutionDate = int(attributes[0])
        DATABASE.registerLoan(studentID, bookID, devolutionDate)
        self._makeMessageBox("Cadastro Realizado!", attributes)

    def _deleteLoan(self):
        for field in self.fields.values():
            _id = field.text()

        try:
            DATABASE.deleteRegister(int(_id), "loan", "loan_id")
        except Exception as e:
            if "ID NÃO EXISTE" in str(e):
                self._makeMessageBox(
                    "Cadastro Não Encontrado!",
                    "O ID informado aparenta não existir, "
                    "revise o ID e tente novamente."
                )
                return
        self._makeMessageBox(
            "Devolução Realizada!",
            "Registros foram apagados do sistema."
        )

    def _makeMessageBox(self, _title: str, _content: list):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(_title)
        messageBox.setIcon(messageBox.Icon.Information)
        messageBox.setText(
            "Informações:"
            f"{_content}"
        )
        messageBox.exec()


class StudentRegisterWindow(BaseWindow):
    def __init__(self, changeRegister=False):
        if changeRegister:
            fields = [
                ("ID", QSpinBox),
                ("Nome", QLineEdit),
                ("Idade", QSpinBox),
                ("Endereço", QLineEdit),
                ("Contato", QLineEdit),
                ("Turno", QLineEdit),
                ("Série", QLineEdit)
            ]
            return super().__init__("Altera Cadastro - Aluno", fields)
        fields = [
            ("Nome", QLineEdit),
            ("Idade", QSpinBox),
            ("Endereço", QLineEdit),
            ("Contato", QLineEdit),
            ("Turno", QLineEdit),
            ("Série", QLineEdit)
        ]
        super().__init__("Cadastro de Aluno", fields)


class BookRegisterWindow(BaseWindow):
    def __init__(self, changeRegister=False):
        if changeRegister:
            fields = [
                ("ID", QSpinBox),
                ("Título", QLineEdit),
                ("Autor", QLineEdit),
                ("Editora", QLineEdit),
                ("Genero", QLineEdit),
                ("Quantidade", QSpinBox),
            ]
            return super().__init__("Altera Cadastro - Livro", fields)
        fields = [
                ("Título", QLineEdit),
                ("Autor", QLineEdit),
                ("Editora", QLineEdit),
                ("Genero", QLineEdit),
                ("Quantidade", QSpinBox),
            ]
        super().__init__("Cadastro de Livro", fields)


class DeleteRegisterWindow(BaseWindow):
    def __init__(self, _type: str) -> None:
        super().__init__("Apagar Cadastro" + " - " + _type, [("ID", QSpinBox)])


class LoanANdDevolutionWindow(BaseWindow):
    def __init__(self, makeLoan=False):
        if not makeLoan:
            fields = [
                ("ID Empréstimo", QSpinBox),
            ]
            return super().__init__("Realizar Devolução", fields)
        fields = [
                ("ID Aluno", QSpinBox),
                ("ID Livro", QSpinBox),
                ("Periodo do empréstimo", QSpinBox),
            ]
        super().__init__("Realizar Empréstimo", fields)
