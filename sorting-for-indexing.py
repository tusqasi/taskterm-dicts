import json

with open('data_file-1.json','r') as read_file:
	s = read_file.read()
	tasks = json.loads(s)
	tasks = tasks['tasks']
sort_index = []

for task in tasks:
	sort_index.append(task['index'])



