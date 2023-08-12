from book import Book
from student import Student
from library import Library

if __name__ == "__main__":
    l1 = Library()
    s1 = Student()
    b1 = Book()

    for item, value in l1.booksDatas.items():
        print(item, value)

    for item, value in l1.studentsDatas.items():
        print(item, value)
