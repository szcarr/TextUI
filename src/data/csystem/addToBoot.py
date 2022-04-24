import os
import platform
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..')) # <- Adds parent folders modules to PATH

import fileHandling as fh
import config
import debug
import myvariables as mv

currentOS = platform.system()

if currentOS == "Windows":
    windows_user = str(os.popen("whoami").read()).split("\\")[1].split("\n")[0]
    windows_primary_startup_location = "C:\\Users\\" + windows_user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

def add_to_boot():
    if currentOS == "Windows":
        if fh.checkIfFileExist(windows_primary_startup_location): # <- Default path for startup
            debug.conditionalPrint(debug.systemPrint, "Found default directory for startup:")
            debug.conditionalPrint(debug.systemPrint, windows_primary_startup_location)
            windows_textui_start = config.mv.project_folder_location + mv.windows_start_script
            #print(windows_textui_start, windows_primary_startup_location)
            os.system('copy ' + windows_textui_start + ' "' + windows_primary_startup_location + '"')

        #hei = os.popen("where /r C:\Users\" + user + " *AppData*").read()
        #print(hei)
    elif currentOS == "Linux":
        # https://unix.stackexchange.com/questions/586894/is-there-a-way-to-make-linux-open-a-browser-window-at-login
        dirs_to_checkfor = [
            mv.home_directory + ".config/",
            mv.home_directory + ".config/autostart/",
        ]
        
        for e in dirs_to_checkfor:
            if not fh.checkIfFileExist(e):
                os.mkdir(e)

        autostart_file = mv.home_directory + ".config/autostart/" + mv.project_folder_name + ".desktop"
        os.system("rm -rf " + autostart_file)
        if not fh.checkIfFileExist(autostart_file):
            fh.createFileInSpecifiedDir(autostart_file)
            debug.conditionalPrint(debug.systemPrint, f"Adding startup file -> {autostart_file}")
            script_location = mv.project_folder_location + mv.linux_start_script
            toAdd = [
                    "[Desktop Entry]",
                    "Type=Application",
                    "Exec=gnome-terminal --command " + script_location,
                    "Hidden=false",
                    "NoDisplay=false",
                    "X-GNOME-Autostart-enabled=true",
                    "Name[en_NG]=Terminal",
                    "Name=Terminal",
                    "Comment[en_NG]=Start Terminal On Startup",
                    "Comment=Start Terminal On Startup",
                ]

            for e in toAdd:
                fh.addTextToSpecifiedFile(autostart_file, e + "\n")

def remove_from_boot():
    if currentOS == "Windows":
        windows_start_file_location = windows_primary_startup_location + mv.split_by + mv.windows_start_script
        if fh.checkIfFileExist(windows_start_file_location):
            fh.removeFile(windows_start_file_location)
    elif currentOS == "Linux":
        autostart_file = mv.home_directory + ".config/autostart/" + mv.project_folder_name + ".desktop"
        if fh.checkIfFileExist(autostart_file):
            os.system("rm -rf " + autostart_file)
# C:\Users\itwan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup