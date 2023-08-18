from PySide6.QtWidgets import QGridLayout
from mybuttons import MyButtons
from function_windows import StudentRegisterWindow
from function_windows import BookRegisterWindow


class StudentLayout(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.registerWindow = StudentRegisterWindow()
        self.changeRegisterWindow = StudentRegisterWindow(changeRegister=True)

        register = MyButtons("Cadastro - Aluno")
        changeRegister = MyButtons("Alterar Cadastro")
        makeRegisteredReport = MyButtons("Relatório de cadastros")
        deleteRegister = MyButtons("Apagar Cadastro")

        self.addWidget(register, 1, 1)
        self.addWidget(changeRegister, 2, 1)
        self.addWidget(makeRegisteredReport, 3, 1)
        self.addWidget(deleteRegister, 4, 1)

        register.clicked.connect(self.registerWindow.show)
        changeRegister.clicked.connect(self.changeRegisterWindow.show)


class BookLayout(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.registerWindow = BookRegisterWindow()
        self.changeRegisterWindow = BookRegisterWindow(changeRegister=True)

        register = MyButtons("Cadastro - Livro")
        changeRegister = MyButtons("Alterar Cadastro")
        makeRegisteredReport = MyButtons("Relatório de cadastros")
        deleteRegister = MyButtons("Apagar Cadastro")

        self.addWidget(register, 1, 1)
        self.addWidget(changeRegister, 2, 1)
        self.addWidget(makeRegisteredReport, 3, 1)
        self.addWidget(deleteRegister, 4, 1)

        register.clicked.connect(self.registerWindow.show)
        changeRegister.clicked.connect(self.changeRegisterWindow.show)


class loanAndDevolutionLayout(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        loan = MyButtons("Realizar Empréstimo")
        devolution = MyButtons("Realizar Devolução")
        makeLoanReport = MyButtons("Relatório - Empréstimos")

        self.addWidget(loan, 1, 1)
        self.addWidget(devolution, 2, 1)
        self.addWidget(makeLoanReport, 3, 1)
