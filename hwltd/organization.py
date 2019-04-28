import json
from uu import Error

from workers.person import Person
from workers.strucrure import Group, Worker, Engineer, SalesPerson

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


class Employees:
    def __init__(self):
        self.employees = {}

    def add_employee(self, email, name):
        self.employees[email] = name


# first_name, last_name, year_of_birth, email, phones, address

def init_worker(role, data, first_name, last_name, year_of_birth, email, phones, address):
    if role == "engineer":
        if ";" in data:
            salary, bonus = data.split(';')
        else:
            salary = data
            bonus = "0"
        return Engineer(first_name, last_name, year_of_birth, email, phones, address, salary, bonus)

    elif role == "sales":
        sales_data = data.split(';')

        if len(sales_data) >= 3:
            salary, comission, *deals = sales_data
        else:
            deals = []
            RuntimeWarning("there is no deals")

        if len(sales_data) == 2:
            comission = sales_data[1]
            salary = sales_data[0]
        elif len(sales_data) == 1:
            salary = sales_data[0]
            comission = 0
            RuntimeWarning("There is no commision")
        else:
            ValueError("No salary")



        return SalesPerson(first_name, last_name, year_of_birth, email, phones,
                           address, salary, comission, deals)
    else:
        return Worker(first_name, last_name, year_of_birth, email, phones, address, data)


class HelloWorld():
    def __init__(self, path_workers, path_json):
        self.employees = Employees()

        with open(path_json, 'r') as f:
            j_obj = json.load(f)
        hello_world_dict = j_obj['Hello World']

        self.group_hwltd = Group(name="Hello World", subgroups=hello_world_dict)


        with open(path_workers, "r") as workers_file:
            for line in workers_file:

                if line.startswith("#") or line == '\n':
                    continue
                if line.endswith("\n"):
                    line = line[:-1]
                # print(line)

                line = line.split(", ")
                # temp_person = Person()

                phones = line[INDEX_phones].split(";")
                address = line[INDEX_address].split(";")
                role = line[INDEX_role]
                team_name = line[INDEX_team]
                self.employees.add_employee(line[INDEX_email],
                                            line[INDEX_first_name])
                try:
                    worker = init_worker(role,
                                         line[INDEX_data],
                                         line[INDEX_first_name],
                                         line[INDEX_last_name],
                                         line[INDEX_year_of_birth],
                                         line[INDEX_email],
                                         phones,
                                         address)
                except ValueError as e:
                    print("An Error has accoure in line:")
                    print(line)
                    print(e)


                try:
                    if team_name in ["qa", "cto"]:
                        team_name = team_name.upper()
                        if team_name in ["CTO"]:
                            team_name += " Group"
                        else:
                            team_name += " Team"
                    else:
                        team_name = team_name.capitalize() + " Team"

                    group = self.group_hwltd.get_team_by_name(team_name)
                    if group:
                        group.add_worker(worker)
                    else:
                        print(f'TEAM NOT FOUND: {team_name}')
                except Exception as e:
                    print(f"error while searching teams {role},{team_name}\n:ERROR:{e}")

    def print_hwltd(self):
        self.group_hwltd.print_teams()

    def print_tree(self):
        self.group_hwltd.print_tree()

    def print_workers(self):
        workers = []
        self.group_hwltd.get_workers(workers)
        print(workers)

    def print_sum(self):
        self.group_hwltd.sum_workeres_subgroups()


    def print(self):
        self.group_hwltd.print_all_departments()



