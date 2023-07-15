import os
import json
from variaveis import CAMINHO_DB_FILES

IDS_ALUNOS = os.path.join(CAMINHO_DB_FILES, "id_alunos.json")
INFO_ALUNOS = os.path.join(CAMINHO_DB_FILES, "info_alunos.json")
IDS_LIVROS = os.path.join(CAMINHO_DB_FILES, "id_livros.json")
INFO_LIVROS = os.path.join(CAMINHO_DB_FILES, "info_livros.json")


class Biblioteca:

    def __init__(self) -> None:

        # Importando dados
        self.id_alunos = self.importacao(IDS_ALUNOS)
        self.info_alunos = self.importacao(INFO_ALUNOS)
        self.id_livros = self.importacao(IDS_LIVROS)
        self.info_livros = self.importacao(INFO_LIVROS)
        print(self.id_alunos)

    def importacao(self, caminho):
        with open(caminho, "r") as arq:
            dados = json.load(arq)
        return dados

    def exportacao(self, caminho, dados):
        with open(caminho, "w") as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=2)

    def cadastra_aluno(self):
        _id = len(self.id_alunos)
        if _id in self.id_alunos:
            return False
        self.id_alunos.append(_id)
        print("ID =", _id)
        nome = input("Nome do Aluno: ")
        idade = int(input("Idade: "))
        serie = input("Série: ")
        turno = input("Turno: ")
        contato = input("Contato (00 0 0000-0000): ")
        print("Endereço: Rua, Bairro, Número.:")
        endereco = input()

        self.info_alunos[_id] = (
            f"Nome = {nome.capitalize()}, Série = {serie},"
            f"Turno = {turno}, Idade = {idade},Contato = {contato},"
            f"Endereço = {endereco.capitalize()}"
        )

        self.exportacao(IDS_ALUNOS, self.id_alunos)
        self.exportacao(INFO_ALUNOS, self.info_alunos)


if __name__ == "__main__":
    b1 = Biblioteca()
    b1.cadastra_aluno()
