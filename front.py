import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import adjust as adj

class Main:
	def __init__(self):
		self.ont = ''
		self.update = ''
		self.dic = []
		self.app = tk.Tk()
		self.app.title("Update Company Names")
		self.app.geometry("700x280")
		self.v1 = tk.StringVar()
		self.v2 = tk.StringVar()
		self.v3 = tk.StringVar()
	def selectOntFile(self):
		self.ont = askopenfilename()
		self.dic = adj.buildOnt(self.ont)
		self.v1.set(self.ont)
	def selectUpdateFile(self):
		self.update = askopenfilename()
		self.v2.set(self.update)
	def updateFile(self):
		if self.dic and self.update:
			try:
				adj.updateFile(self.update, self.dic)
				self.v3.set("Success")
			except(ValueError):
				messagebox.showinfo("Error","Could not find Organization column in the file to be updated. Check that the file \
					to be updated has a header row with 'Organization' in it, and that no typos are present in the header row.")
		else:
			messagebox.showinfo("Error","Import the ontology file first.")

	def goodbye(self):
		self.app.destroy()

	def main(self):
		app = self.app
		instructionContainer = tk.Frame(app, bd=5)
		instructionContainer.pack(fill='x')
		instructions = tk.Label(instructionContainer,bg='#e9e9e9',justify='left',wraplength=690,text="This program helps deal with OSCARplus by updating the organization names that are misspelled by students.\n\n\
Convert all excel files to .csv files before running (can be done through 'save as' in excel), and ensure that the file to be updated has a header row with 'Organization' included in it.\n\nA cleaned file will be added in the same folder as the file to be updated upon completion of this program.")
		instructions.pack()
		panes = tk.PanedWindow(app)
		panes.pack()
		containerA = tk.Frame(panes, bd=5)
		containerB = tk.Frame(panes, bd=5)
		panes.add(containerA)
		panes.add(containerB)
		container1 = tk.Frame(containerA,height=10)
		container2 = tk.Frame(containerA,height=10)
		container3 = tk.Frame(containerA,height=10)
		container1.pack(fill='x')
		container2.pack(fill='x')
		container3.pack(fill='x')
		containerB1 = tk.Frame(containerB,height=10)
		containerB2 = tk.Frame(containerB,height=10)
		containerB3 = tk.Frame(containerB,height=10)
		containerB1.pack(fill='x')
		containerB2.pack(fill='x')
		containerB3.pack(fill='x')
		button1 = tk.Button(container1, command=self.selectOntFile, text="Select File",width=10)
		label1 = tk.Label(container1, text="1. Select file containing ontology ")
		ontFileLabel = tk.Label(containerB1, textvariable=self.v1, fg='green',width=100, anchor='e',pady=4)
		button2 = tk.Button(container2, command=self.selectUpdateFile, text="Select File",width=10)
		label2 = tk.Label(container2, text="2. Select file to be updated ")
		updateFileLabel = tk.Label(containerB2, textvariable=self.v2, fg='green', width=100, anchor='e',pady=4)
		button3 = tk.Button(container3, command=self.updateFile, text="Update File",width=10)
		label3 = tk.Label(container3, text="3. Update file")
		successLabel = tk.Label(containerB3, textvariable=self.v3, fg='green', width=100, anchor='e',pady=4)
		label1.pack(side='left')
		label2.pack(side='left')
		label3.pack(side='left')
		ontFileLabel.pack(side='right')
		updateFileLabel.pack(side='right')
		successLabel.pack(side='right')
		button1.pack(side='right')
		button2.pack(side='right')
		button3.pack(side='right')
		button4 = tk.Button(app,text="Close Window",command=self.goodbye)
		button4.pack()
		app.mainloop()


main = Main()
main.main()