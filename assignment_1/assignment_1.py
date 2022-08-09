
class Person:
    name = ""
    age = " "

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        pass

    def happy_birthday(self):
        # adds 1 year to the age
        self.age += 1
        pass

    def change_name(self, new_name: str):
        # changes name with new name
        self.name = new_name


class Office():
    __name: str
    __people_Working: str

    def __init__(self, name, people_working=""):
        self.people_working = ""
        pass

    def start_working_for(self, Person_object):
        pass

    def finished_working_for(self, Person):
        self.__people_Working = "remove Person from peopleworking"
        pass


obj_person = Person
ecorus = Office("ecorus")

eduardo = Office("ecorus")
ganga = Office("ecorus")

eduardo.start_working_for(obj_person)
eduardo.finished_working_for(obj_person)

print("obj_person:",obj_person)
print("eduardo:", eduardo)
print("ganga:", ganga)



