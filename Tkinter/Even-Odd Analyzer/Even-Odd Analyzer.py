from tkinter import *

window = Tk()
window.geometry("666x444")
window.title("CodeCraftedByAshuRohom - Even-Odd Analyzer")

def checkval():
    try:
        number = int(ValueEntry.get())  # Get the value as an integer
        ValueAnswer.delete(0, END)  # Clear previous value in the display field
        if number % 2 == 0:
            ValueAnswer.insert(0, "Even Number")
        else:
            ValueAnswer.insert(0, "Odd Number")
    except ValueError:
        ValueAnswer.delete(0, END)
        ValueAnswer.insert(0, "Invalid Input")

# Frame f1 (title section)
f1 = Frame(window)
f1.grid(row=0, column=0, columnspan=3, pady=20)

l1 = Label(f1, text="Even-Odd Analyzer", font="lucida 25 bold", fg="red")
l1.grid(row=0, column=0)

l2 = Label(f1, text="CodeCraftedByAshu", font="lucida 8 bold", fg="orchid")
l2.grid(row=1, column=0)

# Frame f2 (input section)
f2 = Frame(window)
f2.grid(row=1, column=0, columnspan=3, pady=20)

# Label and Entry widget
UserInput = Label(f2, text="Enter Value : ", font="comicsansms 10 bold")
UserInput.grid(row=0, column=0, padx=10)  # Position the label in the first column

ValueEntry = Entry(f2)
ValueEntry.grid(row=0, column=1, padx=10)  # Position the entry field in the second column


AnswerLable = Label(f2, text="Answer : ", font="comicsansms 10 bold")
AnswerLable.grid(row=1, column=0, padx=10)

# display result section
ValueAnswer = Entry(f2)
ValueAnswer.grid(row=1, column=1, columnspan=2, pady=10)



# Button to check result
b1 = Button(f2, text="Check", command=checkval, bg="Black", fg="White",font="comicsansms 10 bold", border=2, relief=RIDGE)
b1.grid(row=2, column=0, pady=10)

b2 = Button(f2, text="Exit", command=quit, bg="Black", fg="White", font="comicsansms 10 bold", border=2, relief=RIDGE)
b2.grid(row=2, column=1, pady=10)



# Center content by configuring grid columns
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()
