from student_and_book import Student
from student_and_book import Book
import json

FILE_PATH_STUDENTS = "att/jsonfiles/students.json"
FILE_PATH_BOOKS = "att/jsonfiles/books.json"


class Library:

    def __init__(self) -> None:
        self.studentsDatas = self.__dataImport(FILE_PATH_STUDENTS)
        self.booksDatas = self.__dataImport(FILE_PATH_BOOKS)

    def __dataImport(self, filePath: str):
        with open(filePath, "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas

    def __dataExport(self, studentOrBook: Student | Book):
        __filePath, __dict = (FILE_PATH_STUDENTS, self.studentsDatas)\
              if isinstance(studentOrBook, Student)\
              else (FILE_PATH_BOOKS, self.booksDatas)

        attributes = [
            attr for attr in dir(studentOrBook)
            if not attr.startswith("__")
            and not attr.startswith("set")
        ]

        dictionaryKeyAttributes = [
            attr.replace("set", "") for attr in dir(studentOrBook)
            if attr.startswith("set")
        ]

        objectData = dict()
        for i in range(len(attributes)):
            objectData[dictionaryKeyAttributes[i]] = getattr(
                studentOrBook,
                attributes[i]
            )

        __dict[len(__dict)] = objectData
        with open(__filePath, "w", encoding="utf-8") as file:
            json.dump(
                __dict,
                file,
                ensure_ascii=False,
                indent=2
            )
