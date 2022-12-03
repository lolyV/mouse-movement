from pynput.mouse import Listener

def on_move(x, y):
    print("Mouse Moved!")

def on_click(x, y, button, pressed):
    print("Button Pressed")

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

#You can also import time and then add time.sleep(2) below the print("")
#same with on_click ^^^^
