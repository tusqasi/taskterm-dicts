from tkinter import * 

taskls = [{'index':"d",'name':'None','dur':'None','decs':'None'}]

class AppWin(Frame):

	def __init__(self, master):

		##  frames defined or whatever  ##

		addFrame  = Frame(master)         
		self.chgFrame  = Frame(master)			
		lastFrame = Frame(master)			
		##  frames packed  ##
		
		addFrame.grid(row=0, column=0)           
		self.chgFrame.grid(row=1,column=0)        
		lastFrame.grid(row=3)                    

		##  labels  ##
		
		Label(addFrame,
			  text="Task Name",
			  anchor="e",
			  width=17
			  ).grid(row=1, column=0)

		Label(addFrame,
			  text="Task Duration",
			  anchor="e",
			  width=17
			  ).grid(row=0, column=0)

		Label(addFrame,
			  text="Task Description",
			  anchor="e",
			  width=17
			  ).grid(row=2, column=0)


		Label(self.chgFrame,
			  text="New Task Name",
			  anchor="e",
			  width=17
			  ).grid(row=2, column=0)

		Label(self.chgFrame,
			  text="New Task Duration",
			  anchor="e",
			  width=17
			  ).grid(row=3, column=0)

		Label(self.chgFrame,
			  text="New Task Description ",
			  anchor="e",
			  width=17
			  ).grid(row=4, column=0)
		Label(self.chgFrame,
			  text="Select Task to Change"
			  ).grid(row=0,columnspan=2	)


		##  entry boxes  ##

		self.addNameEntry = Entry(addFrame)        
		self.addDurEntry  = Entry(addFrame)
		self.addDescEntry = Entry(addFrame)

		self.chgNameEntry = Entry(self.chgFrame)
		self.chgDurEntry  = Entry(self.chgFrame)
		self.chgDescEntry = Entry(self.chgFrame)

		self.addNameEntry.grid(row=0,column=1)
		self.addDurEntry.grid(row=1,column=1) 
		self.addDescEntry.grid(row=2,column=1)

		self.chgNameEntry.grid(row=2,column=1)
		self.chgDurEntry.grid(row=3,column=1) 
		self.chgDescEntry.grid(row=4,column=1)

		##  contents StrVar  ##
		# add
		self.addNameContent  = StringVar()  
		self.addDurContent   = StringVar()
		self.addDescContent  = StringVar() 
		# chg
		self.chgNameContent  = StringVar()  
		self.chgDurContent   = StringVar() 
		self.chgDescContent  = StringVar()  


		self.addNameEntry["textvariable"] = self.addNameContent
		self.addDurEntry["textvariable"] = self.addDurContent
		self.addDescEntry["textvariable"] = self.addDescContent
		
		self.chgNameEntry["textvariable"] = self.chgNameContent
		self.chgDurEntry["textvariable"] = self.chgDurContent
		self.chgDescEntry["textvariable"] = self.chgDescContent
		
		self.addButton = Button(addFrame,text='Add Task')
		self.addButton.grid(row=3,columnspan=2)
		self.addButton.bind('<Button-1>',
							self.createTask)

		self.chgButton = Button(self.chgFrame,text='Change Task')
		self.chgButton.grid(row=5,columnspan=2)
		self.chgButton.bind('<Button-1>',
							self.setTask)
		
		# Drop Down menu
		self.chgDropContent = StringVar(self.chgFrame)
		self.chgDropContent.set(taskls[0])

		self.chgDrop = OptionMenu(self.chgFrame,
								  self.chgDropContent,
								  *taskls)

		self.chgDrop.grid(row=1, columnspan=2)


		# self.addButton.bind('<Button-1>', self.dropMenu, add=False)
		# self.addNameEntry.bind('<Key-Return>',
		# 						self.setName) 		 
		# self.addDurEntry.bind('<Key-Return>',
		# 						self.setDur)
		# self.addDescEntry.bind('<Key-Return>',
		# 						self.setDesc)

		# self.chgNameEntry.bind('<Key-Return>',
		# 						self.setName)
		# self.addDurEntry.bind('<Key-Return>',
		# 						self.setDur)
		# self.addDescEntry.bind('<Key-Return>',
		# 						self.setDesc)

	def createTask(self, event):
		if self.addDurEntry.get() == "":
			self.addDurContent.set("Empty Duration not allowed")

		if taskls[0]['index'] == "d":
			taskls.pop()

		if len(taskls) == 1:
			
			taskls.append({'index':len(taskls),
						   'name' :self.addNameEntry.get(),
						   'dur'  :self.addDurEntry.get(),
						   'decs' :self.addDescEntry.get()})
		else:
			taskls.append({'index':len(taskls),
						   'name' :self.addNameEntry.get(),
						   'dur'  :self.addDurEntry.get(),
						   'decs' :self.addDescEntry.get()})
		print(taskls)
		# self.chgDropContent = StringVar(self.chgFrame)
		# self.chgDropContent.set(taskls[0])

		self.chgDrop = OptionMenu(self.chgFrame,
								  self.chgDropContent,
								  *taskls)

		self.chgDrop.grid(row=1, columnspan=2)

	def setTask(self, event):
		pass

	def dropMenu(self, event):
		pass

