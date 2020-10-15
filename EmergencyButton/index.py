import ctypes, keyboard, time
MessageBox = ctypes.windll.user32.MessageBoxW

def warn():
    keyboard.send("alt+f4")

hotkey = keyboard.add_hotkey("ctrl+alt+p", warn)
MessageBox(None, "Hotkey: Ctrl+Alt+P\nPress it whenever you got urge", "Information", 0 | 0x00000040)

while (lambda: time.sleep(1) == None)():
    ...
