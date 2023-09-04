import pokeXP
import time
from pynput.keyboard import Controller as KeyboardController

def runFromBattle():
    pokeXP.directionStep('right', 4)
    time.sleep(0.5)
    keyboard.press('z')
    time.sleep(0.25)
    keyboard.release('z')

keyboard = KeyboardController()

#print(get_pixel_color(2219, 185))

time.sleep(2)

while True:
    pokeXP.directionStep('left')
    pokeXP.directionStep('right')
    #battle check
    battleStartCheck = pokeXP.get_pixel_color(2219, 185)
    hordeBattleStartCheck = pokeXP.get_pixel_color(2880, 137) 
    print(pokeXP.get_pixel_color(2219, 185))
    if battleStartCheck == (48, 48, 48) or battleStartCheck == (47, 47, 47) or hordeBattleStartCheck == (48, 48, 48) or hordeBattleStartCheck == (47, 47, 47):
        #shiny check
        isShinyPokemon = pokeXP.isShiny(pokeXP.getPokemonName())
        if isShinyPokemon:
            print('Shiny!')
            while True:
                pokeXP.directionStep('up')
                pokeXP.time.sleep(0.5)
                pokeXP.directionStep('down')
        else:
            print('Not shiny!')
            time.sleep(10)
            runFromBattle()
            #wait to spawn into world
            time.sleep(6)