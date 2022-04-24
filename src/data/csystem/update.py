import os
import platform
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..')) # <- Adds parent folders modules to PATH

import fileHandling as fh
import config
import debug
import myvariables as mv
from . import addToBoot

def update():
    output = read_userconfigs()

    current_branch_selected = None

    for e in output:
        current_variable_selected = None
        if "[" and "]" in e:
            current_branch_selected = e    
            #print(f"Branch selected: {current_branch_selected}")
        elif current_branch_selected and " = " in e:
            current_variable_selected = e.split(";")[0]
        if current_variable_selected != None:
            select_mode(current_branch_selected, current_variable_selected)
    print(f"System successfully updated.")

def read_userconfigs():
    lst_output = fh.readTXTFile(mv.userconfig_location)
    filtered_output = []
    for e in lst_output:
        filtered_output.append(e.split("\n")[0])
    return filtered_output

def select_mode(branch, userconfig_line): # Add functionality here
    line = userconfig_line.split(" = ")
    if branch == "[SYSTEM]":
        if line[0] == "addToBoot" and line[1] == "True":
            addToBoot.add_to_boot()
        elif line[0] == "addToBoot" and line[1] == "False":
            addToBoot.remove_from_boot()
    elif branch == "[MISC]":
        if line[0] == "loginMessage" and line[1] == "True":
            print(f"System will now prompt user with a login message, when logging in.")

def cache_userconfig():
    fh.createFileInSpecifiedDir(config.userConfigLocation)