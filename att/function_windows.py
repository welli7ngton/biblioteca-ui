from PySide6.QtWidgets import (
    QFormLayout, QDialogButtonBox, QLineEdit, QSpinBox, QDialog
)


class BaseRegisterWindow(QDialog):
    def __init__(self, windowName: str, fields: list) -> None:
        super().__init__()
        self.setWindowTitle(windowName)
        self.setFixedSize(600, 400)

        _layout = QFormLayout()
        self.setLayout(_layout)
        self.fields = {}

        for field_name, field_widget in fields:
            field_widget = field_widget()
            self.fields[field_name] = field_widget
            _layout.addRow(field_name + ":", field_widget)

        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        _layout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


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
            return super().__init__("Altera cadastro", fields)
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
            return super().__init__("Altera Cadastro", fields)
        fields = [
                ("Título", QLineEdit),
                ("Autor", QLineEdit),
                ("Editora", QLineEdit),
                ("Genero", QLineEdit),
                ("Quantidade", QSpinBox),
            ]
        super().__init__("Cadastro de Livro", fields)
