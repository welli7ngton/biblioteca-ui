# class Biblioteca:

#     def __init__(self) -> None:

#         # Importando dados
#         self.id_alunos = self.importacao(IDS_ALUNOS)
#         self.info_alunos = self.importacao(INFO_ALUNOS)
#         self.id_livros = self.importacao(IDS_LIVROS)
#         self.info_livros = self.importacao(INFO_LIVROS)
#         self.emprestimos = self.importacao(EMPRESTIMOS)
#         self.id_emprestimo = self.importacao(ID_EMPRESTIMO)

#     def importacao(self, caminho: str):
#         with open(caminho, "r", encoding="utf-8") as arq:
#             dados = json.load(arq)
#         return dados

#     def exportacao(self, caminho: str, dados: dict):
#         with open(caminho, "w", encoding="utf-8") as arq:
#             json.dump(dados, arq, ensure_ascii=False, indent=2)

#     def cadastra_aluno(
#             self, nome: str, idade: str, serie: str,
#             turno: str, contato: str, endereco: str):

#         _id = str(len(self.id_alunos))
#         if _id in self.id_alunos:
#             return False
#         self.id_alunos.append(_id)

#         self.info_alunos[_id] = {
#             "ID": _id,
#             "Nome": nome.title(),
#             "Série": serie,
#             "Turno": turno.title(),
#             "Idade": idade,
#             "Contato": contato,
#             "Endereço": endereco.title()
#             }
#         self.exportacao(IDS_ALUNOS, self.id_alunos)
#         self.exportacao(INFO_ALUNOS, self.info_alunos)
#         return self.info_alunos[_id]

#     def cadastra_livro(
#             self, numeracao: str, titulo: str, genero: str,
#             autor: str, editora: str, qtd: str
#             ):

#         self.info_livros[numeracao] = {
#             "Título": titulo.capitalize(),
#             "Gênero": genero.capitalize(),
#             "Autor": autor.capitalize(),
#             "Editora": editora.capitalize(),
#             "Quantidade": qtd,
#             "Numeração": numeracao
#             }
#         self.id_livros.append(numeracao)

#         self.exportacao(IDS_LIVROS, self.id_livros)
#         self.exportacao(INFO_LIVROS, self.info_livros)
#         return self.info_livros[numeracao]

#     def altera_aluno(
#             self, _id: str, nome: str, idade: str, serie: str,
#             turno: str, contato: str, endereco: str
#             ):

#         if _id not in self.id_alunos:
#             return None

#         self.info_alunos[_id] = {
#             "ID": _id,
#             "Nome": nome.title(),
#             "Série": serie,
#             "Turno": turno.title(),
#             "Idade": idade,
#             "Contato": contato,
#             "Endereço": endereco.title()
#             }
#         self.exportacao(INFO_ALUNOS, self.info_alunos)
#         return self.info_alunos[_id]

#     def altera_livro(self, numeracao: str, titulo: str, genero: str,
#                      autor: str, editora: str, qtd: str
#                      ):
#         if numeracao not in self.id_livros:
#             return None
#         self.info_livros[numeracao] = (
#             f"Título: {titulo.capitalize()}, "
#             f"Gênero: {genero.capitalize()}, "
#             f"Autor: {autor.capitalize()}, "
#             f"Editora:  {editora.capitalize()}, Quantidade: {qtd}")
#         self.exportacao(INFO_LIVROS, self.info_livros)
#         return self.info_livros[numeracao]

#     def fazer_emprestimo(self, _id: str, livro: str, devo: str):

#         chave = str(datetime.now().microsecond)

#         self.emprestimos[chave] = {
#             "aluno": self.info_alunos[_id],
#             "livro": livro.title(),
#             "devolucao": devo
#         }
#         self.id_emprestimo[chave] = _id
#         self.exportacao(EMPRESTIMOS, self.emprestimos)
#         self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)

#         return chave, self.emprestimos[chave]

#     def fazer_devolucao(self, chave: str):

#         self.emprestimos.pop(chave)
#         self.id_emprestimo.pop(chave)
#         self.exportacao(EMPRESTIMOS, self.emprestimos)
#         self.exportacao(ID_EMPRESTIMO, self.id_emprestimo)
