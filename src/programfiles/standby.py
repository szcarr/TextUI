import time

import time_related.countdown.countdown as countdown
import time_related.addtime.addtime as addtime
import time_related.timeHandling as th

import fileHandling as fh
import myvariables as mv

first_run = True

def main():
    global first_run
    for _ in range(50):
        print("\n")
    while True:
        try:
            do_countdown()
    
            time.sleep(1)
            first_run = False

        except KeyboardInterrupt:
            print(f"Exiting standby mode.")
            break

def do_countdown():
    global first_run

    date_and_time_today = f"{th.getDateToday()} {th.get_local_time()}"
    date, time = date_and_time_today.split(" ")
    now_lst = [[int(i) for i in date.split("-")], [int(i) for i in time.split(":")]] # Converting str to int

    from_date_and_time = get_value_from_states("countdown_next_print")
    from_date, from_time = from_date_and_time.split(" ")
    from_lst = [[int(i) for i in from_date.split("-")], [int(i) for i in from_time.split(":")]] # Converting str to int

    is_ready_for_print = countdown.check_if_time_is_in_the_past(from_lst, now_lst)

    if first_run or is_ready_for_print:
        time_to_add = get_userconfigs_value("[STANDBY]", "countdownPrintDelay")
        nextprint_value = addtime.format_time_to_within_bounds(addtime.add_time(time_to_add, date_and_time_today))
        write_states("countdown_next_print", nextprint_value)
        
        countdown_list = countdown.initialize_countdowns()
        for e in countdown_list:
            print(e)


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
        fh.addTextToSpecifiedFile(state_file, line)

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