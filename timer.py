'''
Timer(Stopwatch) with laps system display in both digital label and analog clock.
'''
from Tkinter import *
import time, math

class Timer():
    def __init__(self):
        '''
        main
        '''
        self.root = Tk()
        self.root.minsize(500,300)
        self.root.maxsize(500,300)
        self.root.geometry("500x300")
        self.root.title('Timer')
        self.start = 0.0
        self.elapsed = 0.0
        self.timedis = StringVar()
        self.run = False

        self.display(self.elapsed)
        lab= Label(self.root, textvariable=self.timedis)
        lab.place(relx=0.2,rely=0.1, anchor=CENTER)
        
        self.lapdis = Text(self.root, height=10, width=20)
        self.lapdis.place(relx=0.05,rely=0.2)
        
        self.sb = Scrollbar(self.root)
        self.sb.config(command=self.lapdis.yview)
        self.lapdis.config(yscrollcommand=self.sb.set)
        self.sb.place(relx=0.35,rely=0.2, relheight=0.55)

        self.deg = 0
        self.r = 100
        self.x = self.r
        self.y = 0


        self.canvas = Canvas(self.root, width=self.r*3, height=self.r*3)
        self.draw()
        self.canvas.place(relx=0.5,rely=0.075)
        
        Button(self.root, text='Start/Stop', command=self.start_time).place(relx=0.05,rely=0.8)
        Button(self.root, text='Laps', command=self.laps).place(relx=0.2,rely=0.8)
        Button(self.root, text='Reset', command=self.reset_time).place(relx=0.3,rely=0.8)
        Button(self.root, text='Clear', command=self.clear_laps).place(relx=0.4,rely=0.8)

        
        self.root.mainloop()
        
    def count(self):
        '''
        count() --> makes timer update every 50 millisecs // name after part for using in stop
        '''
        self.elapsed = time.time() - self.start
        self.deg = 90 - (self.elapsed * 6)
        
        self.hand_point(self.deg)
        self.display(self.elapsed)
        self.draw()
        self.counter = self.root.after(50, self.count)

    def display(self, time):
        '''
        display(time) --> set floating point format into 00:00:00:00 format
        '''
        hrs = int(time / 3600)
        mins = int((time - hrs*3600.0) /60 )
        secs = int(time - hrs*3600.0 - mins*60.0)
        msecs = int((time - hrs*3600.0 - mins*60.0 - secs)*100)
        self.timedis.set('%02d:%02d:%02d:%02d' % (hrs, mins, secs, msecs))
        
    def start_time(self):
        '''start/stop button'''
        if  not self.run:
            self.start = time.time() - self.elapsed
            self.count()
            self.run = True
        elif  self.run:
            self.root.after_cancel(self.counter)
            self.display(self.elapsed)
            self.run = False

    def reset_time(self):
        '''reset button'''
        self.root.after_cancel(self.counter)
        self.elapsed =  0.0
        self.display(self.elapsed)
        self.x = self.r
        self.y = 0
        self.draw()
        self.run = False

    def laps(self):
        '''create laps time'''
        self.lapdis.insert(END, (self.timedis.get() + "\n"))
        self.lapdis.see(END)

    def clear_laps(self):
        '''clear laps data from textbox'''
        self.lapdis.delete(1.0, END)

    def hand_point(self, deg):
        self.x = self.r + int(self.r * math.cos(math.radians(deg)))
        self.y = self.r -  int(self.r  * math.sin(math.radians(deg)))

    def draw(self):
        self.canvas.delete(ALL)
        self.canvas.create_oval(10,10,(self.r*2+10),(self.r*2+10),fill='white',outline='black',width=2)
        self.canvas.create_line((self.r+10),(self.r+10),(self.x+10),(self.y+10),fill='black',width=1)



Timer()
