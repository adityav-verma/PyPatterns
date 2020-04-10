"""cases where we have a limited set of objects which are going to used and created again and again

It makes sense to move the creation to a factory which uses a Prototype of these objects.
"""

import copy


class Address:
    def __init__(self, office_name, seat_number):
        self.office_name = office_name
        self.seat_number = seat_number

    def __str__(self):
        return f'Office: {self.office_name}, Seat: {self.seat_number}'


class Employee:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Name: {self.name}, {self.address}'


class EmployeeFactory:
    main_office = Address('Main Office', None)
    aux_office = Address('Aux Office', None)

    @classmethod
    def __new_employee(cls, name, seat_number, proto: Address):
        office = copy.deepcopy(proto)
        office.seat_number = seat_number
        return Employee(name, office)

    @classmethod
    def create_main_office_employee(cls, name, seat_number):
        return cls.__new_employee(name, seat_number, cls.main_office)

    @classmethod
    def create_aux_office_employee(cls, name, seat_number):
        return cls.__new_employee(name, seat_number, cls.aux_office)


if __name__ == '__main__':
    main_office_emp = EmployeeFactory.create_main_office_employee('Aditya', 11)
    aux_office_emp = EmployeeFactory.create_aux_office_employee('Verma', 10)

    print(main_office_emp)
    print(aux_office_emp)
