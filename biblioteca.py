import os
import json
import sys
from pathlib import Path
# from typing import Optional
import qdarktheme
from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QCalendarWidget, QVBoxLayout,
    QGridLayout, QFormLayout, QWidget, QFrame,
    QApplication, QPushButton, QLabel, QDialog,
    QLineEdit, QSpinBox, QDateEdit,
    QDialogButtonBox, QMessageBox
    )

CAMINHO_DB_FILES = Path(__file__).parent / "db_files"
IDS_ALUNOS = os.path.join(CAMINHO_DB_FILES, "id_alunos.json")
INFO_ALUNOS = os.path.join(CAMINHO_DB_FILES, "info_alunos.json")
IDS_LIVROS = os.path.join(CAMINHO_DB_FILES, "id_livros.json")
INFO_LIVROS = os.path.join(CAMINHO_DB_FILES, "info_livros.json")
EMPRESTIMOS = os.path.join(CAMINHO_DB_FILES, "emprestimos.json")
ID_EMPRESTIMO = os.path.join(CAMINHO_DB_FILES, "id_emprestimo.json")
ANO_ATUAL = datetime.now().year
MES_ATUAL = datetime.now().month
DIA_ATUAL = datetime.now().day

def fazMsgBox(titulo: str,texto: str, critical: bool):
    m = QMessageBox()
    m.setWindowTitle(titulo)
    if critical:
        m.setIcon(m.Icon.Critical)
    else:
        m.setIcon(m.Icon.Information)
    m.setText(texto)
    m.exec()


class Biblioteca:

    def __init__(self) -> None:

        # Importando dados
        self.id_alunos = self.importacao(IDS_ALUNOS)
        self.info_alunos = self.importacao(INFO_ALUNOS)
        self.id_livros = self.importacao(IDS_LIVROS)
        self.info_livros = self.importacao(INFO_LIVROS)
        self.emprestimos = self.importacao(EMPRESTIMOS)
        self.id_emprestimo = self.importacao(ID_EMPRESTIMO)

    def importacao(self, caminho: str):
        with open(caminho, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        return dados

    def exportacao(self, caminho: str, dados: dict):
        with open(caminho, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=2)

    def cadastra_aluno(
            self, nome: str, idade: str, serie: str,
            turno: str, contato: str, endereco: str):

        _id = str(len(self.id_alunos))
        if _id in self.id_alunos:
            return False
        self.id_alunos.append(_id)

        self.info_alunos[_id] = {
            f"ID: {_id}, Nome: {nome.title()}, Série: {serie}, "
            f"Turno: {turno.title()}, Idade: {idade}, Contato: {contato}, "
            f"Endereço: {endereco.title()}"
        }
        self.exportacao(IDS_ALUNOS, self.id_alunos)
        self.exportacao(INFO_ALUNOS, self.info_alunos)
        return self.info_alunos[_id]

    def cadastra_livro(
            self, numeracao: str, titulo: str, genero: str,
            autor: str, editora: str, qtd: str
            ):

        self.info_livros[numeracao] = (
            f"Título: {titulo.capitalize()}, "
            f"Gênero: {genero.capitalize()}, "
            f"Autor: {autor.capitalize()}, "
            f"Editora:  {editora.capitalize()}, "
            f"Quantidade: {qtd}, Numeração: {numeracao}"
        )
        self.id_livros.append(numeracao)

        print("As informações do livro cadasrtado são:")
        print("NUMERAÇÃO: ", numeracao)
        print(self.info_livros[numeracao])

        self.exportacao(IDS_LIVROS, self.id_livros)
        self.exportacao(INFO_LIVROS, self.info_livros)
        return self.info_livros[numeracao]

    def altera_aluno(
            self, _id: str, nome: str, idade: str, serie: str,
            turno: str, contato: str, endereco: str
            ):
        
        if _id not in self.id_alunos:
            return None

        self.info_alunos[_id] = (
            f"Nome: {nome.title()}, Série: {serie}, "
            f"Turno: {turno.title()}, Idade: {idade}, Contato: {contato}, "
            f"Endereço: {endereco.title()}")
        self.exportacao(INFO_ALUNOS, self.info_alunos)
        return self.info_alunos[_id]

    def altera_livro(self, numeracao: str, titulo: str, genero: str,
                     autor: str, editora: str, qtd: str
                     ):
        if numeracao not in self.id_livros:
            return None
        self.info_livros[numeracao] = (
            f"Título: {titulo.capitalize()}, "
            f"Gênero: {genero.capitalize()}, "
            f"Autor: {autor.capitalize()}, "
            f"Editora:  {editora.capitalize()}, Quantidade: {qtd}")
        self.exportacao(INFO_LIVROS, self.info_livros)
        return self.info_livros[numeracao]

    def fazer_emprestimo(self, _id: str, livro: str, devo: str):

        chave = str(datetime.now().microsecond)

        self.emprestimos[chave] = {
            "aluno": self.info_alunos[_id],
            "livro": livro.title(),
            "devolucao": devo
        }
        self.id_emprestimo[chave] = _id
        self.exportacao(EMPRESTIMOS, self.emprestimos)
        self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)

        return chave, self.emprestimos[chave]

    def fazer_devolucao(self, chave: str):

        self.emprestimos.pop(chave)
        self.id_emprestimo.pop(chave)
        self.exportacao(EMPRESTIMOS, self.emprestimos)
        self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)


class JanelaPrincipal(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.b1 = Biblioteca()
        # Padrão
        # Criando o widget central
        self.widgetCentral = QWidget()

        # Criando janelas para cada botão
        self.janelaCA = JanelaCadastraAluno(self.b1)
        self.janelaCL = JanelaCadastroLivro(self.b1)
        self.janelaAA = JanelaAteraAluno(self.b1)
        self.janelaAL = JanelaAlteraLivro(self.b1)
        self.janelaEP = JanelaEmprestimo(self.b1)
        self.janelaDV = JanelaDevolucao(self.b1)

        # Criando os layouts da janela principal
        self.meuLayout1 = QVBoxLayout()
        self.layout_botoes = QGridLayout()
        self.criabotoes()

        # criando widget do calendário
        self.calendario = QCalendarWidget()
        self.config_estilo_calendario()

        # criando widget da barra de titulo
        self.barraTitulo = BarraTitulo()

        # adicionando barra de titulo na primeira linha do layout principal
        self.meuLayout1.addWidget(
            self.barraTitulo,
            )

        # adicionando calendario na primeira linha do segundo layout
        self.meuLayout1.addWidget(
            self.calendario,
            alignment=Qt.AlignmentFlag.AlignCenter
            )

        # Colocando o widget central no topo da hierarquia de widgets
        self.setCentralWidget(self.widgetCentral)

        self.meuLayout1.addLayout(self.layout_botoes)

        # Setando o meuLayout1 no widget central
        self.widgetCentral.setLayout(self.meuLayout1)

        self.layout_botoes.addWidget(self.CA, 0, 0)
        self.layout_botoes.addWidget(self.CL, 0, 1)
        self.layout_botoes.addWidget(self.AA, 1, 0)
        self.layout_botoes.addWidget(self.AL, 1, 1)
        self.layout_botoes.addWidget(self.EP, 2, 0)
        self.layout_botoes.addWidget(self.DV, 2, 1)

        self.config_style()

        self.CA.clicked.connect(self.janelaCA.show)

        self.CL.clicked.connect(self.janelaCL.show)

        self.AA.clicked.connect(self.janelaAA.show)

        self.AL.clicked.connect(self.janelaAL.show)

        self.EP.clicked.connect(self.janelaEP.show)

        self.DV.clicked.connect(self.janelaDV.show)

    def config_style(self):
        # Setando tamanho de 1200x800 enquanto trabalho no projeto
        self.setFixedSize(1200, 975)

        # Setando para iniciar com a tela maximizada
        # self.showMaximized()

        # Setando tamanho mínimo da tela
        # self.setMinimumSize(1200, 975)

        # Setando tema
        qdarktheme.setup_theme(
            theme='dark',
            corner_shape='rounded',
            custom_colors={
                "[dark]": {
                    "primary": f"{'#1e81b0'}",
                },
                "[light]": {
                    "primary": f"{'#1e81b0'}",
                },
            }
        )

    def config_estilo_calendario(self):
        qss = """
            QCalendarWidget {
                background-color: #f0f0f0;
                color: #333;
            }
            QCalendarWidget QToolButton {
                background-color: #1e81b0;
                color: #fff;
                border: 1px solid #1e81b0;
                min-width: 20px;
                min-height: 20px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #16658a;
            }
            QCalendarWidget QToolButton:pressed {
                background-color: #115270;
            }
        """

        self.calendario.setStyleSheet(qss)
        self.calendario.setFixedSize(600, 600)

    def criabotoes(self):
        self.CA = Botao("1 - Cadastra Aluno")
        self.CL = Botao("2 - Cadastra Livro")
        self.AA = Botao("3 - Altera Aluno")
        self.AL = Botao("4 - Altera Livro")
        self.EP = Botao("5 - Empréstimo")
        self.DV = Botao("6 - Devoluçao")


class BarraTitulo(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(45)
        self.setStyleSheet("background-color: #1e81b0; color: white;")

        layout = QVBoxLayout(self)

        self.titulo_label = QLabel("Biblioteca")
        self.titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.titulo_label)


class Botao(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        fonte = self.font()
        fonte.setPixelSize(40)
        fonte.setBold(True)
        self.setFont(fonte)


# classes para as janelas secundárias apenas com estilos
class JanelaCadastraAluno(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Cadastro de Aluno")
        self.setMinimumSize(900, 350)
        self.layoutca = QFormLayout()
        self.setLayout(self.layoutca)
        self.campo_texto = [nome := QLineEdit(), idade := QSpinBox(),
                            serie := QLineEdit(), turno := QLineEdit(),
                            contato := QLineEdit(), endereco := QLineEdit()]
        self.titulos = ["Nome Aluno", "Idade",
                        "Série", "Turno", "Contato", "Endereço"]
        for titulo, campo in enumerate(self.campo_texto):
            self.layoutca.addRow(str(self.titulos[titulo]), campo)

        self.botoes_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )

        self.layoutca.addWidget(self.botoes_box)
        self.botoes_box.accepted.connect(self.faz_slot(
            biblioteca.cadastra_aluno,
            nome, idade, serie,
            turno, contato, endereco
        ))

        self.botoes_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args):
        def slot():
            n, i, s, t, c, e = args
            msg = func(n.text(), i.text(), s.text(),
                       t.text(), c.text(), e.text())
            for b in args:
                b.clear()
            fazMsgBox("Cadastro realizado!",
                      msg,
                      False
                      )
        return slot


class JanelaCadastroLivro(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Cadastro de Livro")
        self.setMinimumSize(900, 350)
        layoutcl = QFormLayout()
        self.setLayout(layoutcl)
        layoutcl.addRow("Numeração:", numeracao := QSpinBox())
        numeracao.setRange(0, 9999999)
        layoutcl.addRow("Titulo Livro:", titulo := QLineEdit())
        layoutcl.addRow("Genero:", genero := QLineEdit())
        layoutcl.addRow("Autor:", autor := QLineEdit())
        layoutcl.addRow("Editora:", editora := QLineEdit())
        layoutcl.addRow("Quantidade:", qtd := QSpinBox())
        qtd.setRange(0, 999)
        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layoutcl.addWidget(b_box)

        b_box.accepted.connect(
            self.faz_slot(
                biblioteca.cadastra_livro,
                numeracao, titulo, genero, autor, editora, qtd
            )
        )
        b_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args):
        def slot():
            n, t, g, a, e, q = args
            msg = func(
                n.text(), t.text(), g.text(), a.text(), e.text(), q.text()
                )
            for b in args:
                b.clear()
            fazMsgBox(
                "Cadastro Realizado!",
                msg,
                False
                )
        return slot


class JanelaAteraAluno(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Altera Cadastro - Aluno")
        self.setMinimumSize(900, 350)
        layoutaa = QFormLayout()
        self.setLayout(layoutaa)
        campo_texto = [_id := QSpinBox(), nome := QLineEdit(),
                       idade := QSpinBox(), serie := QLineEdit(),
                       turno := QLineEdit(), contato := QLineEdit(),
                       endereco := QLineEdit()]
        _id.setRange(0, 999999)
        titulos = ["ID", "Nome Aluno", "Idade",
                   "Série", "Turno", "Contato", "Endereço"]
        for titulo, campo in enumerate(campo_texto):
            layoutaa.addRow(str(titulos[titulo]), campo)

        self.botoes_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )
        
        layoutaa.addWidget(self.botoes_box)
        self.botoes_box.accepted.connect(self.faz_slot(
            biblioteca.altera_aluno,
            _id, nome, idade, serie,
            turno, contato, endereco
        ))

        self.botoes_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args: Botao):
        def slot():
            __id, n, i, s, t, c, e = args
            msg = func(__id.text(), n.text(), i.text(), s.text(),
                    t.text(), c.text(), e.text())
            if msg is None:
                fazMsgBox("ERRO!", "O ID digitado não existe.", True)
                return slot
            for b in args:
                b.clear()
            fazMsgBox("Cadastro atualizado!", msg, False)
        return slot


class JanelaAlteraLivro(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Altera Cadastro - Livro")
        self.setMinimumSize(900, 350)
        layoutcl = QFormLayout()
        self.setLayout(layoutcl)
        layoutcl.addRow("Numeração:", numeracao := QSpinBox())
        numeracao.setRange(0, 9999999)
        layoutcl.addRow("Titulo Livro:", titulo := QLineEdit())
        layoutcl.addRow("Genero:", genero := QLineEdit())
        layoutcl.addRow("Autor:", autor := QLineEdit())
        layoutcl.addRow("Editora:", editora := QLineEdit())
        layoutcl.addRow("Quantidade:", qtd := QSpinBox())
        qtd.setRange(0, 999)
        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layoutcl.addWidget(b_box)

        b_box.accepted.connect(
            self.faz_slot(
                biblioteca.altera_livro,
                numeracao, titulo, genero, autor, editora, qtd
            )
        )
        b_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args):
        def slot():
            n, t, g, a, e, q = args
            msg = func(
                n.text(), t.text(), g.text(), a.text(), e.text(), q.text()
                )
            for b in args:
                b.clear()
            if msg is None:
                fazMsgBox("ERRO!", "ID não encontrado.", True)
                return
            fazMsgBox("Cadastro Alterado!", msg, False)
        return slot


class JanelaEmprestimo(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Empréstimo")
        self.setMinimumSize(900, 350)
        layoutep = QFormLayout()
        self.setLayout(layoutep)

        layoutep.addRow("ID do ALuno:", _id := QSpinBox())
        _id.setRange(0, 9999999)

        layoutep.addRow("Livro:", livro := QLineEdit())
        layoutep.addRow("Devolução:", data := QDateEdit())
        data.setCalendarPopup(True)

        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layoutep.addWidget(b_box)

        b_box.accepted.connect(self.faz_slot(
            biblioteca.fazer_emprestimo, _id, livro, data
        ))
        b_box.rejected.connect(self.reject)

    def faz_slot(self, func, *args):
        def slot():
            i, l, d = args
            chave, msg = func(i.text(), l.text(), d.text())
            for b in args:
                b.clear()
            fazMsgBox(
                "Empréstimo Realizado!",
                f"CHAVE DA DEVOLUÇÃO: {chave}\nINFO ALUNO: {msg}",
                False
                )
        return slot


class JanelaDevolucao(QDialog):
    def __init__(self, biblioteca: Biblioteca, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Devolução")
        self.setMinimumSize(600, 350)
        layoutdv = QFormLayout()
        self.setLayout(layoutdv)

        layoutdv.addRow("Chave da Devolução:", chave := QSpinBox())
        chave.setRange(0, 9999999)

        b_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layoutdv.addWidget(b_box)

        b_box.accepted.connect(self.faz_slot(
            biblioteca.fazer_devolucao,
            chave
        ))
        b_box.rejected.connect(self.reject)

    def faz_slot(self, func, chave):
        def slot():
            try:
                func(chave.text())
                chave.clear()
                fazMsgBox(
                    "Devolução Realizada!",
                    "Devolução bem sucedida.",
                    False
                    )
            except KeyError:
                fazMsgBox(
                    "Falha!",
                    "Devolução mal sucedida.\nERRO: CHAVE NÃO ENCONTRADA",
                    True
                    )
        return slot


if __name__ == "__main__":
    app = QApplication(sys.argv)

    janelaCentral = JanelaPrincipal()

    janelaCentral.show()
    sys.exit(app.exec())
