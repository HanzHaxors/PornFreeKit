
# Blocked
blacklisted = [
    "porn",
    "hentai",
    "masturbation"
]

whitelisted = [
    "pornfree",
    "overcoming porn addiction",
    "pornfreekit",
    "stay clean",
    "get out of that"
]

msgs = [
    "STOP BRUH",
    "Hey, have you pray to your god today?"
]

# Sorry i skidded

import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

def getTitles():
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return titles

# Sorry i skidded

from time import sleep
from threading import Thread
from random import choice

MessageBox = ctypes.windll.user32.MessageBoxW
# WARNING: ctypes.windll is only for WINDOWS

def wait(s=2):
    sleep(s)
    return True

while wait():
    titles = getTitles()

    titles = [title for title in titles if not any(allowed in title.lower() for allowed in whitelisted)]

    # list(''.join([f if 'a' in f or 'b' in f else '' for f in l]))
    if any(blocked in title.lower() for title in titles for blocked in blacklisted):
        print("Ban")

        kwargs = {
            "target": MessageBox,
            "args": (None,
                    choice(msgs) + "\n\nForce your computer to shut down.",
                    "GET OUT OF THAT",
                    0),
            "daemon": True
        }
        Thread(**kwargs).start()
    print(titles)
