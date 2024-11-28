from tkinter import *
window = Tk()
window.geometry("655x455")
window.title("Ashu Rohom")

def getvals():
    print(uservalue.get())
    print(passvalue.get())


#variable Classes
# BooleanVar, DoubleVar, IntVar, StringVar

user = Label(window,text="Username")
password = Label(window,text="Password")
user.grid()
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(window, textvariable=uservalue)
passentry = Entry(window, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit", command=getvals).grid()

window.mainloop()