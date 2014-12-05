from Tkinter import *
import time

class Analog():
    def __init__(self):
        '''
        main
        '''
        self.root = Tk()
        self.root.geometry("300x300")

        canvas = Canvas(self.root, width=300, height=200)
        canvas.create_oval(5,5,195,195,fill='white',outline='black',width=5)
        canvas.create_line(100,100,100,10,fill='black',width=5)
        canvas.place(relx=0.175,rely=0.1)

        self.root.mainloop()

Analog()
