import tkinter as tk
from PIL import Image, ImageTk


#main window and/or parent widget
class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        #pack this into our frame
        self.pack(fill=tk.BOTH, expand=1)

        #create a button instance
        #quitButton = tk.Button(self, text='Quit', command=self.client_exit)

        #quitButton.place(x=0, y=0)

        #this is a menu of the main window
        myMenu = tk.Menu(self.master)

        #define the menu
        self.master.config(menu=myMenu)

        #create the File button in the menu
        myFile = tk.Menu(myMenu)
        myFile.add_command(label='Save')
        myFile.add_command(label='Exit', command=self.client_exit)
        myMenu.add_cascade(label='File', menu=myFile)

        myEdit = tk.Menu(myMenu)
        myEdit.add_command(label='Undo')
        myEdit.add_command(label='Show Image', command=self.showImg)
        myEdit.add_command(label='Show Text', command=self.showTxt)
        myMenu.add_cascade(label='Edit', menu=myEdit)

    def showImg(self):
        load = Image.open('C:\\Code\\David_Python_Testing\\apple.png')
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = tk.Label(self, text='Hey der')
        text.pack()

    def client_exit(self):
        exit()

root = tk.Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
