from . import person


class Group(object):
    def __init__(self, name, subgroups, parent_group=None):
        self.name = name
        # self.description = description
        self.parent_group = parent_group
        self.subgroups = []
        self.workers = None

        if isinstance(subgroups, dict):
            for group_key in subgroups:
                self.subgroups.append(Group(group_key, subgroups[group_key], self))

        elif isinstance(subgroups, list):
            self.workers = []

        print(f'G:{self.name}  subgroups: {self.subgroups}')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    # todo
    def get_workers(self):
        pass

    # todo
    def get_parents(self):
        pass


class Worker(object):

    def __init__(self, first_name, last_name, year_of_birth, email, phones, address, salary):
        self.person = person.Person(first_name, last_name, year_of_birth, email, phones,
                                    address)  # todo: add args to here for real
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class Engineer(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, phones, address, salary, bonus):
        super().__init__(first_name, last_name, year_of_birth, email, phones, address, salary)
        self.bonus = bonus

    def get_salary(self):
        return str(int(super().get_salary()) + int(self.bonus))


class SalesPerson(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, phones, address, salary, commission):
        super().__init__(first_name, last_name, year_of_birth, email, phones, address, salary)
        self.commission = commission
        self.deals = []

    def get_salary(self):
        return str(int(super().get_salary()) + int(self.commission) * len(self.commission))
