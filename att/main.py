import json


FILE_PATH_STUDENTS = "att/jsonfiles/students.json"
FILE_PATH_BOOKS = "att/jsonfiles/books.json"


class Student:
    def __init__(self) -> None:
        pass

    @property
    def setName(self):
        return self._name

    @setName.setter
    def setName(self, value: str):
        self._name = value.title()

    @property
    def setAge(self):
        return self._age

    @setAge.setter
    def setAge(self, value: int):
        self._age = value

    @property
    def setAdress(self):
        return self._adress

    @setAdress.setter
    def setAdress(self, value: str):
        self._adress = value.title()

    @property
    def setContactNumber(self):
        return self._contactNumber

    @setContactNumber.setter
    def setContactNumber(self, value: str):
        self._contactNumber = value

    @property
    def setShift(self):
        return self._shift

    @setShift.setter
    def setShift(self, value: str):
        self._shift = value.capitalize()

    @property
    def setGradeYear(self):
        return self._gradeYear

    @setGradeYear.setter
    def setGradeYear(self, value: str):
        self._gradeYear = value


class Book:
    def __init__(self) -> None:
        pass

    @property
    def setTitle(self):
        return self._title

    @setTitle.setter
    def setTitle(self, value: str):
        self._title = value.title()

    @property
    def setGender(self):
        return self._gender

    @setGender.setter
    def setGender(self, value: str):
        self._gender = value.title()

    @property
    def setAuthor(self):
        return self._author

    @setAuthor.setter
    def setAuthor(self, value: str):
        self._author = value.capitalize()

    @property
    def setPublishingCompany(self):
        return self._publishingCompany

    @setPublishingCompany.setter
    def setPublishingCompany(self, value: str):
        self._publishingCompany = value.capitalize()

    @property
    def setAmount(self):
        return self._amount

    @setAmount.setter
    def setAmount(self, value: int):
        self._amount = value


class Library:
    def __init__(self) -> None:
        self.studentsDatas = self.dataImport(FILE_PATH_STUDENTS)
        self.booksDatas = self.dataImport(FILE_PATH_BOOKS)

    def dataImport(self, filePath: str):
        with open(filePath, "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas

    def dataExport(self, studentOrBook: Student | Book):
        __filePath,__dict = (FILE_PATH_STUDENTS, self.studentsDatas)\
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


if __name__ == "__main__":
    s1 = Student()
    s1.setName = "wellington almeida Silva"
    s1.setAge = 20
    s1.setAdress = "vila andrade, bairro açude velho casa n 1187"
    s1.setContactNumber = "88 9 8176-2299"
    s1.setShift = "matutino"
    s1.setGradeYear = "8"

    b1 = Book()
    b1.setTitle = "inglês intermediário"
    b1.setAuthor = "escola"
    b1.setGender = "educação"
    b1.setPublishingCompany = "estado"
    b1.setAmount = 200
    print(s1._name)
    print(s1._age)
    print(s1._adress)
    print(s1._contactNumber)
    print(s1._shift)
    print()
    print(b1._title)
    print(b1._gender)
    print(b1._author)
    print(b1._publishingCompany)
    print(b1._amount)

    l1 = Library()
    l1.dataExport(b1)
    l1.dataExport(s1)
