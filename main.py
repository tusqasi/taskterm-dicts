import json 
c = 0      

#Reads from file

with open('data_file-1.json','r') as read_file:
	str_file = read_file.read()
	if len(str_file) != 0:
		tasks = json.loads(str_file)
		tasks = tasks['tasks']
	else:
		tasks = []

while True: #Main loop
	prmt = str(input("'a' for adding new task \a \
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

		tasks.append({'index':c, 'name':usrn, 'duration':usrdu, 'description':usrds})
					  
	elif prmt == 'l':
		""""listing all tasks"""
		if len(tasks) == 0:
			print("No Tasks Now")
		else:
			print(tasks)

	elif prmt == 'c':
		""""chaning tasks"""
		while True: #task change loop
			n, s =str(input("Which task(No.)\
						\nand what((n)ame, (d)uration or d(e)scription)\
						\n(separated by |)\
						\n")).split("|",1)
			n -= 1		# 'coz computers count from 0 not 1
			if 'n' in s:
				newn = str(input("New name\n"))
				(tasks[int(n)])['name'] = newn
				break
			elif 'd' in s:
				newd = str(input("New duration\n"))
				(tasks[int(n)])['duration'] = newd
				break
			elif 'e' in s:
				newe = str(input("New description\n"))
				(tasks[int(n)])['description'] = newe
				break
			else:
				print("Give a input in a valid format")
				continue
	elif prmt == 'q':
		print("Bye User")
		break
#Make data writable
tasks = {"tasks":tasks}
#print(tasks)

#To save data, only when something is done. 
if len(tasks) != 0:
	with open('data_file-{x}.json'.format(x=c),'w') as f :
		json.dump(tasks,f,indent=4)


