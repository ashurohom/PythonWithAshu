from tkinter import *
window = Tk()
window.geometry("655x455")
window.title("Ashu Rohom")

def myfun():
    print("MyFun")

#used to create a menubar
mymenu = Menu(window)
mymenu.add_command(label="File",command=myfun)
mymenu.add_command(label="File",command=quit)
window.config(menu=mymenu)

#menubar with list

menubar = Menu(window)
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="New",command=myfun)
m1.add_command(label="Save",command=myfun)
m1.add_command(label="Save As",command=myfun)

#make a line seprate
m1.add_separator()

m1.add_command(label="Print",command=myfun)
m1.add_command(label="Delete",command=myfun)
window.config(menu=menubar)
menubar.add_cascade(label="File",menu=m1)





m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Cut",command=myfun)
m2.add_command(label="Copy",command=myfun)
m2.add_command(label="Paste",command=myfun)
m2.add_command(label="Find",command=myfun)
m2.add_command(label="More",command=myfun)
window.config(menu=menubar)
menubar.add_cascade(label="Edit",menu=m2)









window.mainloop()