from PySide6.QtWidgets import (
    QFormLayout, QDialogButtonBox, QLineEdit, QSpinBox, QDialog, QMessageBox
)
from student_and_book import (
    Student, Book
)
from database import DataBase


class BaseRegisterWindow(QDialog):
    def __init__(self, windowName: str, fields: list[tuple]) -> None:
        super().__init__()
        self.setWindowTitle(windowName)
        self.setFixedSize(600, 400)
        self.db = DataBase()
        _layout = QFormLayout()
        self.setLayout(_layout)
        self.fields = {}

        for field_name, field_widget in fields:
            field_widget = field_widget()
            self.fields[field_name] = field_widget
            if field_name == "ID" or field_name == "Quantidade":
                field_widget.setRange(0, 9999999)
            _layout.addRow(field_name + ":", field_widget)

        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        _layout.addWidget(self.buttonBox)

        if windowName == "Cadastro de Aluno":
            self.buttonBox.accepted.connect(self.getNewStundetInfos)
        elif windowName == "Altera Cadastro - Aluno":
            self.buttonBox.accepted.connect(self.getChangesStudent)
        elif windowName == "Cadastro de Livro":
            self.buttonBox.accepted.connect(self.getNewBookInfos)
        elif windowName == "Altera Cadastro - Livro":
            self.buttonBox.accepted.connect(self.getChangesBook)
        elif windowName == "Apagar Cadastro - Aluno":
            self.buttonBox.accepted.connect(self.deleteStudentRegister)
        elif windowName == "Apagar Cadastro - Livro":
            self.buttonBox.accepted.connect(self.deleteBookRegister)

        self.buttonBox.rejected.connect(self.reject)

    def getNewStundetInfos(self):
        attributes = []
        _student = Student()
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()

        _student.setName = attributes[0]
        _student.setAge = int(attributes[1])
        _student.setAdress = attributes[2]
        _student.setContactNumber = attributes[3]
        _student.setShift = attributes[4]
        _student.setGradeYear = attributes[5]
        self.db.registerStudent(_student)
        self._makeMessageBox("Cadastro Realizado!", attributes)
        self.db._closeConnectionAndCursor()

    def getNewBookInfos(self):
        attributes = []
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        _book = Book()
        _book.setTitle = attributes[0]
        _book.setAuthor = attributes[1]
        _book.setPublishingCompany = attributes[2]
        _book.setGender = attributes[3]
        _book.setAmount = int(attributes[4])
        self.db.registerBook(_book)
        self.db._closeConnectionAndCursor()
        self._makeMessageBox("Cadastro Realizado!", attributes)

    def getChangesStudent(self):
        attributes = []
        _student = Student()
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        print(attributes)
        _id = int(attributes[0])
        _student.setName = attributes[1]
        _student.setAge = int(attributes[2])
        _student.setAdress = attributes[3]
        _student.setContactNumber = attributes[4]
        _student.setShift = attributes[5]
        _student.setGradeYear = attributes[6]
        self.db.changeRegisterStudent(_id, _student)
        self._makeMessageBox("Cadastro Atualizado!", attributes[1:])
        self.db._closeConnectionAndCursor()

    def getChangesBook(self):
        attributes = []
        _book = Book()
        for field in self.fields.values():
            attributes.append(field.text())
            field.clear()
        _id = int(attributes[0])
        _book.setTitle = attributes[1]
        _book.setAuthor = attributes[2]
        _book.setPublishingCompany = attributes[3]
        _book.setGender = attributes[4]
        _book.setAmount = int(attributes[5])
        self.db.changeRegisterBook(_id, _book)
        self._makeMessageBox("Cadastro Atualizado!", attributes[1:])
        self.db._closeConnectionAndCursor()

    def deleteStudentRegister(self):
        for field in self.fields.values():
            _id = field.text()
        try:
            self.db.deleteRegister(int(_id), "students", "student_id")
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

    def deleteBookRegister(self):
        for field in self.fields.values():
            _id = field.text()

        try:
            self.db.deleteRegister(int(_id), "books", "book_id")
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

    def _makeMessageBox(self, _title: str, _content: list):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(_title)
        messageBox.setIcon(messageBox.Icon.Information)
        messageBox.setText(
            "informações adicionadas:"
            f"{_content}"
        )
        messageBox.exec()


class StudentRegisterWindow(BaseRegisterWindow):
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


class BookRegisterWindow(BaseRegisterWindow):
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


class DeleteRegisterWindow(BaseRegisterWindow):
    def __init__(self, _type: str) -> None:
        super().__init__("Apagar Cadastro" + " - " + _type, [("ID", QSpinBox)])
