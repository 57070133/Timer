'''
Timer(Stopwatch) with laps system display in both digital label and analog clock.
'''
from Tkinter import *
import time

class Timer():
    def __init__(self):
        '''
        main
        '''
        self.root = Tk()
        self.root.title('Timer')
        self.start = 0.0
        self.elapsed = 0.0
        self.timedis = StringVar()
        self.run = False
        
        lab= Label(self.root, textvariable=self.timedis)
        self.display(self.elapsed)
        lab.pack(pady=30, padx=80)

        self.lapdis = Text(self.root, height=10, width=20)
        self.lapdis.pack()
        
        Button(self.root, text='Start', command=self.start_time).pack(side=TOP)
        Button(self.root, text='Laps', command=self.laps).pack(side=TOP)
        Button(self.root, text='Stop', command=self.stop_time).pack(side=TOP)
        Button(self.root, text='Reset', command=self.reset_time).pack(side=TOP)

        
        self.root.mainloop()
        
    def count(self):
        '''
        count() --> makes timer update every 50 millisecs // name after part for using in stop
        '''
        self.elapsed = time.time() - self.start
        self.display(self.elapsed)
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
        '''start button'''
        if  not self.run:
            self.start = time.time() - self.elapsed
            self.count()
            self.run = True
                
    def stop_time(self):
        '''stop button'''
        if  self.run:
            self.root.after_cancel(self.counter)
            self.display(self.elapsed)
            self.run = False

    def reset_time(self):
        '''reset button'''
        self.root.after_cancel(self.counter)
        self.elapsed =  0.0
        self.display(self.elapsed)
        self.run = False

    def laps(self):
        '''create laps time'''
        self.lapdis.insert(END, (self.timedis.get() + "\n"))
Timer()

