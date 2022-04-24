import os
import traceback

import settings
import config
import debug
import fileHandling as fh
import misc.chancegame as chance
import csystem.update as update
import myvariables as mv
import standby
import csystem.login as login
#This file is main

debug.conditionalPrint(debug.verbose, debug.settingVariables + " in " + str(os.path.basename(__file__)).split(fh.detectOS())[-1]) # <- get filename of current file

exit_program = False
first_run = True

modeHelpList = {
    "exit": "Exit | Exits current program | Syntax: exit",
    "help": "Help | Prints all legal commands | Syntax: help",
    "chance": "Chance | Plays a game of chance | (-b For Magic 8 Ball) (-c For coin flip) | Syntax: chance <FLAG>",
    "schedule": "Schedule | Prints all schedule sub commands | Syntax: schedule",
    "settings": "Settings | Enters settings | User can add and remove countdowns here | Syntax: settings",
    "standby": "Standby | Enters standby mode. Automatically prints important data | Syntax: standby",
    "update": "Update | Updates and applies user configs | (-y For yes) | Syntax: update",
}

mv.setup()
config.setup()

login.main()

def menu():
    global first_run
    while True:
        if exit_program:
            break
        elif first_run:
            print_modes()
            first_run = False
        print("> ", end="")
        mode = input() 
        check_modes(mode)

def check_modes(mode):
    try:
        mode = mode.split(" ")
        if mode[0] == "exit":
            exit()
        elif mode[0] == "help":
            print_modes()
        elif mode[0] == "chance":
            if mode[1] == "-b":
                chance.eightball()
            elif mode[1] == "-c":
                chance.coinflip()
        elif mode[0] == "schedule":
            pass
        elif mode[0] == "settings":
            settings.menu()
        elif mode[0] == "standby":
            standby.main()
        elif mode[0] == "update":
            if len(mode) == 2:
                if mode[1] == "-y":
                    update.update()
            else:
                response = input("System wants to update and apply settings. Y/n? > ")
                if response == "" or response == "Y" or response == "y":
                    update.update()

    except IndexError as i:
        print(traceback.format_exc())  

def exit():
    global exit_program
    exit_program = True
    print("Goodbye!")

def print_modes():
    keysForModeList = list(modeHelpList.keys())
    counter = 0
    print("\n<=========================|TEXTUI|=========================>")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeHelpList.get(key)))
    print("")

menu()