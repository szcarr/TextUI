import os
import fileHandling as fh

verbose = True #Acts as a global switch
system = True

textUI = True
settings = True
config = True

textUIPrint = True if verbose and textUI else False
systemPrint = True if verbose and system else False
configPrint = True if verbose and config else False

settingVariables = "Setting variables"

def conditionalPrint(bool, toPrint):
    if bool:
        print(toPrint)

def nameOfCurrentFile():
    return str(os.path.basename(__file__)).split(fh.detectOS())[-1]