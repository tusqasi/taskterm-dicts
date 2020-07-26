from tkinter import * 

taskls = []

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
		
		self.addBtn = Button(addFrame, text='Add Task')
		self.addBtn.grid(row=3,columnspan=2)
		self.addBtn.bind('<Button-1>',
						  self.add_btn_func)

		self.chgBtn = Button(self.chgFrame,text='Change Task')
		self.chgBtn.grid(row=5,columnspan=2)
		self.chgBtn.bind('<Button-1>',
						  self.chg_btn_func)
		


	def create_task(self):
		pass
		
	def set_task():
		pass


	def chg_btn_func(self, event):
		pass

	def add_btn_func(self, event):
		pass

	def drop_menu_func(self):
		self.dropMenuCtn = StringVar()
		self.dropMenu = OptionMenu(self.chgFrame,
								   self.dropMenuCtn,
								  *taskls,
								   command=self.update_drop_menu)