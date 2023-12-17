import tkinter as tk

def move(event):
    key = event.keysym
    if key == "Up":
        canvas.move(rectangle, 0, -5)
    elif key == "Down":
        canvas.move(rectangle, 0, 5)
    elif key == "Left":
        canvas.move(rectangle, -5, 0)
    elif key == "Right":
        canvas.move(rectangle, 5, 0)

root = tk.Tk()
root.title("Déplacer le rectangle avec les touches fléchées")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Créer un rectangle initial
rectangle = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Lier les événements clavier à la fonction move
root.bind("<KeyPress>", move)

root.mainloop()