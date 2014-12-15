'''
Timer(Stopwatch) with laps system display in both digital label and analog clock.
'''
from Tkinter import *
import time, math

class Timer():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("350x800")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.title('Timer')
        
        self.start = 0.0
        self.elapsed = 0.0
        self.timedis = StringVar()
        self.run = False

        self.r = 100
        self.margin = 20
        self.x = self.r
        self.y = 0

        #digital time display
        self.display(self.elapsed)
        lab= Label(self.root, textvariable=self.timedis, font=('OCRAStd', 20), fg='black')
        lab.place(relx=0.5,rely=0.42, anchor=CENTER)

        #laps label
        lab2= Label(self.root, text='Laps', font=('OCRAStd', 12), fg='black', relief=GROOVE, bd=3)
        lab2.place(relx=0.5,rely=0.59, anchor=CENTER)

        #text box for contains laps
        self.lapdis = Text(self.root, height=10, width=18, font=('BatangChe', 16), bd=0, state='disable')
        self.lapdis.place(relx=0.2,rely=0.62)

        #scrollbar for laps textbox
        self.sb = Scrollbar(self.root)
        self.sb.config(command=self.lapdis.yview)
        self.lapdis.config(yscrollcommand=self.sb.set)
        self.sb.place(relx=0.75,rely=0.62, relheight=0.265)

        #canvas for analog clock
        self.canvas = Canvas(self.root, width=self.r*2+self.margin*2, height=self.r*2+self.margin*2)
        self.draw()
        self.canvas.place(relx=0.5,rely=0.2, anchor=CENTER)

        #menu
        self.menu = Menu(self.root)
        help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Help', menu=help_menu)
        self.root.config(menu=self.menu)
        help_menu.add_command(label='User Guide', command=self.userguide)
        help_menu.add_command(label='About...', command=self.about)
        
        #button        
        self.ss_button = Button(self.root, text='Start', command=self.start_time)
        self.ss_button.place(relx=0.2,rely=0.47)
        Button(self.root, text='Laps', command=self.laps).place(relx=0.45,rely=0.47)
        Button(self.root, text='Reset', command=self.reset_time).place(relx=0.7,rely=0.47)
        Button(self.root, text='Clear', command=self.clear_laps).place(relx=0.45,rely=0.92)

        
        self.root.mainloop()

    def about(self):
        '''about window'''
        window = Tk()
        window.title('About')
        window.geometry('300x300')
        lab = Label(window, text='Timer', font=('OCRAStd', 20))
        lab.place(relx=0.1, rely=0.1)
        msg = "Timer project"+"\n - - - - - - - - - - - - - "\
              +"\n\nThis project is dedicated to PROBLEM SOLVING IN INFORMATION TECHNOLOGY(PSIT) course at IT Faculty, KMITL."\
              + "\n\nBy  #57070129 Salinee T."+"\n    #57070133 Suchanun C."
        text = Text(window, height=15, width=30, bg='#F0F0ED', bd=0, wrap=WORD)
        text.insert(END, msg)
        text.place(relx=0.1, rely=0.3)
        text.configure(state='disabled')
        window.mainloop()

    def userguide(self):
        '''user guide window'''
        window = Tk()
        window.title('User Guide')
        window.geometry('450x150')
        lab = Label(window, text='How to use', font=('OCRAStd', 20))
        lab.place(relx=0.1, rely=0.1)
        msg = "\nUse 'Start' button to start and stop the timer.\n"+"Use 'Laps' button to create laps.\n"\
              +"Use 'Reset' button to reset the timer.\n"+"Use 'Clear' button to clear laps.\n"
        text = Text(window, height=15, width=50, bg='#F0F0ED', bd=0, wrap=WORD)
        text.insert(END, msg)
        text.place(relx=0.05, rely=0.3)
        text.configure(state='disabled')
        window.mainloop()
        
    def count(self):
        '''
        count() --> makes timer update every 50 millisecs // name after part for using in stop
        '''
        self.elapsed = time.time() - self.start
        deg = 90 - (self.elapsed * 6)
        self.hand_point(self.r, deg)
        self.display(self.elapsed)
        self.draw()
        self.counter = self.root.after(10, self.count)
        
    def display(self, time):
        '''
        display(time) --> set the elapsed time into 00:00:00:00 format
        '''
        hrs = int(time / 3600)
        mins = int((time - hrs*3600.0) /60 )
        secs = int(time - hrs*3600.0 - mins*60.0)
        msecs = int((time - hrs*3600.0 - mins*60.0 - secs)*100)
        self.timedis.set('%02d:%02d:%02d:%02d' % (hrs, mins, secs, msecs))
        
    def start_time(self):
        '''start/stop button'''
        if  not self.run:
            self.start = time.time() - self.elapsed #if cut " - self.elapsed" part, the clock will automatically went back to 0
            self.count()
            self.ss_button.config(text='Stop')
            self.run = True
        elif  self.run:
            self.root.after_cancel(self.counter)
            self.display(self.elapsed)
            self.ss_button.config(text='Start')
            self.run = False

    def reset_time(self):
        '''reset button'''
        self.root.after_cancel(self.counter)
        self.ss_button.config(text='Start')
        self.elapsed =  0.0
        self.display(self.elapsed)
        self.x = self.r
        self.y = 0
        self.draw()
        self.run = False

    def laps(self):
        '''create laps time'''
        self.lapdis.configure(state='normal')
        self.lapdis.insert(END, (self.timedis.get() + "\n"))
        self.lapdis.see(END)
        self.lapdis.configure(state='disabled')

    def clear_laps(self):
        '''clear laps data from textbox'''
        self.lapdis.configure(state='normal')
        self.lapdis.delete(1.0, END)
        self.lapdis.configure(state='disabled')

    def hand_point(self, r, deg):
        '''calculate where the clock hand should be '''
        self.x = r + int(r * math.cos(math.radians(deg)))
        self.y = r -  int(r  * math.sin(math.radians(deg)))
        return (self.x, self.y)

    def draw(self):
        '''draw the clock face and hand'''
        self.canvas.delete(ALL)
        margin = self.margin
        step = 30
        step2 = 6
        self.canvas.create_oval(margin,margin,self.r*2+margin,self.r*2+margin,fill='white',outline='black')
        self.canvas.create_oval(margin*5.8,margin*5.8,self.r*2-margin*3.8,self.r*2-margin*3.8,fill='red', outline='red')
        self.canvas.create_line(self.r+margin,self.r+margin,self.x+margin,self.y+margin, fill='red')
        for i in xrange(12): #draw the numbers around the clock
            angle = i*step
            temp = self.hand_point(self.r*1.1, 90 - angle)
            self.canvas.create_text(temp[0]+10, temp[1]+10,text=str(i*5))
        for i in xrange(12): #draw a long secs mark
            angle = i*step
            temp = self.hand_point(self.r, angle)
            temp2 = self.hand_point(self.r*0.8, angle)
            self.canvas.create_line(temp[0]+margin, temp[1]+margin,temp2[0]+40, temp2[1]+40, )
        for i in xrange(60): #draw a secs mark
            angle = i*step2
            if i % 5 != 0:
                temp = self.hand_point(self.r, angle)
                temp2 = self.hand_point(self.r*0.9, angle)
                self.canvas.create_line(temp[0]+margin, temp[1]+margin,temp2[0]+30, temp2[1]+30 )
                
Timer()
