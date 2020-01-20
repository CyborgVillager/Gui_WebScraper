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
frame = Frame(root,bg='#99b3ff')
#relwidth = relative width, relheight= relative height
# This makes the frame centered using relx=0.1, rely=0.1 -> Also adjusts with the user's screen
#frame.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.8)

frame.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.8)
button = Button(frame, text='Testing Button', bg='Gray')
# button.pack(side="left", fill='both') -> example on filing the whole left screen to an extent
# button.pack(side="left", fill='both', expand=True) -> bigger
button.grid(row=0,column=0)

# Just a Label
label = Label(frame, text='Hello this is a label', bg='yellow')
label.grid(row=0,column=1)

# User Typing Enabled
entry = Entry(frame, bg='green')
entry.grid(row=0,column=2)


root.mainloop()