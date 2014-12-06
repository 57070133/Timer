from Tkinter import *
import time
import math

secs = 0
deg = 0
x = 0
y = 0

class Analog():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x300")
        self.aaa = StringVar()
        self.bbb = StringVar()
        self.tick()
        self.draw()

        lab= Label(self.root, textvariable=self.aaa)
        lab.pack()

        lab= Label(self.root, textvariable=self.bbb)
        lab.place(relx=0.3,rely=0.8)
        
        self.root.mainloop()

    def draw(self):
        global x,y
        canvas = Canvas(self.root, width=300, height=200)
        canvas.create_oval(5,5,195,195,fill='white',outline='black',width=5)
        canvas.create_line(100,100,x,y,fill='black',width=5)
        canvas.place(relx=0.175,rely=0.1)
        self.root.after(1000, self.draw)

    def hands(self,deg):
        global x, y, canvas
        x = (100 * math.sin(math.radians(deg)))
        y = (100 * math.sin(math.radians(90 - deg)))
        self.bbb.set('%02d:%02d' % (x, y))

    def tick(self):
        global secs, deg
        secs += 1
        deg += 6
        self.hands(deg)
        self.aaa.set('%03d' % (secs))
        self.root.after(1000, self.tick)
    

Analog()
