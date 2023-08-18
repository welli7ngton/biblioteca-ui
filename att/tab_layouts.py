from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from mybuttons import MyButtons


class StudentLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        register = MyButtons("Cadastrar Aluno")
        changeRegister = MyButtons("Alterar Cadastro")
        makeRegisteredReport = MyButtons("Relatório de cadastros")
        deleteRegister = MyButtons("Apagar Cadastro")

        self.addWidget(
            register,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.addWidget(
            changeRegister,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.addWidget(
            makeRegisteredReport,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.addWidget(
            deleteRegister,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
