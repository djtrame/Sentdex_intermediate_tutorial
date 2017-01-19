from tkinter import *

#this file simply has us import * instead of aliasing all tkinter stuff with tk, which i like better
#main window and/or parent widget
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        #pack this into our frame
        self.pack(fill=BOTH, expand=1)

        #create a button instance
        quitButton = Button(self, text='Quit')

        quitButton.place(x=0, y=0)

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
