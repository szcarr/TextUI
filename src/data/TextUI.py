import os

import schedule
import settings
import config
import debug
import fileHandling as fh

#This file is main

debug.conditionalPrint(debug.verbose, debug.settingVariables + " in " + str(os.path.basename(__file__)).split(fh.detectOS())[-1]) # <- get filename of current file

exitProgram = False
firstRun = True

modeHelpList = {
    "exit": "Exit | Exits current program | Syntax: exit",
    "help": "Help | Prints all legal commands | Syntax: help",
    "schedule": "Schedule | Prints all schedule sub commands | Syntax: schedule",
    "settings": "Settings | Enters settings | Syntax: settings",
}

config.setup()

def menu():
    global firstRun
    while True:
        if exitProgram:
            break
        elif firstRun:
            printModes()
            firstRun = False
        print("> ", end="")
        mode = input() 
        checkModes(mode)

def checkModes(mode):
    try:
        modeList = mode.split(" ")
        if modeList[0] == "exit":
            exit()
        elif modeList[0] == "help":
            printModes()
        elif modeList[0] == "schedule":
            pass
        elif modeList[0] == "settings":
            settings.menu()
    
    except IndexError as i:
        print(i)
    except:
        print("Error in selecting mode")

def exit():
    global exitProgram
    exitProgram = True
    print("Exiting...")
    
def printModes():
    keysForModeList = list(modeHelpList.keys())
    counter = 0
    print("\n<=========================|TEXTUI|=========================>")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeHelpList.get(key)))

menu()