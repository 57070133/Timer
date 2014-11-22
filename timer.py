from Tkinter import *
import time

class Timer():
    def __init__(self):
        self.start = 0.0
        self.elapsed = 0.0
        self.timedis = StringVar()
        self.widget()

    def count(self):
        self.elapsed = time.time() - self.start
        self.display(self.elapsed)
        self.counter = self.after(50, self.count)

    def display(self, time):
        hrs = int(time / 3600)
        mins = int((time - hrs*3600.0) /60 )
        secs = int(time - hrs*3600.0 - mins*60.0)
        msecs = int((time - hrs*3600.0 - mins*60.0 - secs)*100)
        self.timedis.set('%02d:%02d:%02d:%02d' % (hrs, mins, secs, msecs))

