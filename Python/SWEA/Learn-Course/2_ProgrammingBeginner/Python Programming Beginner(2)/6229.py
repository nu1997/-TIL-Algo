class Person:
    def __init__(self):
        pass
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

he = Male()
he.getGender()

she = Female()
she.getGender()