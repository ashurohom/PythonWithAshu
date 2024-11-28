from tkinter import *
window = Tk()

#set height and width manully
canvas_height = 800
canvas_width = 400
window.geometry(f'{canvas_height}x{canvas_width}')
window.title("Ashu Rohom")

can_widget = Canvas(window, width=canvas_width, height=canvas_height)
can_widget.pack()

#the line goes from the point x1,y1, to x2,y2
can_widget.create_line(0,0,800,40, fill="blue")
can_widget.create_line(0,400,800,0)
can_widget.create_line(0,0,500,10)

#to create rectangle
can_widget.create_rectangle(3, 5, 700, 300, fill="skyblue")





window.mainloop()