from tkinter import *
window = Tk()
window.geometry("655x455")
window.title("Ashu Rohom")

def getval():
    print("Form Submitted..!")
    print(f'{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), servicevalue.get()}')

    with open("Record.txt",'a')as f:
        f.write(f'{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), servicevalue.get()}\n')


#heading
Label(window, text="WelCome To Ashu's Work Area",font="comicsansms 13 bold",padx=50).grid(row=0,column=3)


#Lable for forms
name = Label(window, text="Name")
phone = Label(window, text="Phone")
gender = Label(window, text="Gender")
paymentmode = Label(window, text="PaymentMode")


# pack text using grid
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentmode.grid(row=4, column=2)


#create variable 
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentmodevalue = StringVar()
servicevalue = IntVar()

#create entry
nameentry = Entry(window, textvariable=namevalue)
phoneentry = Entry(window, textvariable=phonevalue)
genderentry = Entry(window, textvariable=gendervalue)
paymentmodeentry = Entry(window, textvariable=paymentmodevalue)


#packing entry
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymentmodeentry.grid(row=4, column=3)


#checkbox
foodservice = Checkbutton(text="Want to pre book your meals?", variable=servicevalue)
foodservice.grid(row=6, column=3)

#button and pack it
Button(text="Submit", command=getval).grid(row=7, column=3)

window.mainloop()