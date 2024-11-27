from tkinter import *
window = Tk()

window.geometry("555x555")

window.title("Ashitosh Rohom")

# imp lable option
'''
text : add text
bd : background
fg : foreground
font : set font
1) font=("comicsansms", 10, "bold")
2) font="comicsansms 10 bold"
padx : x padding
pady : y padding
relife : border styling : SUNKEN,RAISED,GROOVE,RIDGE
'''
Label1 = Label(text=''' The ASUS Vivobook S15 OLED is a sleek, lightweight laptop with 
               vibrant OLED display, powerful performance, and stylish design. Ideal 
               for multitasking, entertainment, and productivity, it combines functionality 
               and elegance effortlessly.''',bg="pink",fg="blue",padx=20,pady=20,
               font="comicsansms 10 bold", border=3, relief=RIDGE)



# Importent Pack Options
'''
anchor = nw,ne,sw,se (north,west) 
side = top,bottom,left,right
fill = x,y (responsive)
padx
pady

'''


# Label1.pack(side="bottom", anchor="sw", fill=X)
Label1.pack(side="bottom", anchor="sw", fill=Y, padx=10, pady=10)

window.mainloop()