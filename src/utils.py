import subprocess
import keyboard
import mouse
import os
from Xlib import X, display, Xutil

d = display.Display()
root = d.screen().root
class Key:
    def __init__(self, key):
        self.key = key

    def addHotkey(keys, script):
        keyboard.add_hotkey(keys, script)

    def write(message):
        keys = list(message)
        for key in keys:
            if key == " ":
                keys[keys.index(key)] = "space"
        #print(keys)
        newmessage = " ".join(keys)
        #print(message)
        result = subprocess.run(["xdotool", "getactivewindow"], capture_output=True, text=True)
        window_id = result.stdout.strip()
        if window_id != None:
            os.system(f"xdotool key --clearmodifiers --window {window_id} {newmessage}")

    def release(key):
        keyboard.release(key)