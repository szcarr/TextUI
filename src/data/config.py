import os
import platform

import fileHandling as fh
import debug
import myvariables as mv

mv.project_folder_location = None
userConfigLocation = None

def addStartScripts():
    if mv.currentOS == "Windows":
        locationAndNameOfWindowsStartScript = mv.project_folder_location + fh.detectOS() + mv.windows_start_script
        if not fh.checkIfFileExist(locationAndNameOfWindowsStartScript):
            fh.createFileInSpecifiedDir(locationAndNameOfWindowsStartScript)

            toAdd = [
                #str("@echo off\n"),
                str("cd /d " + mv.project_folder_location + mv.source_folder + "\\" + mv.name_of_folder_to_programs + "\n"),
                str("set PYTHONPATH=%PYTHONPATH%;" + mv.project_folder_location + mv.source_folder + "\\" + mv.name_of_folder_to_programs),
                str("python3 TextUI.py\n"),
                str("pause"),
            ]

            for i in range(len(toAdd)):
                fh.addTextToSpecifiedFile(locationAndNameOfWindowsStartScript, toAdd[i])

    elif mv.currentOS == "Linux":
        locationAndNameOfLinuxStartScript = mv.project_folder_location + mv.linux_start_script
        if not fh.checkIfFileExist(locationAndNameOfLinuxStartScript):
            fh.createFileInSpecifiedDir(locationAndNameOfLinuxStartScript)
            os.system("chmod 755 " + locationAndNameOfLinuxStartScript)

            toAdd = [
                "#!/bin/bash\n",
                "\n",
                str("cd " + mv.project_folder_location + mv.source_folder + mv.split_by + mv.name_of_folder_to_programs + "\n"),
                str("export PYTHONPATH=$PYTHONPATH:`" + mv.project_folder_location + "'"),
                str("python3 TextUI.py\n"),
            ]

            for e in toAdd:
                fh.addTextToSpecifiedFile(locationAndNameOfLinuxStartScript, e)

def addVariablesToUserConfig():
    debug.conditionalPrint(debug.configPrint, "Checking contents of: " + mv.userconfig_location)

    fileSize = 0
    loc = mv.usr_folder

    if mv.currentOS == "Windows":
        loc = mv.project_folder_location + fh.detectOS() + "src" + fh.detectOS() + "cfg" + fh.detectOS() + "user" + fh.detectOS()
        splitlist = os.popen("dir " + loc).read().split("\n")
        for i in range(len(splitlist)):
            if "userconfig.txt" in splitlist[i]:
                temp = splitlist[i].split(" ")
                for i in range(len(temp)):
                    if temp[i] == mv.name_of_userconfig:
                        fileSize = int(temp[i - 1])
    elif mv.currentOS == "Linux":
        fileSize = int(str(os.popen("ls -l " + loc + "| tail -1").read()).split(" ")[4])

    if fh.checkIfFileExist(mv.userconfig_location) and fileSize < 1:
        debug.conditionalPrint(debug.configPrint, "Adding values to: " + mv.userconfig_location)
        toAdd = [
            "TextUI by szcarr. https://github.com/szcarr/TextUI",
            "Version: " + mv.version_number,
            "",
            "[MISC]",
            "loginMessage = True; // When user first enters TextUI, user is prompted with a login message.",
            "",
            "[SYSTEM]",
            "addToBoot = False; // Adds file to startup, meaning this program will start when computer boots.",
        ]

        for i in range(len(toAdd)):
            fh.addTextToSpecifiedFile(mv.userconfig_location, toAdd[i] + "\n")

def checkForConfigFiles():
    cfgfolder = mv.cfg_folder
    userfolder = cfgfolder + "user" + fh.detectOS()
    userconfig = cfgfolder + "user" + fh.detectOS() + mv.name_of_userconfig

    args = [
        cfgfolder,
        userfolder,
    ]

    for i in range(len(args)):
        if not os.path.exists(args[i]):
            debug.conditionalPrint(debug.configPrint, "File/Folder " + str(args[i]) + " did not exist. Creating directory now.")
            fh.makeDirectory(args[i])
    if not fh.checkIfFileExist(userconfig):
        debug.conditionalPrint(debug.configPrint, "File/Folder " + str(args[i]) + " did not exist. Creating userconfig.txt.")
        fh.createFileInSpecifiedDir(userconfig)

def resetConfigs():
    if mv.currentOS == "Linux":
        to_delete = str(mv.project_folder_location + mv.source_folder + mv.split_by + mv.config_folder_name)
        response = input("System wants to delete '" + to_delete + "'. Y/n?")
        if response == "" or "Y" or "y":
            os.system("rm -rf " + to_delete)
            print("System successfully deleted " + to_delete)
            setup()
    elif mv.currentOS == "Windows":
        to_delete = str(mv.project_folder_location + mv.source_folder + mv.split_by + mv.config_folder_name)
        print(to_delete)
        response = input("System wants to delete '" + to_delete + "'. Y/n?")
        if response == "" or "Y" or "y":
            os.system(f"rmdir {to_delete} /s /q")
            setup()
        #print("Not added deleting for windows check config.py -> resetConfigs()")

def state():
    if not fh.checkIfFileExist(mv.state_folder):
        os.mkdir(mv.state_folder)

def add_countdown_file():
    if not fh.checkIfFileExist(mv.usr_folder):
        file = mv.usr_folder + mv.countdown_txt
        fh.createFileInSpecifiedDir(file)

def setup():
    debug.conditionalPrint(debug.systemPrint, "Operating system: " + str(mv.currentOS))
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " in file: " + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
    checkForConfigFiles()
    addVariablesToUserConfig()
    addStartScripts()
    state()