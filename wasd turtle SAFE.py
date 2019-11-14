import turtle
from pynput import keyboard
turtle.colormode(255)
turtle.speed("fastest")
def on_press(key):
    try:
        if key.char == ("w"):
            turtle.forward(10)
        if key.char == ("a"):
            turtle.left(30)
        if key.char == ("s"):
            turtle.backward(10)
        if key.char == ("d"):
            turtle.right(30)
        else:
            pass
    except:
        pass
listener = keyboard.Listener(
    on_press=on_press)
listener.start()
turtle.getscreen()._root.mainloop()
