import programfiles.myvariables as mv
import programfiles.fileHandling as fh

def get_value_from_states(variable):
    
    '''
    Get the selected variable and value
    Returns '-1' if function does not find variable
    Else returns variable's value
    '''

    output = fh.readTXTFile(mv.state_folder + mv.standby_states_txt)

    value = "-1"
    for e in output:
        if variable in e:
            value = e.split("\n")[0].split(" = ")[1]

    return value


def write_states(state, value):
    state_file = mv.state_folder + mv.standby_states_txt
    file_output = fh.readTXTFile(state_file)
    foundline = False
    line =  f"{state} = {value}"
    for i, e in enumerate(file_output):
        if state in e:
            fh.replaceLineInFile(state_file, i, line)
            foundline = True

    if foundline == False:
        fh.addTextToSpecifiedFile(state_file, f"{line}\n")