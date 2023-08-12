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
