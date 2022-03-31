import os
import platform

import fileHandling as fh
import debug
import myvariables as mv

projectFolderLocation = None
userConfigLocation = None

projectFolderName = "TextUI" #Name must be indentical to project folder name
nameOfUserConfig = "userconfig.txt"

currentOS = platform.system()
versionNumber = "0.1"

def addStartScripts():
    locationAndNameOfWindowsStartScript = projectFolderLocation + fh.detectOS() + "TextUIstart.bat"
    if not fh.checkIfFileExist(locationAndNameOfWindowsStartScript):
        fh.createFileInSpecifiedDir(locationAndNameOfWindowsStartScript)
        toAdd = str("python3 " + projectFolderLocation + "\\" + mv.sourceFolder + "\\" + mv.nameOfFolderToPrograms + "\\TextUI.py")
        fh.addTextToSpecifiedFile(locationAndNameOfWindowsStartScript, toAdd)

def addVariablesToUserConfig():
    debug.conditionalPrint(debug.configPrint, "Checking contents of: " + userConfigLocation)

    fileSize = 0
    loc = projectFolderLocation + fh.detectOS() + "src" + fh.detectOS() + "cfg" + fh.detectOS() + "user" + fh.detectOS()

    if currentOS == "Windows":
        loc = projectFolderLocation + fh.detectOS() + "src" + fh.detectOS() + "cfg" + fh.detectOS() + "user" + fh.detectOS()
        splitlist = os.popen("dir " + loc).read().split("\n")
        for i in range(len(splitlist)):
            if "userconfig.txt" in splitlist[i]:
                temp = splitlist[i].split(" ")
                for i in range(len(temp)):
                    if temp[i] == "userconfig.txt":
                        fileSize = int(temp[i - 1])
    elif currentOS == "Linux":
        fileSize = int(str(os.popen("ls -l " + loc + "| tail -1").read()).split(" ")[4])

    if fh.checkIfFileExist(userConfigLocation) and fileSize < 1:
        debug.conditionalPrint(debug.configPrint, "Adding values to: " + userConfigLocation)
        toAdd = [
            "TextUI by szcarr. https://github.com/szcarr/TextUI",
            "Version: " + versionNumber,
            "",
            "[SYSTEM]",
            "addToBoot = False",
        ]

        for i in range(len(toAdd)):
            fh.addTextToSpecifiedFile(userConfigLocation, toAdd[i] + "\n")

def checkForConfigFiles():
    cfgfolder = str(projectFolderLocation + "src" + fh.detectOS()) + "cfg" + fh.detectOS()
    userfolder = cfgfolder + "user" + fh.detectOS()
    userconfig = cfgfolder + "user" + fh.detectOS() + nameOfUserConfig

    args = [
        cfgfolder, #cfg
        userfolder,
    ]

    for i in range(len(args)):
        if not os.path.exists(args[i]):
            debug.conditionalPrint(debug.configPrint, "File/Folder " + str(args[i]) + " did not exist. Creating directory now.")
            fh.makeDirectory(args[i])
    if not fh.checkIfFileExist(userconfig):
        debug.conditionalPrint(debug.configPrint, "File/Folder " + str(args[i]) + " did not exist. Creating userconfig.txt.")
        fh.createFileInSpecifiedDir(userconfig)

def setProjectFolderLocation():
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " for projectFolderLocation.")

    global projectFolderLocation
    lst = fh.getPathToCurrentDir(projectFolderName).split(fh.detectOS())
    lastIndex = -1
    for i in range(len(lst)):
        if lst[i] == projectFolderName:
            lastIndex = i

    if lastIndex == -1:
        print("Error did not find projectFolderName. In file" + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
        raise ValueError

    projectlocation = ""
    for i in range(lastIndex + 1):
        projectlocation = projectlocation + lst[i] + fh.detectOS()
    
    projectFolderLocation = projectlocation
    debug.conditionalPrint(debug.configPrint, "projectFolderLocation set to: " + projectlocation)

def setUserConfigLocation():
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " for userConfigLocation.")

    global userConfigLocation

    userconfig = ""
    if currentOS == "Windows":
        userconfig = os.popen("where /r " + projectFolderLocation + " userconfig.*").read().split("\n")[0]
        userConfigLocation = userconfig if projectFolderLocation != None else -1
    elif currentOS == "Linux":
        userconfig = str(os.popen("find -name userconfig.txt").read()).split("\n")[0].replace("." + fh.detectOS(), "")
        userConfigLocation = projectFolderLocation + userconfig if projectFolderLocation != None else -1
    
    if userConfigLocation == -1:
        print("Error did not find userConfigLocation. In file" + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
        raise ValueError
    debug.conditionalPrint(debug.configPrint, "userConfigLocation set to: " + userConfigLocation)

def setup():
    debug.conditionalPrint(debug.systemPrint, "Operating system: " + str(currentOS))
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " in file: " + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
    setProjectFolderLocation()
    checkForConfigFiles()
    setUserConfigLocation()
    addVariablesToUserConfig()
    addStartScripts()

#setup() #remove later