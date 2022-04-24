import os
import fileHandling as fh

verbose = False #Acts as a global switch
system = True
user = True #Should be True by default

textUI = False
settings = False
config = True

systemPrint = True if verbose and system else False
userPrint = True if verbose and user else False
textUIPrint = True if verbose and textUI else False
settingsPrint = True if verbose and settings else False
configPrint = True if verbose and config else False

settingVariables = "Setting variables"

def conditionalPrint(bool, to_print):
    if bool:
        print(to_print)

def nameOfCurrentFile():
    return str(os.path.basename(__file__)).split(fh.detectOS())[-1]