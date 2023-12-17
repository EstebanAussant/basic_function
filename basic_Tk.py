from tkinter import Tk, Canvas, Button

#create window
mw = Tk()
mw.geometry('1000x600')

#create canevas
canevas = Canvas(mw, width = 800, height = 400, bg = 'blue')
canevas.pack(padx=10, pady=10)

#create button
button_quit = Button(mw, text = 'quit', command = mw.destroy)
button_quit.pack()


mw.mainloop()

