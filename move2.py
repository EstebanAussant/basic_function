
import tkinter as tk

# Dictionnaire pour suivre les touches enfoncées
keys_pressed = {}

def move(event):
    key = event.keysym
    keys_pressed[key] = True

def release(event):
    key = event.keysym
    keys_pressed[key] = False

def update_movement():
    if keys_pressed.get("Up"):
        canvas.move(rectangle, 0, -5)
    if keys_pressed.get("Down"):
        canvas.move(rectangle, 0, 5)
    if keys_pressed.get("Left"):
        canvas.move(rectangle, -5, 0)
    if keys_pressed.get("Right"):
        canvas.move(rectangle, 5, 0)
    root.after(10, update_movement)  # Appel récursif pour mettre à jour le déplacement

root = tk.Tk()
root.title("Déplacer le rectangle avec les touches fléchées")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Créer un rectangle initial
rectangle = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Lier les événements clavier à la fonction move et release
root.bind("<KeyPress>", move)
root.bind("<KeyRelease>", release)

update_movement()  # Démarrer la mise à jour du déplacement

root.mainloop()