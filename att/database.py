import sqlite3
from student import Student
from book import Book
DATABASE_FILE_PATH = 'library.db'


class DataBase():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()

    def registerStudent(self, student: Student):

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

    def registerBook(self, book: Book):

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

    # TODO: registerLoan
    # TODO: getStudent|BookID


if __name__ == "__main__":
    s1 = Student()
    s1.setName = "Qeijo"
    s1.setAdress = "vila acude distrito federal jaburu 12"
    s1.setAge = 12
    s1.setContactNumber = "1232148931238"
    s1.setGradeYear = "3"
    s1.setShift = "noturno"

    b1 = Book()
    b1.setTitle = "Harry Potter"
    b1.setAmount = 100
    b1.setAuthor = "Augusto ferreira"
    b1.setGender = "fantasia"
    b1.setPublishingCompany = "sei la"

    b = DataBase()
    b.registerStudent(s1)
    b.registerBook(b1)
    b.cursor.close()
    b.connection.close()
