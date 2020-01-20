from tkinter_source_file import *

# Screen Size Data
HEIGHT = 800
WIDTH = 800

# Root
root = Tk()

# Screen Size
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# To organize widgets use Frame , bd = border
frame = Frame(root,bg='#99b3ff', bd=5)
# relwidth = relative width, relheight= relative height
# This makes the frame centered using relx=0.1, rely=0.1 -> Also adjusts with the user's screen
# frame.place(relx=0.1, rely=0.1,relwidth=0.8,relheight=0.8)
frame.place(relx=0.5, rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')
button = Button(frame, text='Testing Button', font=40)
# button.pack(side="left", fill='both') -> example on filing the whole left screen to an extent
# button.pack(side="left", fill='both', expand=True) -> bigger
# button.grid(row=0,column=0)
button.place(relx=.7,relheight=1,relwidth=0.3)


# User Typing Enabled
entry = Entry(frame, font=40)
entry.place(relwidth=.65,relheight=1)


lower_frame = Frame(root,bg='#99b3ff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75,relheight=.6,anchor='n')

# Just a Label
label = Label(lower_frame, text='Hello this is a label', bg='yellow')
label.place(relx=0.3,rely=0, relwidth=0.45,relheight=.25)


root.mainloop()