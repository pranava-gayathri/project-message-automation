import time
from tkinter import *
import winsound
import pywhatkit
def countdown(t):
    root = Tk()
    root.geometry("300x250")
    root.title("Time Counter")
    hour=StringVar()
    minute = StringVar()
    second = StringVar()
    h, m, s = map(int, t.split(":"))
    hr = int(time.strftime("%H"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    hour.set(h-hr)
    minute.set((m-mn+1))
    second.set((s-sec-50))
    hourEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=hour)
    hourEntry.place(x=80, y=20)
    minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=minute)
    minuteEntry.place(x=140, y=20)
    secondEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=second)
    secondEntry.place(x=200, y=20)
    def submit():
        try:
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        except:
            print("Please input the right value")
        while temp > -1:

            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            root.update()
            time.sleep(1)
            temp -= 1
        if(int(hour.get())==0 and int(minute.get())==0 and int(second.get())==0):
            root.destroy()
            winsound.Beep(4500,300)
            pywhatkit.sendwhatmsg('+916304215015','hi',h,m+1)
    submit()
    root.mainloop()
countdown(input("Enter time :"))