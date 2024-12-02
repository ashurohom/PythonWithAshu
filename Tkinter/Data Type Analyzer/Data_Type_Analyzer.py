from tkinter import *

window = Tk()
window.geometry("666x444")
window.title("CodeCraftedByAshuRohom - Data Type Analyzer")

def checkval():
    input_value = ValueEntry.get()  
    ValueAnswer.delete(0, END)  

    if input_value.lower() in ['true', 'false']:
            ValueAnswer.insert(0, "Boolean")
    elif input_value.isdigit():  
        ValueAnswer.insert(0, "Number")
    elif input_value.isalpha():  
        ValueAnswer.insert(0, "String")
    elif input_value.isalnum():  
        ValueAnswer.insert(0, "Alphanumeric")
    elif input_value.lower() in ['+','-','*','/','!','@','#','$','%','^',',&',"?"]:
         ValueAnswer.insert(0, "Symbol")    
    else: 
        ValueAnswer.insert(0, "Invalid Input")


f1 = Frame(window)
f1.grid(row=0, column=0, columnspan=3, pady=20)

l1 = Label(f1, text="Data Type Analyzer", font="lucida 25 bold", fg="red")
l1.grid(row=0, column=0)

l2 = Label(f1, text="CodeCraftedByAshu", font="lucida 8 bold", fg="orchid")
l2.grid(row=1, column=0)


f2 = Frame(window)
f2.grid(row=1, column=0, columnspan=3, pady=20)

Note = Label(f2, text="Number String Boolean Symbol Alphanumeric", font="comicsansms 10 bold", fg="yellow")
Note.grid(row=0, column=1, padx=10, pady=5)

UserInput = Label(f2, text="Enter Value : ", font="comicsansms 10 bold", fg="Black")
UserInput.grid(row=1, column=0, padx=10)  

ValueEntry = Entry(f2)
ValueEntry.grid(row=1, column=1, padx=10)  


AnswerLable = Label(f2, text="Answer : ", font="comicsansms 10 bold", fg="Black")
AnswerLable.grid(row=2, column=0, padx=10)

ValueAnswer = Entry(f2)
ValueAnswer.grid(row=2, column=1, columnspan=2, pady=10)


b1 = Button(f2, text="Check", command=checkval, bg="Black", fg="White",font="comicsansms 10 bold", border=2, relief=RIDGE)
b1.grid(row=3, column=1, pady=10)

b2 = Button(f2, text="Exit", command=quit, bg="Black", fg="White", font="comicsansms 10 bold", border=2, relief=RIDGE)
b2.grid(row=4, column=1, pady=10)


window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
