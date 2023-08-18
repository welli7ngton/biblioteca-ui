import sqlite3
from student_and_book import Student
from student_and_book import Book
from datetime import date, timedelta
from utils import checkSpecialCharacters
from utils import getAttributesValues


DATABASE_FILE_PATH = './att/library.db'
LOAN_PERIOD = 14
TODAY = date.today()
DEVOLUTION_DATE = TODAY + timedelta(days=LOAN_PERIOD)


class DataBase():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()

    def registerStudent(self, student: Student) -> None:

        self.cursor.execute(
            "INSERT INTO students "
            "(name, age, contact, adress, grade_year, shift) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            [
                student._name, student._age, student._contactNumber,
                student._adress, student._gradeYear, student._shift
            ]
        )
        self.connection.commit()

    def registerBook(self, book: Book) -> None:

        values = getAttributesValues(book)
        if checkSpecialCharacters(values):
            self.cursor.execute(
                "INSERT INTO books "
                "(title, author, publishing_company, gender, amount) "
                "VALUES(?, ?, ?, ?, ?, )",
                [
                    book._title, book._author, book._publishingCompany,
                    book._gender, book._amount
                ]
            )
            self.connection.commit()

    def registerLoan(
        self, student_id: int,
        book_id: int, devolution_date=None
    ) -> None:

        if devolution_date:
            self.cursor.execute(
                "INSERT INTO loan "
                "(student_id, book_id, loan_date, devolution_date) "
                "VALUES(?, ?, ?, ?)",
                [
                    student_id, book_id, TODAY,
                    (TODAY + timedelta(days=devolution_date))
                ]
            )
            self.connection.commit()
            return

        self.cursor.execute(
            "INSERT INTO loan "
            "(student_id, book_id, loan_date, devolution_date) "
            "VALUES(?, ?, ?, ?)",
            [
                student_id, book_id, TODAY, DEVOLUTION_DATE
            ]
        )
        self.connection.commit()

    def deleteRegister(self, _id: int, table: str, column: str) -> None:
        if checkSpecialCharacters(table) and\
                checkSpecialCharacters(column) and\
                self._checkIdexistence(_id, table, column):

            self.cursor.execute(
                f"DELETE FROM {table} WHERE {column}={_id}"
            )
            self.connection.commit()

    def _checkIdexistence(self, _id: int, table: str, column) -> bool:

        rows = self.cursor.execute(
            f"SELECT * FROM {table} WHERE {column}"
        )

        for row in rows.fetchall():
            if _id in row:
                return True
        raise Exception("ID NÃO EXISTE")

    def getTableInfo(self, table_name: str) -> None:
        tableRows = self.cursor.execute(
            f"SELECT * FROM {table_name}"
        )

        for row in tableRows.fetchall():
            print(row)

    def _closeConnectionAndCursor(self) -> None:
        self.cursor.close()
        self.connection.close()
