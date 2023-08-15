import sqlite3
from student import Student
DATABASE_FILE_PATH = './att/database_content/librarytest.sqlite'


class DataBase():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()

    def importData(self):
        result = self.cursor.execute(
            "SELECT * FROM students"
        )

        for data in result.fetchall():
            print(data)

    def registerStudent(self, student: Student):
        data = [
            69,
            student._name,
            student._age,
            student._contactNumber,
            student._adress,
            student._gradeYear,
            student._shift,
            "2023-08-15 14:57:16"
        ]

        self.cursor.executemany("""
            INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        self.connection.commit()
        print("Registro salvo!")


def createDB():
    con = sqlite3.connect(DATABASE_FILE_PATH)
    cur = con.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS tabela_teste'
        '('
        'id_aluno INTEGER PRIMARY KEY AUTOINCREMENT, '
        'nome TEXT, '
        'idade INTEGER, '
        'crated_at DATETIME DEFAULT(DATETIME("NOW"))'
        ');'
    )
    con.commit()
    cur.execute(
        'INSERT INTO tabela_teste'
        '(nome, idade) '
        'VALUES '
        '("JOSE", 20)'
    )
    cur.close()
    con.close()


if __name__ == "__main__":
    s1 = Student()
    s1.setName = "Pedro Henrique"
    s1.setAdress = "Casa 32"
    s1.setAge = "19"
    s1.setContactNumber = "11 1111-1111"
    s1.setGradeYear = "9"
    s1.setShift = "Matutino"

    createDB()
