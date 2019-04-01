import json

from workers.strucrure import Group

f = open("data/structure_organization.json", 'r')
j_obj = json.load(f)
hello_world_dict = j_obj['Hello World']
group_hwltd = Group(name="hello world", subgroups=hello_world_dict)
