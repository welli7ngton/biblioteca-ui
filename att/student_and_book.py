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
