
from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text



root = Tk()
root.title("AshuWorld News - Morning NEWS")
root.geometry("800x1000")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    #TODO : image = image.resize((225, 265), Image.ANTIALIAS)   ANTIALIAS used in old version
    image = image.resize((225, 265), Image.Resampling.LANCZOS)  #Resampling.LANCZOS used in new version

    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=500, height=70)
Label(f0, text="Ashu World NEWS", font="lucida 33 bold").pack()
Label(f0, text="November 29, 2024", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=100, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=100, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")


f3 = Frame(root, width=900, height=100, pady=34)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")




root.mainloop()

