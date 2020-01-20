from tkinter_source_file import *

# Screen Size Data
HEIGHT = 800
WIDTH = 800

# Root
root = Tk()

# Screen Size
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# To organize widgets use Frame
frame = Frame(root,bg='blue')
#relwidth = relative width, relheight= relative height
frame.place(relwidth=1,relheight=1)


button = Button(root, text='Testing Button', bg='Gray', fg='red')
button.pack()
root.mainloop()