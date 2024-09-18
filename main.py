import tkinter as tk
from PIL import ImageTk, Image

ss = Image.open("mario.png")

framelist = []

window = tk.Tk()

for i in range(0,5):
    box = (0, 0+(i*16), 16, 32+(i*16))
    region = ss.crop(box)
    frame = region.resize((80, 160))
    frame = ImageTk.PhotoImage(frame)
    framelist.append(frame)


window.resizable(False, False)
window.overrideredirect(1)

window.geometry('80x160+200+200')

label = tk.Label(window,bd=0,bg='#010101')
label.config(image=framelist[0])

window.wm_attributes('-transparentcolor','#010101')

label.pack()
