from Tkinter import *
import re
def birthday():
    p=e1.get()
    q=str(e2.get())
    r=str(e3.get())
    sample="Name:"+p+" "+"Birthdaydate:"+q+" "+"Alarmtime:"+r
    file1=open("birthdaydetails.txt","a")
    file1.write(sample)
    file1.write("\n")
    file1.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    print "done"
    execfile("/home/akshat/Documents/birthdaypro.py")
window = Tk()
window.title("Birthday Alarm")
A=Label(window, text="Name")
G=Label(window, text="Birthday date")
l=Label(window, text="Alarm time")
A.grid(row=0,column=0)
G.grid(row=1,column=0)
l.grid(row=2,column=0)
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
Q=Button(window,text="Save",fg="Blue",command=birthday) 
W=Button(window,text="Quit",fg="Red",command=window.destroy)
W.grid(row=3, column=0)
Q.grid(row=3,column=2)
window.mainloop()


