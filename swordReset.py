import pygetwindow as gw
from pynput.keyboard import Controller as KeyboardController
import time
import pyautogui
import matplotlib.pyplot as plt
import pydirectinput

def get_window_by_title(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]
    return None

#for testing
def visualize_color(rgb_color):
    if rgb_color is not None:
        r, g, b = rgb_color
        color = [r / 255.0, g / 255.0, b / 255.0]
        plt.imshow([[color]])
        plt.title(f"RGB Color: {rgb_color}")
        plt.axis("off")
        plt.show()

def get_pixel_color(x, y):
    try:
        # Get the screen color at the specified pixel coordinate
        pixel_color = pyautogui.pixel(x, y)
        return tuple(pixel_color)
    except pyautogui.FailSafeException:
        print("Error: The specified pixel coordinate is out of screen bounds.")
        return None

window_title = 'Roblox'
target_window = get_window_by_title(window_title)

if target_window:
    target_window.activate()
    
    keyboard = KeyboardController()
    
    print(get_pixel_color(3689, 611))

    while True:
        time.sleep(10)
        if get_pixel_color(3689, 611) == (213, 46, 46):
            keyboard.press('s')
            time.sleep(1.2)
            keyboard.release('s')
            time.sleep(1)
            keyboard.press('d')
            time.sleep(5)
            keyboard.release('d')
            time.sleep(0.5)
            pydirectinput.moveTo(3689,611, duration=0.5)
            time.sleep(0.5)
            pydirectinput.click(3689,611)
            time.sleep(1)
            pydirectinput.moveTo(3086,631, duration=0.5)
            time.sleep(0.5)
            pydirectinput.click(3086,631)
            time.sleep(0.5)
else:
    print(f"Window with title '{window_title}' not found.")