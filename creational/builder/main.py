class Person:
    def __init__(self):
        # Personal details
        self.name = None
        self.address = None
        self.age = None

        # work details
        self.company = None
        self.earnings = None

    def __str__(self):
        return f'{self.name} {self.address} {self.age} {self.company} {self.earnings}'

    # The client doesn't need to know about the builder class
    @staticmethod
    def create():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def name(self, name):
        self.person.name = name
        return self

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super(PersonJobBuilder, self).__init__(person)

    def at(self, company_name):
        self.person.company = company_name
        # Since we want to chain function calls
        return self

    def earning(self, earnings):
        self.person.earnings = earnings
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super(PersonAddressBuilder, self).__init__(person)

    def at(self, address):
        self.person.address = address
        return self

    def is_of_age(self, age):
        self.person.age = age
        return self


if __name__ == '__main__':
    person = Person.create().name('Aditya').lives.at('Janhavi Enclave').is_of_age(27).works.at('Smartlinks').earning(10).build()
    print(person)
