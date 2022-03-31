exitProgram = False
firstRun = True

modeHelpList = {
    "exit": "Exit | Exits current program | Syntax: exit",
    "help": "Help | Prints all legal commands | -v advanced help | Syntax: help",
    "settings": "Settings | Enters settings | Syntax: settings",
}

helpFlags = {
    "-v": " \n\n\n\n From the settings menu that you are currently in, you can change variables in userconfig file located in current menu by <variable>=<value>",
    "-b": "heisnan",
}

def menu():
    global firstRun
    while True:
        if exitProgram:
            break
        elif firstRun:
            printModes()
            firstRun = False
        print(">> ", end="")
        mode = input() 
        checkModes(mode)

def checkModes(mode):
    try:
        modeList = mode.split(" ")
        if modeList[0] == "exit":
            exit()
        elif modeList[0] == "help":
            if len(modeList) == 1:
                printModes()
            else:
                for i in range(len(modeList)):
                    for key in helpFlags:
                        if modeList[i] == key:
                            print(helpFlags.get(key))
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
    print("\n<=========================|SETTINGS|=========================>")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeHelpList.get(key)))