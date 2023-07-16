import os
import json
from variaveis import CAMINHO_DB_FILES
from datetime import datetime
# from utils import converte_data_p_str

IDS_ALUNOS = os.path.join(CAMINHO_DB_FILES, "id_alunos.json")
INFO_ALUNOS = os.path.join(CAMINHO_DB_FILES, "info_alunos.json")
IDS_LIVROS = os.path.join(CAMINHO_DB_FILES, "id_livros.json")
INFO_LIVROS = os.path.join(CAMINHO_DB_FILES, "info_livros.json")
EMPRESTIMOS = os.path.join(CAMINHO_DB_FILES, "emprestimos.json")
ID_EMPRESTIMO = os.path.join(CAMINHO_DB_FILES, "id_emprestimo.json")
ANO_ATUAL = datetime.now().year


class Biblioteca:

    def __init__(self) -> None:

        # Importando dados
        self.id_alunos = self.importacao(IDS_ALUNOS)
        self.info_alunos = self.importacao(INFO_ALUNOS)
        self.id_livros = self.importacao(IDS_LIVROS)
        self.info_livros = self.importacao(INFO_LIVROS)
        self.emprestimos = self.importacao(EMPRESTIMOS)
        self.id_emprestimo = self.importacao(ID_EMPRESTIMO)
        for i, j in self.id_emprestimo.items():
            print(i, j)

    def importacao(self, caminho):
        with open(caminho, "r") as arq:
            dados = json.load(arq)
        return dados

    def exportacao(self, caminho, dados):
        with open(caminho, "w") as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=2)

    def cadastra_aluno(self):
        _id = str(len(self.id_alunos))
        if _id in self.id_alunos:
            return False
        self.id_alunos.append(_id)
        print("ID =", _id)

        # ########### change ########### #
        nome = input("Nome do Aluno: ")
        idade = int(input("Idade: "))
        serie = input("Série: ")
        turno = input("Turno: ")
        contato = input("Contato (00 0 0000-0000): ")
        print("Endereço: Rua, Bairro, Número.:")
        endereco = input()
        # ########### change ########### #

        self.info_alunos[_id] = (
            f"Nome: {nome.capitalize()}, Série: {serie}, "
            f"Turno: {turno}, Idade: {idade}, Contato: {contato}, "
            f"Endereço: {endereco.capitalize()}"
        )

        self.exportacao(IDS_ALUNOS, self.id_alunos)
        self.exportacao(INFO_ALUNOS, self.info_alunos)

    def cadastra_livro(self):

        titulo_livro = input("Digite o título do livro: ")
        genero = input("Digite o gênero do livro: ")
        autor = input("Digite o Autor: ")
        editora = input("Digite a Editora: ")
        qtd = input("Digite a quantidade: ")

        # verificando se a quantidade é um valor numérico
        while True:
            if qtd.isdigit() is False:
                qtd = input("Digite um valor válido, um número: ")
            else:
                break
        _id = input("Digite a numeração do livro: ")
        # verificando se a numeração do livro é um valor numérico
        while True:
            if _id.isdigit():
                while True:
                    if _id not in self.id_livros and _id.isdigit():
                        break
                    else:
                        print("Livro já cadastrado ou numeração inválida.")
                        _id = input("Digite uma numeração válida: ")
                break
            else:
                print("Digite uma numeração válida.")
        # atualizando dicionário
        self.info_livros[_id] = (
            f"Título: {titulo_livro.capitalize()}, "
            f"Gênero: {genero.capitalize()}, "
            f"Autor: {autor.capitalize()}, "
            f"Editora:  {editora.capitalize()}, "
            f"Quantidade: {qtd}, Numeração: {_id}"
        )
        self.id_livros.append(_id)

        print()
        print("As informações do livro cadasrtado são:")
        print("NUMERAÇÃO: ", _id)
        print(self.info_livros[_id])
        print()
        self.exportacao(IDS_LIVROS, self.id_livros)
        self.exportacao(INFO_LIVROS, self.info_livros)

    def altera_aluno(self):
        while True:
            verificador = input("Digite o ID do Aluno que quer alterar: ")
            if verificador not in self.id_alunos:
                print(
                    "Aluno não cadastrado ou numeração inválida, "
                    "revise e digite uma numeração válida."
                    )
                continue
            else:
                print("O cadastro que vai ser alterado é:")
                print(self.info_alunos[verificador])
                print("Digite as alterações:")
                nome = input("Nome do Aluno: ")
                serie = str(input("Série: "))
                turno = input("Turno: ")
                idade = int(input("Idade: "))
                print("Contato: 00 0 0000 0000")
                contato = input()
                print("Endereço: Rua, Bairro, Número.:")
                endereco = input()
                # atualizando dicionário
                self.info_alunos[verificador] = (
                    f"Nome: {nome.capitalize()}, Série: {serie}, "
                    f"Turno: {turno}, Idade: {idade}, Contato: {contato}, "
                    f"Endereço: {endereco.capitalize()}")
                self.exportacao(INFO_ALUNOS, self.info_alunos)
                break

    def altera_livro(self):
        while True:
            numeracao = input("Digite a numeração do livro que quer alterar: ")
            if numeracao not in self.id_livros:
                print(
                    "Livro não cadastrado ou numeração inválida, "
                    "revise e digite uma numeração válida."
                    )
                continue
            else:
                print("O livro que vai ser alterado é:")
                print(self.info_livros[numeracao])
                print("Digite as alterações:")

                # cadastro de alterações
                titulo_livro = input("Digite o título do livro: ")
                genero = input("Digite o gênero do livro: ")
                autor = input("Digite o Autor: ")
                editora = input("Digite a Editora: ")
                qtd = input("Digite a quantidade: ")
                while True:
                    if qtd.isdigit() is False:
                        qtd = input("Digite um valor válido, um número: ")
                    else:
                        qtd = int(qtd)
                        break

                # atualizando dados no dicionário
                self.info_livros[numeracao] = (
                    f"Título: {titulo_livro.capitalize()}, "
                    f"Gênero: {genero.capitalize()}, "
                    f"Autor: {autor.capitalize()}, "
                    f"Editora:  {editora.capitalize()}, Quantidade: {qtd}")
                self.exportacao(INFO_LIVROS, self.info_livros)
                break

    def fazer_emprestimo(self):
        r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
        if r in "nN":
            nome = input("Digite o nome do aluno: ")
            for chave, valor in self.info_alunos.items():
                if nome.lower() in valor \
                    or nome.capitalize() in valor \
                        or nome.title() in valor:
                    print(" ID:", chave, "\n", valor)
        while True:
            _id = input("Digite o ID do aluno: ")

            if _id not in self.info_alunos:
                print("ID não encontrado, digite um ID válido.")
                continue
            else:
                livro = input("Digite o Livro que será emprestado: ")
                devo = input("Digite a data para devolução(DD/MM): ")
                chave = datetime.now().microsecond

            self.emprestimos[chave] = (self.info_alunos[_id],
                                       livro.title(),
                                       devo
                                       )
            print(" Chave da devolução:", chave, "\n", self.emprestimos[chave])
            self.id_emprestimo[chave] = _id
            self.exportacao(EMPRESTIMOS, self.emprestimos)
            self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)
            break

    def fazer_devolucao(self):
        r = input("Tem conhecimento do ID do aluno? [S]im [N]ão: ")
        if r in "nN":
            nome = input("Digite o nome do aluno: ")
            for chave, valor in self.info_alunos.items():
                if nome.lower() in valor \
                    or nome.capitalize() in valor \
                        or nome.title() in valor:
                    print(" ID:", chave, "\n", valor)

        while True:
            _id = input("Digite o ID do aluno: ")
            if _id not in self.id_emprestimo.values():
                print("O aluno não tem nada para devolver.")
                return False
            else:
                for chave, valor in self.id_emprestimo.items():
                    print("Chave:", chave) if _id \
                        in self.id_emprestimo.values() else print()
                    print("Informações:", self.emprestimos[chave], "\n")

            c = input("Digite a chave para realizar a devolução: ")
            self.emprestimos.pop(c)
            self.id_emprestimo.pop(c)
            print("Devolução realizada.")
            self.exportacao(EMPRESTIMOS, self.emprestimos)
            self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)
            break


if __name__ == "__main__":
    b1 = Biblioteca()
    # b1.cadastra_aluno()
    # b1.cadastra_livro()
    # b1.altera_aluno()
    # b1.altera_livro()
    # b1.fazer_emprestimo()
    # b1.fazer_devolucao()
