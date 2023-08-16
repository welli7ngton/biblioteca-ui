import sqlite3
from student import Student
from book import Book
from datetime import date, timedelta

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
            "VALUES("
            f"'{student._name}', {student._age}, "
            f"'{student._contactNumber}', '{student._adress}', "
            f"'{student._gradeYear}', '{student._shift}'"
            ")"
        )
        self.connection.commit()

    def registerBook(self, book: Book) -> None:

        self.cursor.execute(
            "INSERT INTO books "
            "(title, author, publishing_company, gender, amount) "
            "VALUES("
            f"'{book._title}', '{book._author}', "
            f"'{book._publishingCompany}', '{book._gender}', "
            f"{book._amount}"
            ")"
        )
        self.connection.commit()

    def registerLoan(self, student_id: int,
                     book_id: int, devolution_date=None) -> None:

        if devolution_date:
            self.cursor.execute(
                "INSERT INTO loan "
                "(student_id, book_id, loan_date, devolution_date) "
                "VALUES("
                f"'{student_id}', '{book_id}', "
                f"'{TODAY}', '{TODAY + timedelta(days=devolution_date)}' "
                ")"
            )
            self.connection.commit()
            return

        self.cursor.execute(
            "INSERT INTO loan "
            "(student_id, book_id, loan_date, devolution_date) "
            "VALUES("
            f"'{student_id}', '{book_id}', "
            f"'{TODAY}', '{DEVOLUTION_DATE}' "
            ")"
        )
        self.connection.commit()

    def _closeCon(self) -> None:
        self.cursor.close()
        self.connection.close()

    # TODO: getStudent|BookID


if __name__ == "__main__":
    # s1 = Student()
    # s1.setName = "Qeijo"
    # s1.setAdress = "vila acude distrito federal jaburu 12"
    # s1.setAge = 12
    # s1.setContactNumber = "1232148931238"
    # s1.setGradeYear = "3"
    # s1.setShift = "noturno"

    # b1 = Book()
    # b1.setTitle = "ingles"
    # b1.setAmount = 200
    # b1.setAuthor = "escola"
    # b1.setGender = "educacao"
    # b1.setPublishingCompany = "governo"

    b = DataBase()
    # b.registerStudent(s1)

    b.registerLoan(99, 6, 5)
    b._closeCon()
