import pygetwindow as gw
import random
from pynput.keyboard import Controller as KeyboardController
import time
import pydirectinput

def get_window_by_title(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]
    return None

window_title = 'Roblox'
target_window = get_window_by_title(window_title)

if target_window:
    target_window.activate()
    
    keyboard = KeyboardController()

    while True:
        time.sleep(1)
        keys_to_press = ['w', 'a', 's', 'd']
        duration = random.uniform(0.5, 1.3)
        key = random.choice(keys_to_press)
        keyboard.press(key)
        time.sleep(duration)
        keyboard.press(key)

else:
    print(f"Window with title '{window_title}' not found.")