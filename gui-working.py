from tkinter import * 





class AppWin(Frame):

	def __init__(self,master=None):

		#frames defined or whatever

		addFrame        = Frame(master)          #packed
		chgFrame        = Frame(master)			 #packed
		lastFrame       = Frame(master)			 #packed
		#frames packed
		
		addFrame.grid(row=0, column=0)           
		chgFrame.grid(row=1,column=0)        
		lastFrame.grid(row=3)                    

		#labels
		addNameLabel    = Label(addFrame,		 #packed
							    text='Task Name',
							    anchor="e",
							    width=14)
		addDurLabel     = Label(addFrame, 		 #packed
							    text='Task duration',
							    anchor="e",
							    width=14)
		addDescLabel    = Label(addFrame,		 #packed
							    text='Task Description',
							    anchor="e",
							    width=14)

		chgNameLabel    = Label(chgFrame,
								text='New Name',
								anchor='e',
								width=16)

		chgDurLabel     = Label(chgFrame,
					 		    text='New Duration',
					 		    anchor='e',
					 		    width=16)

		chgDescLabel    = Label(chgFrame,
								text='New Description',
								anchor='e',
								width=16)
		#labels packed
		addDurLabel.grid(row=1, column=0)
		addNameLabel.grid(row=0, column=0)
		addDescLabel.grid(row=2, column=0)

		chgNameLabel.grid(row=0, column=0)
		chgDurLabel.grid(row=1, column=0)
		chgDescLabel.grid(row=2, column=0)



		

		#entry boxes 

		self.addNameEntry    = Entry(addFrame)        
		self.addDurEntry     = Entry(addFrame)
		self.addDescEntry    = Entry(addFrame)

		self.addNameEntry.grid(row=0,column=1)
		self.addDurEntry.grid(row=1,column=1) 
		self.addDescEntry.grid(row=2,column=1)
		# contents StrVar

		self.addNameContent  = StringVar()  
		self.addDurContent   = StringVar()
		self.addDescContent  = StringVar() 
		
		self.chgNameContent  = StringVar()  
		self.chgDurContent   = StringVar() 
		self.chgDescContent  = StringVar()  

		self.addNameContent.set("Task Name")
		self.addDurContent.set("Task Duration")
		self.addDescContent.set("Task Description")

		self.chgNameContent.set("New Task Name")
		self.chgDurContent.set("New Task Duration")
		self.chgDescContent.set("New Task Description")	

		self.addNameEntry["textvariable"] = self.addNameContent
		self.addDurEntry["textvariable"] = self.addDurContent
		self.addDescEntry["textvariable"] = self.addDescContent
		
		self.addNameEntry.bind('<Key-Return>',
								self.) 		 



root = Tk()
root.geometry("280x140")

app = AppWin(root)

root.mainloop()