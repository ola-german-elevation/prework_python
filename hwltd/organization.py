from workers.person import Person
from workers import strucrure

import json

INDEX_last_name = 0
INDEX_first_name = 1
INDEX_year_of_birth = 2
INDEX_email = 3
INDEX_phones = 4
INDEX_address = 5
INDEX_team = 6
INDEX_role = 7
INDEX_data = 8


class Employees():
    def __init__(self):
        self.employees = {}

    def add_employee(self, *args):
        self.employees[args[INDEX_email]] = Person(args)


class HelloWorld():
    def __init__(self, path):
        self.employees = Employees()
        self.group = strucrure.Group("hello world")

        with open(path, "r") as workers_file:
            for line in workers_file:
                if line.startswith("#") or line == '\n':
                    continue

                line = line.split(", ")
                # temp_person = Person()

                phones = line[INDEX_phones].split(";")
                address = line[INDEX_address].split(";")

                self.employees.add_employee(line[INDEX_first_name],
                                            line[INDEX_last_name],
                                            line[INDEX_year_of_birth],
                                            line[INDEX_email],
                                            phones,
                                            address)


