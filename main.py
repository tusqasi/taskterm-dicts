import json
import defs.TaskFuncs
#Reads from file
sort_index = []


try:

	with open('data_file-1.json', 'r+') as read_file:
		str_file = read_file.read()
		if len(str_file) != 0:
			tasks = json.loads(str_file)
			tasks = tasks['tasks']
			for t in tasks:
				sort_index.append(t['index'])
		else:
			tasks = []

except FileNotFoundError:
	tasks = [] 

c = max(sort_index, default=0)

while True: #Main loop
	prmt = str(input("'a' for adding new task\
					\n'l' for listing all tasks\
					\n'c' for changing a task\
					\n'q' for exiting program\n"))

	if prmt == "a": 
		"""adding a task"""
		c+=1
		usrn, usrdu ,usrds = str(input("name:duration:description\
							 		  \n(separated by '|')\
							 		  \n(duration:HH-MM)\
							 		  \n")).split("|",  2)

		tasks.append(TaskFuncs.addTask(ind=c, name=usrn, dur=usrdu, desc=usrds))
					  
	elif prmt == 'l':
		""""listing all tasks"""
		if len(tasks) == 0:
			print("No Tasks Now")
		else:
			print(tasks)

	elif prmt == 'c':
		tasks = TaskFuncs.chgTask(Tasks)
	elif prmt == 'q':
		print("Bye User")
		break

	else:
		print("No function of that name")
#Make data writable
tasks = {"tasks":tasks}
#print(tasks)


#To save data, only when something is done. 
if len(tasks) != 0:
	with open('data_file-1.json','w') as f :
		json.dump(tasks,f,indent=4)