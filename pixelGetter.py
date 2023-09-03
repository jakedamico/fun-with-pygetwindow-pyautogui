import pygetwindow as gw
import pyautogui

def get_window_by_title(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]
    return None

def get_mouse_position():
    return pyautogui.position()

# Replace 'Window Title' with the title of the window you want to select
window_title = 'PokeMMO'

#target_window = get_window_by_title(window_title)

#if target_window:
    # Activate the target window
    #target_window.activate()

print("Move the mouse to the desired point within the window...")
print("Press Ctrl+C to stop.")

try:
    while True:
        # Get the current mouse position
        x, y = get_mouse_position()
        print(f"Mouse position: ({x}, {y})", end='\r')
except KeyboardInterrupt:
    print("\nStopped.")

else:
    print(f"Window with title '{window_title}' not found.")