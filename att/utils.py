# from student import Student


def checkSpecialCharacters(strings_list: list[str]) -> bool:
    for i in strings_list:
        print(i)
        for j in i:
            if j in ["'", ";", '"', "-"]:
                raise Exception("Caracteres inválidos, possível SQL injection")
    return True


def getAttributesValues(the_object: object) -> list[str]:
    attributes = [
            attr for attr in dir(the_object)
            if not attr.startswith("__")
            and not attr.startswith("set")
            and not attr == "_age"
            and not attr == "_amount"
            ]
    values = [
        getattr(the_object, attributes[i])
        for i in range(len(attributes))
        ]
    return values


# primeiros testes
# if __name__ == "__main__":
#     s1 = Student()
#     s1.setName = "wellin;gton"
#     s1.setAdress = "endereco"
#     s1.setAge = 12
#     s1.setContactNumber = "88 8888-8888"
#     s1.setGradeYear = "9"
#     s1.setShift = "noturno"

#     atributes_values = getAttributesAndValues(s1)

#     print(checkSpecialCharacters(atributes_values))
