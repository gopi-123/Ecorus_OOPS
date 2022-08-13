class Person:

    def __init__(self, name: str, age: int = 0) -> None:
        self.name = name
        self.age = age

    def happy_birthday(self) -> None:
        # adds 1 year to the age
        self.age += 1

    def change_name(self, new_name: str) -> None:
        # changes name with new name provided
        self.name = new_name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person):
            return (other.name == self.name and other.age == self.age)
        return False

    def __str__(self) -> str:
        return f'Person(name:{self.name}, age:{self.age})'


class Office:

    def __init__(self, name: str, people_working: list = []) -> None:
        self.name = name
        self.people_working = people_working

    def start_working_for(self, person_object: Person) -> None:
        self.people_working.append(person_object)

    def finished_working_for(self, person_object: Person) -> None:
        if self.people_working and person_object in self.people_working:
            del self.people_working[self.people_working.index(person_object)]

    def __str__(self) -> str:
        return (
            f'Office(name:{self.name}, '
            f'people_working:{[str(person) for person in self.people_working]})'
        )


# 4: Create 2 objects of that class (Eduardo and <dev_name>)
eduardo = Person("eduardo")
ganga = Person("ganga", 15)

# 3: Create an object of the class "Office", named Ecorus
ecorus = Office("ecorus")

# 5: Make Eduardo and <dev_name> start working for Ecorus
ecorus.start_working_for(eduardo)
ecorus.start_working_for(ganga)

# 6: Make Eduardo finish working from Ecorus
ecorus.finished_working_for(eduardo)

# console screenshot showing the result (printing the objects)
print("Person Object-->", eduardo)
print("Person Object-->", ganga)
print("Office Object-->", ecorus)
