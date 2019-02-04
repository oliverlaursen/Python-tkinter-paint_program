#fileencoding=UTF-8
"""
	paint.py


	A simple drawing program that works like a simplified MSPaint

"""

import tkinter as tk
from tkinter.colorchooser import *

class Paint:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Paint')

		self.toolbar=tk.Frame(bg='black')
		self.v = tk.IntVar()
		self.colour=tk.StringVar(self.root)
		self.colour.set("black")

		self.img1=tk.PhotoImage(file='images/line_tool.gif')
		self.img2=tk.PhotoImage(file='images/pencil_tool.gif')
		self.img3=tk.PhotoImage(file='images/oval_tool.gif')
		self.img4=tk.PhotoImage(file='images/rectangle_tool.gif')

		self.r1=tk.Radiobutton(self.toolbar, text="line",variable=self.v,value=1,indicatoron=0,padx=20,image=self.img1)
		self.r1.pack(side=tk.LEFT)

		self.r2=tk.Radiobutton(self.toolbar,text="freehand", variable=self.v,value=2,indicatoron=0,padx=20,image=self.img2)
		self.r2.pack(side=tk.LEFT)

		self.r3=tk.Radiobutton(self.toolbar,text="circle",variable=self.v,value=3,indicatoron=0,padx=20,image=self.img3)
		self.r3.pack(side=tk.LEFT)

		self.r4=tk.Radiobutton(self.toolbar,text="square",variable=self.v,value=4,indicatoron=0,padx=20,image=self.img4)
		self.r4.pack(side=tk.LEFT)

		self.optm=tk.OptionMenu(self.toolbar,self.colour,"black","blue","red","orange","green")
		self.optm.pack(side=tk.LEFT)

		self.colour_wheel=tk.Button(self.toolbar,text="Colour Wheel",command=self.get_color)
		self.colour_wheel.pack(side=tk.LEFT)

		self.toolbar.pack()


		self.canvas = tk.Canvas(width=600, height=400)
		self.canvas.pack(fill='both', expand=tk.YES)
		self.canvas.bind('<ButtonPress-1>', lambda event: self.click(event)) # Kaldes ved et museklik på canvas
		self.canvas.bind('<ButtonRelease-1>', lambda event: self.release(event))
		self.canvas.bind('<B1-Motion>', lambda event: self.motion(event))
		self.colour.trace('w', self.callback)
		self.root.bind("<Configure>", self.on_resize) #Resize

		self.x=0
		self.y=0

		self.height=self.root.winfo_reqheight()
		self.width=self.root.winfo_reqwidth()

		self.oval=self.canvas.create_oval(0,0,0,0, fill=self.colour.get())
		self.rect=self.canvas.create_rectangle(0,0,0,0,fill=self.colour.get())
		self.line=self.canvas.create_line(0,0,0,0,fill=self.colour.get())

	def get_color(self):
		self.colour.set(askcolor()[1])

	def on_resize(self,event): 
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height

	def callback(self,*args):
		self.toolbar.config(bg=self.colour.get())

	def click(self, event):
		self.startx=event.x
		self.starty=event.y

		self.x=event.x
		self.y=event.y

		if(self.v.get()==1):
			self.line=self.canvas.create_line(self.startx,self.starty,self.startx,self.starty,fill=self.colour.get())

		elif(self.v.get()==3):
			self.oval=self.canvas.create_oval(self.startx,self.starty,self.startx,self.starty,fill=self.colour.get())

		elif(self.v.get()==4):
			self.rect=self.canvas.create_rectangle(self.startx,self.starty,self.startx,self.starty,fill=self.colour.get())


	def release(self,event):
		self.endx=event.x
		self.endy=event.y


	def motion(self, event):
		if(self.v.get()==2): #freehand
			self.canvas.create_line(self.x,self.y,event.x,event.y, fill=self.colour.get())

		elif(self.v.get()==3): #oval animation
			self.canvas.coords(self.oval,self.startx,self.starty, self.x,self.y)
		elif(self.v.get()==4): #rektangel animation
			self.canvas.coords(self.rect,self.startx,self.starty,self.x,self.y)
		elif(self.v.get()==1): #line animation
			self.canvas.coords(self.line,self.startx,self.starty,self.x,self.y)


		self.x=event.x
		self.y=event.y



if __name__ == '__main__':
	p1=Paint()
	p1.root.mainloop()

