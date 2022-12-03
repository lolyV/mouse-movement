from pynput.mouse import Listener

def on_move(x, y):
    print("Mouse Moved!")

with Listener(on_move=on_move) as listener:
    listener.join()

#You can also import time and then add time.sleep(2) below the print("")
