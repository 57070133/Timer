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
        lab.pack(pady=15, padx=30)
        
        self.root.mainloop()
        
    def count(self):
        '''
        count() --> makes timer update every 50 millisecs // name after part for using in stop
        '''
        if not self.run: 
            self.run = True
        self.elapsed = time.time() - self.start
        self.display(self.elapsed)
        self.counter = self.after(50, self.count)

    def display(self, time):
        '''
        display(time) --> set floating point format into 00:00:00:00 format
        '''
        hrs = int(time / 3600)
        mins = int((time - hrs*3600.0) /60 )
        secs = int(time - hrs*3600.0 - mins*60.0)
        msecs = int((time - hrs*3600.0 - mins*60.0 - secs)*100)
        self.timedis.set('%02d:%02d:%02d:%02d' % (hrs, mins, secs, msecs))

