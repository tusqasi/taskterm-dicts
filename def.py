
class TaskFuncs:
	"""doc string for TaskFuncs"""
			
	def addTask(id, name , dur, desc):
		return {'index':id,
				'name':name,
				'duration':dur,
				'description':desc }
	
	def chgTask(taskl):
		""""changing tasks"""
		while True: #task change loop
			n, s =str(input("Which task(No.)\
						\nand what((n)ame, (d)uration or d(e)scription)\
						\n(separated by |)\
						\n")).split("|",1)
			n = int(n)
			n -= 1		# 'coz computers count from 0 not 1

			if 'n' in s:
				newn = str(input("New name\n"))
				(taskl[int(n)])['name'] = newn
				break
			elif 'd' in s:
				newd = str(input("New duration\n"))
				(taskl[int(n)])['duration'] = newd
				break
			elif 'e' in s:
				newe = str(input("New description\n"))
				(taskl[int(n)])['description'] = newe
				break
			else:
				print("Give a input in a valid format")
				continue
		return taskl
