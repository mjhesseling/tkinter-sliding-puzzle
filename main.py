import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk

class Gui():
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.empty = [0, 0]
        self.flags = [1, 0, 1, 0] # Up, down, left, right

        self.img = ImageTk.PhotoImage(Image.fromarray(self.data, 'RGB'))
        self.canvas = tk.Canvas(root, width=data.shape[1], height=data.shape[0])
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.canvas.grid(row=0, column=0)
        cFrame = ttk.Frame(root, height=100)
        cFrame.grid(row=1, column=0)
        qButton = ttk.Button(cFrame, text='Quit uwu')
        qButton.grid(row=0, column=0)

    def onKeyPress(self, event):
        # Defining our valid key inputs as WASD.
        # Based on input direction, slide our "tiles" in specified direction (i.e. move array values along direction and fill in zeros in update empty space location)
        print(event.char)
        if event.char == 'w' and self.flags[0]: # Up
            self.data[self.empty[0]:self.empty[0]+128, self.empty[1]:self.empty[1]+128, :] = \
                    self.data[self.empty[0]+128:self.empty[0]+256, self.empty[1]:self.empty[1]+128, :]
            self.empty[0] += 128
            self.flags[1] = 1
            if self.empty[0] >= 384:
                self.flags[0] = 0
        elif event.char == 's' and self.flags[1]: # Down
            self.data[self.empty[0]:self.empty[0]+128, self.empty[1]:self.empty[1]+128, :] = \
                    self.data[self.empty[0]-128:self.empty[0], self.empty[1]:self.empty[1]+128, :]
            self.empty[0] -= 128
            self.flags[0] = 1
            if not self.empty[0]:
                self.flags[1] = 0
        elif event.char == 'a' and self.flags[2]: # Left
            self.data[self.empty[0]:self.empty[0]+128, self.empty[1]:self.empty[1]+128, :] = \
                    self.data[self.empty[0]:self.empty[0]+128, self.empty[1]+128:self.empty[1]+256, :]
            self.empty[1] += 128
            self.flags[3] = 1
            if self.empty[1] >= 384:
                self.flags[2] = 0
        elif event.char == 'd' and self.flags[3]: # Right
            self.data[self.empty[0]:self.empty[0]+128, self.empty[1]:self.empty[1]+128, :] = \
                    self.data[self.empty[0]:self.empty[0]+128, self.empty[1]-128:self.empty[1], :]
            self.empty[1] -= 128
            self.flags[2] = 1
            if not self.empty[1]: # i.e. it hits 0
                self.flags[3] = 0
        else: # Work around to ignore inputs other than WASD, need to find a prettier way
            return

        self.data[self.empty[0]:self.empty[0]+128, self.empty[1]:self.empty[1]+128,  :] = 0
        
        self.img = ImageTk.PhotoImage(Image.fromarray(self.data, 'RGB'))
        self.canvas.create_image(0, 0, anchor='nw', image=self.img)

if __name__ == '__main__':
    root = tk.Tk()
    
    w, h = 512, 512
    data = np.zeros((w,h,3), dtype=np.uint8)
    for irow in range(4):
        for icol in range(4):
            data[irow*128:(irow+1)*128, icol*128:(icol+1)*128] = [irow*80, icol*80, (irow+icol)*40]

    gui = Gui(root, data)
    root.bind('<KeyPress>', gui.onKeyPress)
    root.mainloop()
