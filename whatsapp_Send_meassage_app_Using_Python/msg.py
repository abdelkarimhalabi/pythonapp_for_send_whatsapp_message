from tkinter import *
import pywhatkit as kit
window = Tk()

window.title("Abdelkarim whtasapp automation")

window.geometry('350x200')

lbl = Label(window, text="Enter phone number here ")

lbl.grid(column=0, row=0)

pn = Entry(window,width=20)

pn.grid(column=1, row=0)

lb2 = Label(window,text="Enter your message here: ")
lb2.grid(column=0,row=2)

msg = Entry(window,width=20)
msg.grid(column=1,row=2)

lb3 = Label(window,text="Enter the time that you want the message arrive: ")
lb3.grid(column=0,row=3)
tm = Entry(window,width=20)
tm.grid(column=1,row=4)
lb = Label(window,text="Hour : ")
lb.grid(column=0,row=4)
mnl = Label(window,text="Minute : ")
mnl.grid(column=0,row=5)
mn = Entry(window,width=20)
mn.grid(column=1,row=5)
def sendmsg():

    kit.sendwhatmsg(pn.get(),msg.get(),int(tm.get()),int(mn.get()))

btn = Button(window, text="Send wp message" ,command=sendmsg)

btn.grid(column=0, row=6)

window.mainloop()

