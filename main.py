tasks = []
c = 0
while True:
	prmt = str(input("'a' for adding new task \a \
					\n'l' for listing all tasks\
					\n'c' for changing a task\
					\n'q' for exiting program\n"))

	if prmt == "a": 
		c+=1
		usrn, usrdu ,usrds = str(input("name:duration:description\
							 		  \n(separated by '|')\
							 		  \n(duration:HH-MM)\
							 		  \n")).split("|",  2)

		tasks.append({'index':c, 'name':usrn, 'duration':usrdu, 'description':usrds})
					  
	elif prmt == 'l':
		print(tasks)
	elif prmt == 'c':
		while True:
			n, s =str(input("Which task(No.)\
						\nand what((n)ame, (d)uration or d(e)scription)\
						\n(separated by |)\
						\n")).split("|",1)
			n -= 1 
			if 'n' in s:
				newn = str(input("New name\n"))
				(tasks[int(n)])['name'] = newn
				break
			elif 'd' in s:
				newd = str(input("New duration\n"))
				(tasks[int(n)])['duration'] = newd
				break
			elif 'e' in s:
				newd = str(input("New description\n"))
				(tasks[int(n)])['description'] = newe
				break
			else:
				print("Give a input in a valid format")
				continue