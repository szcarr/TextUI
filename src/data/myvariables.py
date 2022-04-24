import platform
import os

import debug
import fileHandling as fh

currentOS = platform.system()
split_by = fh.detectOS()

project_folder_name = "TextUI" #Name must be indentical to project folder name

name_of_userconfig = "userconfig.txt"
previous_login = "previous_login.txt"
countdown_txt = "countdown.txt"

source_folder = "src"
name_of_folder_to_programs = "data"
config_folder_name = "cfg"
user_folder_name = "user"
state_folder_name = "state"

windows_start_script = "TextUIstart.bat"
linux_start_script = "TextUIstart.sh"

def setup():
    setProjectFolderLocation()

def setProjectFolderLocation():
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " for project_folder_location.")

    global project_folder_location

    lst = fh.getPathToCurrentDir(project_folder_name).split(fh.detectOS())
    lastIndex = -1
    for i in range(len(lst)):
        if lst[i] == project_folder_name:
            lastIndex = i

    if lastIndex == -1:
        print(lst)
        print("Error did not find project_folder_name. In file " + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
        raise ValueError

    projectlocation = ""
    for i in range(lastIndex + 1):
        projectlocation = projectlocation + lst[i] + fh.detectOS()
    
    project_folder_location = projectlocation
    debug.conditionalPrint(debug.configPrint, "projectFolderLocation set to: " + projectlocation)
    return projectlocation

def setUserConfigLocation():
    debug.conditionalPrint(debug.systemPrint, debug.settingVariables + " for userConfigLocation.")

    global userconfig_location
    userconfig = ""

    if currentOS == "Windows":
        #print("heisannnnnn")
        userconfig = os.popen("where /r " + project_folder_location + " userconfig.*").read().split("\n")[0]
        userconfig_location = userconfig if project_folder_location != None else -1
    elif currentOS == "Linux":
        userconfig = str(os.popen("find " + project_folder_location + " -name userconfig.txt").read()).split("\n")[0].replace("." + split_by, "") #str(os.popen("find -name userconfig.txt").read()).split("\n")[0].replace("." + fh.detectOS(), "")
        userconfig_location = userconfig if project_folder_location != None else -1
    
    if userconfig_location == -1:
        print("Error did not find userconfig_location. In file" + str(os.path.basename(__file__)).split(fh.detectOS())[-1])
        raise ValueError

    debug.conditionalPrint(debug.configPrint, "userConfigLocation set to: " + userconfig_location)

    return userconfig

def get_current_version_and_date():

    '''
    Returns version number and date
    '''

    history_file = f"{project_folder_location}{'history.txt'}"
    #print(history_file)
    if fh.checkIfFileExist(history_file):
        output = fh.readTXTFile(history_file)
        for e in output:
            if "============" in e:
                lst = e.split(" | ")
                version_number = lst[0].split("< ")[1]
                version_date = lst[1].split(" >")[0]
                return (version_number, version_date)

def get_system_user():
    user = None
    if currentOS == "Windows":
        user = str(os.popen("whoami").read()).split(split_by)[1].split("\n")[0]
    elif currentOS == "Linux":
        user = str(os.popen("whoami").read()).split("\n")[0]
    else:
        print("COULD NOT FIND SYSTEM USER")
    return user


setup()

cfg_folder = str(project_folder_location + source_folder + split_by + config_folder_name + split_by)
usr_folder = str(cfg_folder + user_folder_name + split_by)
state_folder = str(cfg_folder + state_folder_name + split_by)

project_folder_location = setProjectFolderLocation()
userconfig_location = setUserConfigLocation()

version_number, version_date = get_current_version_and_date()

home_directory = str(os.popen("echo ~").read()).split("\n")[0] + split_by

system_user = get_system_user()