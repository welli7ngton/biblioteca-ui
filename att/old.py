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
            if verifica_campos(*args):
                msg = func(n.text(), i.text(), s.text(),
                           t.text(), c.text(), e.text())
                for b in args:
                    b.clear()
                faz_msg_box(
                    "Cadastro realizado!", str(msg), False
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
        qtd.setRange(0, 9999)
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
            if verifica_campos(*args):
                msg = func(
                    n.text(), t.text(), g.text(), a.text(), e.text(), q.text()
                    )
                for b in args:
                    b.clear()
                faz_msg_box(
                    "Cadastro Realizado!", str(msg), False
                    )
        return slot
