import pygetwindow as gw
from pynput.keyboard import Key, Controller as KeyboardController
import time
import pyautogui
import matplotlib.pyplot as plt
import pydirectinput
from PIL import Image, ImageGrab
import pytesseract
import easyocr
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#cut for now
# def get_window_by_title(title):
#     windows = gw.getWindowsWithTitle(title)
#     if windows:
#         return windows[0]
#     return None


def get_pixel_color(x, y):
    try:
        # Get the screen color at the specified pixel coordinate
        pixel_color = pyautogui.pixel(x, y)
        return tuple(pixel_color)
    except pyautogui.FailSafeException:
        print("Error: The specified pixel coordinate is out of screen bounds.")
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
        
def getPokemonName():
    pokemonNameRegion = (2249, 151, 300, 20)
    x, y, width, height = pokemonNameRegion
    nameScreenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height),include_layered_windows=False, all_screens=True)
    tesseractResult = pytesseract.image_to_string(nameScreenshot, config='--psm 7')
    #remove level from string
    if 'Lv.' in tesseractResult:
        tesseractResult = tesseractResult.split('Lv')[0]
    print(tesseractResult)
    return tesseractResult

def isShiny(pokemonString):
    return 'shiny' in pokemonString.lower()

#keyboard functions
def battleInitializer():
    time.sleep(5)
    keyboard.press(Key.left)
    time.sleep(0.5)
    keyboard.release(Key.left)
    
    time.sleep(0.25)
    
    keyboard.press(Key.up)
    time.sleep(0.5)
    keyboard.release(Key.up)
    
    time.sleep(0.25)
    
    keyboard.press('z')
    time.sleep(0.25)
    keyboard.release('z')
    
    time.sleep(0.25)

def topRightMoveSelect():
    keyboard.press(Key.up)
    time.sleep(0.5)
    keyboard.release(Key.up)
    
    time.sleep(0.25)
    
    keyboard.press(Key.right)
    time.sleep(0.5)
    keyboard.release(Key.right)
                
    time.sleep(0.25)
                
    keyboard.press('z')
    time.sleep(0.25)
    keyboard.release('z')

def topLeftMoveSelect():
    keyboard.press(Key.up)
    time.sleep(0.5)
    keyboard.release(Key.up)
    
    time.sleep(0.25)
    
    keyboard.press(Key.left)
    time.sleep(0.5)
    keyboard.release(Key.left)
    
    time.sleep(0.25)

    keyboard.press('z')
    time.sleep(0.25)
    keyboard.release('z')

def runUpDown():
    keyboard.press(Key.up)
    time.sleep(0.75)
    keyboard.release(Key.up)
    
    time.sleep(0.1)
    
    keyboard.press(Key.down)
    time.sleep(0.75)
    keyboard.release(Key.down)
    
    time.sleep(0.1)

def directionStep(direction, repeats=1):
    # Mapping directions to Key attributes
    direction_map = {
        'left': Key.left,
        'right': Key.right,
        'up': Key.up,
        'down': Key.down
    }
    
    if direction in direction_map:
        key_to_press = direction_map[direction]
        
        for _ in range(repeats):
            keyboard.press(key_to_press)
            time.sleep(0.1)
            keyboard.release(key_to_press)
            time.sleep(0.1)
    else:
        print(f"Invalid direction: {direction}")

#MAIN LOOP
window_title = 'PokeMMO'
#target_window = get_window_by_title(window_title)

#if target_window:
#target_window.activate()

keyboard = KeyboardController()

#print(get_pixel_color(2219, 185))

time.sleep(2)

while True:
    directionStep('left')
    directionStep('right')
    #battle check
    battleStartCheck = get_pixel_color(2219, 185) 
    print(get_pixel_color(2219, 185))
    if battleStartCheck == (48, 48, 48) or battleStartCheck == (47, 47, 47):
        #shiny check
        isShinyPokemon = isShiny(getPokemonName())
        if isShinyPokemon:
            print('Shiny!')
            while True:
                directionStep('up')
                time.sleep(0.5)
                directionStep('down')
        else:
            print('Not shiny!')

        #battle sequence
        moveCounter = 25
        while True:
            battleInitializer()
            #first move
            if moveCounter <= 25:
                topRightMoveSelect()
            #second move
            elif moveCounter <= 60:
                topLeftMoveSelect()
            
            #wait for move animations to end
            time.sleep(6)
            moveCounter = moveCounter + 1
            
            if moveCounter >= 25:
                moveCounter +=1
            
            battleEndCheck = get_pixel_color(2219, 185)
            if battleEndCheck != (48, 48, 48):
                break