from hwltd import reports
from hwltd.organization import HelloWorld

path_struct_json = "data/structure_organization.json"
path_workers_data = "data/prework-task2-data.txt"

hwltd = HelloWorld(path_workers_data, path_struct_json)
print("\n\n")

ans = reports.get_num_employees(hwltd, "Engineering Department", 4)
print(ans)
print("\n\n\n")


print(reports.get_average_salary(hwltd, "App Team"))




