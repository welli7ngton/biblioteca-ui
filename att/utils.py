# from student import Student


def checkSpecialCharacters(strings_list: list[str]) -> bool:
    for i in strings_list:
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
