from tkinter import Tk, Canvas, Button, Label, StringVar

#create window
mw = Tk()
mw.geometry('1000x600')
mw.title('Space Invader')

#create canevas
canevas = Canvas(mw, width = 800, height = 400, bg = 'blue')
canevas.pack(padx=10, pady=10)

#create button
button_quit = Button(mw, text = 'quit', command = mw.destroy)
button_quit.pack()

#text
label_text = Label(mw, text = 'Hello world!', fg = 'blue')
label_text.pack(padx = 5, pady = 5)

#text variable
Text_life = StringVar()
Text_life.set('Hello world')
label_life = Label(mw, textvariable = Text_life, fg = 'red')
label_life.pack(padx = 5, pady = 5)

#create rectangle with spawn and delete
def spawn():
    global grey_rectangle
    grey_rectangle  = canevas.create_rectangle(700 + 10, 200 +10 , 700 - 10 , 200 - 10, outline='black', fill = 'grey')

def destroy_grey():
    canevas.delete(grey_rectangle)

button_spawn = Button(mw, text = 'spawn', command = spawn)
button_spawn.pack()

button_destroy = Button(mw, text = 'destroy', command = destroy_grey)
button_destroy.pack()



mw.mainloop()

