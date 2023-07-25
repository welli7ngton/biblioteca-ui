import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        a = {
            "0": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "1": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "2": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "3": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "4": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "5": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "6": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01",
            "7": "Nome: Wellington Silva, Série: 8, Turno: Manhã, Idade: 20, Contato: 99 9 9999-9999, Endereço: Rua 01"
            }
        layout = QVBoxLayout()

        # Criando o QListWidget
        self.lista_itens = QListWidget()
        for i in a:
            # Adicionando alguns itens à lista
            self.lista_itens.addItem(a[i])
            self.lista_itens.addItem(" ")

        # Definindo o modo de seleção para seleção única (QAbstractItemView.SingleSelection)
        self.lista_itens.setSelectionMode(QListWidget.SingleSelection)

        layout.addWidget(self.lista_itens)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setWindowTitle("Exemplo de QListWidget")
    window.show()
    sys.exit(app.exec_())