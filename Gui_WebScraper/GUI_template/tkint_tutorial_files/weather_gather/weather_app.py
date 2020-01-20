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
button.pack()

# Just a Label
label = Label(frame, text='Hello this is a label', bg='yellow')
label.pack()

# User Typing Enabled
entry = Entry(frame, bg='green')
entry.pack()

button.pack()
root.mainloop()