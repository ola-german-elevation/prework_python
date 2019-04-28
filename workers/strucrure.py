from . import person


class Group(object):
    def __init__(self, name, subgroups, parent_group=None):
        self.name = name
        # self.description = description
        self.parent_group = parent_group
        self.subgroups = []
        self.workers = []

        if isinstance(subgroups, dict):
            for group_key in subgroups:
                self.subgroups.append(Group(group_key, subgroups[group_key], self))

    def print_teams(self):
        if self.subgroups:
            for group in self.subgroups:
                group.print_teams()
        else:
            print(self)

    def print_all_departments(self):
        print(self.name, len(self.workers))
        for s in self.subgroups:
            s.print_all_departments()


    def print_tree(self, dep=[0]):
        dep[0] += 1
        for s in self.subgroups:
            print("\t" * dep[0], s.name, len(s.workers))
            print(s.workers)
            s.print_tree()
        dep[0] -= 1


    def get_team_by_name(self, name):
        if self.name == name:
            return self

        if self.subgroups:
            for s in self.subgroups:
                ans = s.get_team_by_name(name)
                if ans:
                    return ans



    def get_parent_group_by_worker_id(self, id_of_worker):
        for w in self.workers:
            if w.person.id == id_of_worker:
                return self

        if self.subgroups:
            for s in self.subgroups:
                ans = s.get_parent_group_by_worker_id(id_of_worker)
                if ans:
                    return ans


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    def add_worker(self, person_obj):
        if isinstance(person_obj, Worker):
            self.workers.append(person_obj)
        else:
            raise TypeError("a worker need to be a person obj")

    # needs a list, to append the workers to it.
    def get_workers(self, temp_workers):
        if self.workers:
            temp_workers += self.workers
        else:
            for group in self.subgroups:
                group.get_workers(temp_workers)

    # todo
    def get_parent(self):
        pass


class Worker(object):

    def __init__(self, first_name, last_name, year_of_birth, email, phones, address, salary):
        self.person = person.Person(first_name, last_name, year_of_birth, email, phones,
                                    address)  # todo: add args to here for real
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f'name: {self.person.first_name}, salary: {self.get_salary()}'

    def __repr__(self):
        return f'{self.person.id}:{self.person.first_name} {self.person.last_name}'


class Engineer(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, phones, address, salary, bonus):
        super().__init__(first_name, last_name, year_of_birth, email, phones, address, salary)
        self.bonus = bonus

    def get_salary(self):
        return str(int(super().get_salary()) + int(self.bonus))


class SalesPerson(Worker):
    def __init__(self, first_name, last_name, year_of_birth, email, phones,
                 address, salary, commission, deals):
        super().__init__(first_name, last_name, year_of_birth, email, phones, address, salary)
        self.commission = commission
        self.deals = deals

    def get_salary(self):
        return str(int(super().get_salary()) + float(self.commission) * float(self.commission))
