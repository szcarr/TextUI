import programfiles.myvariables as mv
import programfiles.fileHandling as fh

def get_userconfigs_value(branch, variable):
    '''
    Get a selected variable and value from a specified branch
    Returns '-1' if function does not find variable from branch
    Else returns variable's value
    '''

    output = fh.readTXTFile(mv.userconfig_location)
    current_branch = ""
    value = "-1"
    
    for e in output:
        if "[" and "]" in e: #
            current_branch = e.split("\n")[0]
        if current_branch == branch and variable in e:
            value = e.split(" = ")[1].split(";")[0]

    return value