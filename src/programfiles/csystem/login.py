import os
import platform
import sys
import datetime

sys.path.insert(1, os.path.join(sys.path[0], '..')) # <- Adds parent folders modules to PATH

import fileHandling as fh

import myvariables as mv
import time_related.timeHandling as th
import programfiles.csystem.prev_logins as prev
import programfiles.crypto.cryptoprices as crypto
import stringFormatting as sf

#print(mv.split_by, mv.project_folder_location)
statefile = mv.state_folder + mv.previous_login

def main():
    if is_login_message_enabled():
        print_login_message()
    if fh.checkIfFileExist(statefile):
        fh.removeFile(statefile)
    write_login_data()

def print_login_message():

    is_error = False
    try:
        output = fh.readTXTFile(statefile)
    except:
        is_error = True

    if not is_error:
        user = prev.get_prev_user(output)
        date = prev.get_prev_login_date(output)

        title = sf.title("LOGINMESSAGE")
        msg = [
            title,
            f"User who last logged in: {user}",
            f"Last login date: {date}",
        ]
        
        print("\n")
        print(*msg, sep="\n")

def write_login_data():

    try:
        #print(statefile)
        fh.createFileInSpecifiedDir(statefile)
    except OSError as o:
        print(o)

    today = datetime.datetime.today().strftime("%A")
    clock = datetime.datetime.now().strftime("%H:%M:%S") # <- clock right now in local time
    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

    toAdd = [
        f"User '{mv.system_user}' logged in: {today} {th.getDateToday()} {clock} {timezone}.",
        f"TextUI version: {mv.version_number}. Build date: {mv.version_date}.",
        f"Operating system: {mv.currentOS}"
    ]

    for e in toAdd:
        fh.addTextToSpecifiedFile(statefile, e + "\n")

def is_login_message_enabled() -> bool:
    try:
        output = fh.readTXTFile(mv.userconfig_location)
    except:
        return False

    current_branch_selected = None

    for e in output:
        current_variable_selected = None
        if "[" and "]" in e:
            current_branch_selected = e    
            #print(f"Branch selected: {current_branch_selected}")
        elif current_branch_selected and " = " in e:
            current_variable_selected = e.split(";")[0]
        if current_variable_selected == "loginMessage = True" and current_branch_selected.split("\n")[0] == "[MISC]":
            return True
    return False