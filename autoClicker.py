import pygetwindow as gw
import time
import pyautogui

def get_window_by_title(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]
    return None

window_title = 'Roblox'
target_window = get_window_by_title(window_title)

if target_window:
    target_window.activate()

    while True:
        pyautogui.click()
        
        time.sleep(0.05)

else:
    print(f"Window with title '{window_title}' not found.")