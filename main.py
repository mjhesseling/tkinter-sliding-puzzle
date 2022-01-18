import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk

class Gui():
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.img = ImageTk.PhotoImage(Image.fromarray(data, 'RGB'))
        self.canvas = tk.Canvas(root, width=data.shape[1], height=data.shape[0])
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.grid(row=0, column=0)
        cFrame = ttk.Frame(root, height=100)
        cFrame.grid(row=1, column=0)
        qButton = ttk.Button(cFrame, text='Quit uwu')
        qButton.grid(row=0, column=0)

    def onKeyPress(self, event):
        return

if __name__ == '__main__':
    root = tk.Tk()
    
    w, h = 512, 512
    data = np.zeros((w,h,3), dtype=np.uint8)
    data[0:256, 0:256] = [255, 0, 0]
    data[0:256, 256:512] = [0, 255, 0]

    gui = Gui(root, data)
    root.mainloop()
