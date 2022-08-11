import time

import time_related.countdown.countdown as countdown
import time_related.addtime.addtime as addtime
import time_related.timeHandling as th

import crypto.cryptoprices as cryptoprice

import fileHandling as fh
import myvariables as mv

import stringFormatting as sf

import states.standby_state as standby_state

import config.userconfig as userconfig

first_run = True

def main():
    global first_run
    first_run = True
    for _ in range(50):
        print("")
    while True:
        try:
            do_countdown()
            #do_crypto()

            time.sleep(5)
            first_run = False

        except KeyboardInterrupt:
            print(f"Exiting standby mode.")
            break

def do_countdown():
    global first_run

    for e in all_standby_values():
        name = e.split("PrintDelay")[0]
        state_write_name = f"{name}_nextprint"

        date_and_time_today = f"{th.getDateToday()} {th.get_local_time()}"
        date_today, time_today = date_and_time_today.split(" ")
        now_lst = [[int(i) for i in date_today.split("-")], [int(i) for i in time_today.split(":")]] # Converting str to int

        from_date_and_time = standby_state.get_value_from_states(state_write_name)
        if from_date_and_time != "-1":
            from_date, from_time = from_date_and_time.split(" ")
            from_lst = [[int(i) for i in from_date.split("-")], [int(i) for i in from_time.split(":")]] # Converting str to int

        is_ready_for_print = False
        if from_date_and_time == "-1":
            is_ready_for_print = False
        elif countdown.check_if_time_is_in_the_past(from_lst, now_lst):
            is_ready_for_print = True

        if first_run or is_ready_for_print:
            if name == f"countdown":
                countdown_list = countdown.initialize_countdowns()

                title = sf.title("COUNTDOWNS")
                print("")
                print(title)

                for c in countdown_list:
                    print(c)

            elif name == f"cryptoTrending":
                title = sf.title("TRENDING CRYPTO")
                print("")
                print(title)
        
                cryptoprice.print_trending_coins_data()

            time_to_add = userconfig.get_userconfigs_value("[STANDBY]", e)
            nextprint_value = addtime.format_time_to_within_bounds(addtime.add_time(time_to_add, date_and_time_today))
            standby_state.write_states(state_write_name, nextprint_value)

def do_crypto():
    pass
#    if first_run or is_ready_for_print:
#        title = sf.title("TRENDING CRYPTO")
#        print("")
#        print(title)
#
#        cryptoprice.print_trending_coins_data()


def all_standby_values(): #TEMP
    '''
        Gets all printable objects from userconfig.txt
    '''

    output = fh.readTXTFile(mv.userconfig_location)
    current_branch = ""
    
    branch = "[STANDBY]"


    standby_values = []
    for e in output:
        if "[" and "]" in e: #
            current_branch = e.split("\n")[0]
            continue
        if current_branch == branch and e != "\n":
            standby_values.append(e.split("\n")[0].split(" = ")[0])

    return standby_values