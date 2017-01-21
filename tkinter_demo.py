import tkinter as tk
from PIL import Image, ImageTk


#main window and/or parent widget
class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.master = master
        self.scale_factor = 1
        self.canvas = tk.Canvas(self)

        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        #pack this into our frame
        self.pack(fill=tk.BOTH, expand=1)

        #canvas = tk.Canvas(self)
        self.canvas.create_line(300, 35, 300, 200)
        self.canvas.create_line(15, 25, 200, 25, dash=(4, 2))
        self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        self.canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#05f")
        self.canvas.pack(fill=tk.BOTH, expand=1)

        points = [150, 100, 200, 120, 240, 180, 210,
                  200, 150, 150, 100, 200]
        self.canvas.create_polygon(points, outline='red',
                              fill='green', width=2)



        self.master.bind("<MouseWheel>", self.zoom)



        #create a button instance
        quitButton = tk.Button(self, text='Quit', command=self.client_exit)

        quitButton.place(x=0, y=0)

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

    def zoom(self, event):
        if event.delta > 0:
            self.scale_factor = 1.1
            print('Zoom in!  New scale factor: ' + str(self.scale_factor))
        else:
            self.scale_factor = 0.9
            print('Zoom out!  New scale factor: ' + str(self.scale_factor))

        self.canvas.scale(tk.ALL, 0, 0, self.scale_factor, self.scale_factor)

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
root.geometry("800x600")

app = Window(root)

root.mainloop()
