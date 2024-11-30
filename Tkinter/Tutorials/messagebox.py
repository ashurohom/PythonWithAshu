from tkinter import *
import tkinter.messagebox as tmsg
window = Tk()
window.geometry("655x455")
window.title("Ashu Rohom")

def myfun():
    print("MyFun")

#open new dialogbox
def help():
    print("How I Can Help You..?")
    tmsg.showinfo("Help", "Ashu Will Help You")


#Yes No Button
def rate():
    print("Rate Us")  
    value = tmsg.askquestion("Tell Me","Love or Not")    
    print(value)

    if value == "yes":
        msg = "Great,, Awesome"
    else:
        msg = "We Will Upgrade"  

    tmsg.showinfo("Exp",msg)     

#menubar with list

menubar = Menu(window)
m3 = Menu(menubar, tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="RateUs",command=rate)
window.config(menu=menubar)
menubar.add_cascade(label="Help",menu=m3)




window.mainloop()