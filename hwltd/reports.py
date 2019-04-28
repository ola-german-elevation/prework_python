from workers import strucrure
from . import organization




def get_relational_salary(hwltd, worker_id):
    group = get_parent_group_by_worker_id(hwltd, worker_id)
    for w in group.workers:
        pass

def get_parent_group_by_worker_id(hwltd, worker):
    pass


def get_average_salary(hwltd, department_str):
    group = hwltd.group_hwltd.get_team_by_name(department_str)
    if group:
        if group.workers:
            print(group.workers)
            print(type(group.workers[0]))
            sum = 0
            for w in group.workers:

                salary = w.get_salary()
                sum += float(salary)
            return sum / len(group.workers)
    else:
        print("department was not found")


def get_num_employees(hwltd, department, depth):
    group = hwltd.group_hwltd.get_team_by_name(department)
    if group:
        return __get_num_of_employees(group, depth)
    else:
        print("department was not found")


def __get_num_of_employees(group, depth):
    ans = {}
    __sum_workeres_subgroups(group, ans, depth)
    return ans


def __sum_workeres_subgroups(group, ans, depth):
    if depth == 0:
        return 0
    sum_of_workers = len(group.workers)

    if depth == 1:
        return sum_of_workers

    depth -= 1
    for s in group.subgroups:
        sum_of_workers += __sum_workeres_subgroups(s, ans, depth)
    ans[group.name] = sum_of_workers
    return sum_of_workers


