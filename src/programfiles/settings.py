import traceback

import time_related.countdown.countdown as countdown
import config
import debug
import fileHandling as fh
import myvariables as mv
import stringFormatting as sf
exitProgram = False
firstRun = True

helpFlags = {
    "-v": '''
From the settings menu that you are currently in, you can change variables in userconfig file located in current menu by typing: <variable> = <value>
User must use 'Exit' command to save changes to variables.
Remember when referencing a variable to include the spaces between "=" so its " = "
Else, variable will not get proper value

User can cancel changes by raising a KeyboardInterrupt with "CTRL+C"

User can also reference a variable by its name to get a description of what the specified variable does.
''',
}

modeHelpList = {
    "exit": "Exit | Exits current program | Syntax: exit",
    "help": "Help | Prints all legal commands | -v verbose | Syntax: help",
    "countdown": "countdown | User has to specify one flag and one flag only | -v verbose -a add -r remove -l list | Syntax: countdown -a <name_of_countdown> <YYYY-MM-DD HH:MM:SS>",
    "lsvar": "List variables | Lists all variables user can access | Syntax: lsvar", 
    "rconf": "Reset configs | Resets all configs | Syntax: rconf",
    "settings": "Settings | Enters settings | Syntax: settings",
}

userconfigvariables = {} #Values are dynamically added
userconfigdescription = {} #Values are dynamically added

def addChanges():
    index = -1
    for k in userconfigvariables:
        index += 1
        if "[" and "]" in k:
            #print("Found '[' and ']' in " + k)
            index = userconfigvariables.get(k)
            continue
        toAdd = k + " = " + userconfigvariables.get(k) + "; // " + userconfigdescription.get(k)
        fh.replaceLineInFile(mv.userconfig_location, index, toAdd)

def menu(): # Main function
    setup()
    global firstRun, exitProgram
    exitProgram = False
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
        #print(modeList)
        if modeList[0] == "exit":
            addChanges()
            exit()

        elif modeList[0] == "help":
            if len(modeList) == 1:
                printModes()
            else:
                for i in range(len(modeList)):
                    for key in helpFlags:
                        if modeList[i] == key:
                            print(helpFlags.get(key))

        elif modeList[0] == "countdown":
            if modeList[1] == "-v" and len(modeList) == 2:
                print(countdown.countdown_description)
            elif modeList[1] == "-l" and len(modeList) == 2:
                countdown.print_countdown_txt()
            elif modeList[1] == "-a" and len(modeList) == 5:
                name_of_countdown = modeList[2]
                countdown_date = f"{modeList[3]} {modeList[4]}"
                countdown.add_countdown(name_of_countdown, countdown_date)
            elif modeList[1] == "-r" and len(modeList) == 3:
                countdown.remove_countdown(int(modeList[2]))

        elif modeList[0] == "rconf":
            config.resetConfigs()
            setup()
            debug.conditionalPrint(debug.systemPrint, f"System successfully deleted {mv.config_folder_name} folder.")

        elif modeList[0] == "lsvar":
            for k in userconfigvariables:
                toPrint = str(k + " = " + str(userconfigvariables.get(k)) + ";")
                if "[" and "]" in k:
                    toPrint = k
                print(toPrint)
                
        else:
            if len(modeList) > 1: # User is assigning values to variables
                for k in userconfigvariables:
                    if modeList[0] == k:
                        print(k + " is now set to: " + modeList[2])
                        userconfigvariables[k] = modeList[2]
            else: # User wants a description of variable
                for k in userconfigdescription:
                    if modeList[0] == k:
                        print(userconfigdescription.get(modeList[0]))
    except IndexError as i:
        print(traceback.format_exc())

def exit():
    global exitProgram
    exitProgram = True
    print("Exiting...")

def printModes():
    keysForModeList = list(modeHelpList.keys())
    counter = 0
    title = sf.title("SETTINGS")
    print(f"\n{title}")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeHelpList.get(key)))
    print("")

def setup():
    setup_userconfig()
    setupUserConfigDecription()

def setup_userconfig():
    global userconfigvariables
    userconfigvariables.clear()
    #configFile = mv.userconfig_location if mv.userconfig_location != -1 and mv.userconfig_location != None else debug.conditionalPrint(debug.settingsPrint, "Error getting userconfiglocation.")    
    output = fh.readTXTFile(mv.userconfig_location)
    startAdding = False
    for index, line in enumerate(output):
        category = False
        if line == "\n":
            debug.conditionalPrint(debug.settingsPrint, "Skipping '" + line.split("\n")[0] + "' at index: " + str(index))
            continue
        elif "[" and "]" in line:
            startAdding = True
            category = True
        if category:
            userconfigvariables[line.split("\n")[0]] = index
        elif startAdding:
            keyandvalue = line.split("\n")[0].split(";")[0].split(" = ") # Index 0 is key, index 1 should be value
            key = keyandvalue[0]
            value = keyandvalue[1]
            userconfigvariables[key] = value
    debug.conditionalPrint(debug.settingsPrint, userconfigvariables)

def setupUserConfigDecription():
    global userconfigdescription
    userconfigdescription.clear()
    output = fh.readTXTFile(mv.userconfig_location)
    startAdding = False
    for index, line in enumerate(output):
        if line == "\n" or "[" and "]" in line:
            debug.conditionalPrint(debug.settingsPrint, "Skipping '" + line.split("\n")[0] + "' at index: " + str(index))
            startAdding = True
            continue
        if startAdding:
            holder = line.split("\n")[0].split(";")
            key = holder[0].split(" = ")[0]
            value = ""
            try:
                value = holder[1].split(" // ")[1]
            except IndexError as i: # There was no comment to variable
                pass
            userconfigdescription[key] = value
    debug.conditionalPrint(debug.settingsPrint, userconfigdescription)