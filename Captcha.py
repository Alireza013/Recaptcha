"""write program to create re-captcha password with python
use libraries"""

# import useful libraries
from random import choice, randint
from captcha.image import ImageCaptcha
from tkinter import *
import string


#for gui window
root = Tk()
root.title("Re-captcha")
canvas = Canvas(root, width=300, height=300)
canvas.pack()


#for create captcha
cap = ImageCaptcha(width=280, height=90)
ps = string.ascii_letters + string.digits
c_text = "".join(choice(ps) for w in range(randint(4, 6)))

data = cap.generate(c_text)
cap.write(c_text , "pass.jpg")


#for show captcha
img = PhotoImage(file = "pass.jpg")
canvas.create_image(20,20,anchor = NW, image = img)


#for textbox
txt = Entry(root)
canvas.create_window(150, 140, window=txt)


#check captcha
def check():
    if txt.get() == c_text:
        lbl['text'] = "True"
    else:
        lbl['text'] = "False!"


#for check button
btn = Button(root, text="Check!", command=check)
btn.place(x = 120,y=160)


#for label
lbl = Label(root, text= "Enter Captcha!")
lbl.place(x = 120, y= 200)


mainloop()
# Codded by Alireza Rahimi