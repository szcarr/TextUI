import time

import time_related.timeHandling as th

import fileHandling as fh
import myvariables as mv

countdown_description = '''
User can create countdowns to keep track of their stuff.
Add example: countdown -a "Christmas" "2022-12-24 00:00:00"
User can remove countdowns by their index gotten from the command: countdown -l
Remove example: countdown -r 0
User can list current tracked countdowns and get their index
List example: countdown -l
'''

countdown_txt_location = mv.usr_folder + mv.countdown_txt

def countdown(countdown_date, countdown_from) -> str:

    '''
    countdown_date is where the target date is
    countdown_from is where to start the countdown from

    Passed in the form 'YYYY-MM-DD HH:MM:SS' as a string.\n

    Returns time left till date
    '''

    ct_date = countdown_date.split(" ")
    ct_date_ymd = th.getYearMonthDay(ct_date[0])
    ct_date_hms = th.getHoursMinutesSeconds(ct_date[1])

    ct_from = countdown_from.split(" ")
    ct_from_ymd = th.getYearMonthDay(ct_from[0])
    ct_from_hms = th.getHoursMinutesSeconds(ct_from[1])

    date_lst = [ct_date_ymd, ct_date_hms]
    from_lst = [ct_from_ymd, ct_from_hms]

    output = check_if_time_is_in_the_past(date_lst, from_lst)
    if output:
        #print("Time is in the past")
        return f"-1"

    #print("Time was not in the past")
    days_remaining = 0
    
    start_month, end_month = int(ct_from_ymd[1]), int(ct_date_ymd[1])
    start_year, end_year = int(ct_from_ymd[0]), int(ct_date_ymd[0])

    month_counter = start_month + 1
    year_counter = int(ct_from_ymd[0])

    if start_year != end_year or start_month != end_month:
        while year_counter != end_year or month_counter != end_month:
            if month_counter % 13 == 0:
                year_counter += 1
                month_counter = 1
            if year_counter == end_year and month_counter == end_month:
                break
            if year_counter > 10000: 
                # User has either gave an illegal input or time is in the past:
                return "-1"
           # print(year_counter, month_counter, end_year,  end_month)
            days_remaining += th.monthrange(year_counter, month_counter)[1]
            #print(year_counter, month_counter, days_remaining)
            month_counter += 1
            #time.sleep(1)
        days_left_in_current_month = int(th.monthrange(ct_from_ymd[0], ct_from_ymd[1])[1]) - int(ct_from_ymd[2])
        days_left_in_target_month = int(ct_date_ymd[2])

        days_remaining += days_left_in_current_month + days_left_in_target_month

    else: # Date is in same month as from month
        day_diff = (int(ct_date_ymd[2]) - 1) - int(ct_from_ymd[2])
        days_remaining += day_diff

    lst = [
        (24 - int(ct_from_hms[0]) - 1) + int(ct_date_hms[0]), # Remaining hours of the day
        (60 - int(ct_from_hms[1]) - 1) + int(ct_date_hms[1]), # Remaining minutes of the day
        (60 - int(ct_from_hms[2])) + int(ct_date_hms[2]), # Remaining seconds of the day
    ]

    timeleft = ""
    for i in range(len(lst) - 1, -1, -1):
        while lst[i] >= 60 and i == 2: # Seconds appending to minutes
            lst[i] = lst[i] - 60
            lst[i - 1] = lst[i - 1] + 1

        while lst[i] >= 60 and i == 1: # Minutes appending to hours
            lst[i] = lst[i] - 60
            lst[i - 1] = lst[i - 1] + 1

        while lst[i] >= 24 and i == 0: # Hours appending to days
            lst[i] = lst[i] - 24
            days_remaining += 1

    for i, e in enumerate(lst): # Creating the timeleft string
        addon = ":"
        if i == len(lst) - 1:
            addon = ""
        timeleft += str(e) + addon
        
    return f"{days_remaining} {timeleft}"


def toString(countdown_name, time):
    '''
    https://zetcode.com/python/fstring/
    '''
    lst = str(time).split(" ")
    timelist = lst[1].split(":")
    days = lst[0]
    fstring = f'''
 -- Countdown to '{countdown_name}'.
    {days:>3} {timelist[0]:>4} {timelist[1]:>6} {timelist[2]:>7}
    {"Days":>4} {"Hours":>5} {"Minutes":>5} {"Seconds":>5}
    '''
    return fstring

def add_countdown(name, date):
    '''
    Date should be passed in the format "YYYY-MM-DD HH:MM:SS"
    '''
    
    output = read_countdown_txt()
    for index, element in enumerate(output):
        if element == "\n" or element == "": #If empty slot then add contents here
            fh.replaceLineInFile(countdown_txt_location, index, f"{name} {date}")
            break
    
    new_version = read_countdown_txt()
    if output == new_version: # Compares if countdown txt is different if different it has already updated the txt file
        fh.addTextToSpecifiedFile(countdown_txt_location, f"{name} {date}\n")

def read_countdown_txt():

    '''
    Reads content of countdown.txt
    '''

    output = fh.readTXTFile(countdown_txt_location)

    r_list = [] # Refined list
    for e in output:
        fstring = e.split("\n")[0]
        r_list.append(fstring)
    return r_list

def print_countdown_txt():
    lst = read_countdown_txt()
    for i, e in enumerate(lst):
        print(f"{i} : {e}")

def remove_countdown(i):
    '''
    i (index) -> int
    '''
    fh.replaceLineInFile(countdown_txt_location, i, "")

def initialize_countdowns():
    output = read_countdown_txt()
    r_list = []
    for e in output:
        if e == "\n" or e == "":
            continue
        fstring = e.split("\n")[0]
        r_list.append(fstring)

    countdown_list = []
    for s in r_list:
        name = s.split('"')[1]
        datelist = s.split(" ")
        date, time = datelist[len(datelist) - 2], datelist[len(datelist) - 1]
        countdown_date = f"{date} {time}"
        dateandtime = f"{th.getDateToday()} {th.get_local_time()}"
        funny = toString(name, countdown(countdown_date, dateandtime))
        countdown_list.append(funny)

    return countdown_list

def check_if_time_is_in_the_past(date_lst, from_lst):

    '''
    Inputs are: date = [[year, month, day], [hour, minutes, seconds]]\n
    Returns true if time is in the past\n
    Else returns false\n
    '''

    if date_lst[0][0] < from_lst[0][0]:
        return True
    if date_lst[0][0] <= from_lst[0][0] and date_lst[0][1] < from_lst[0][1]:
        return True
    if date_lst[0][0] <= from_lst[0][0] and date_lst[0][1] <= from_lst[0][1] and date_lst[0][2] < from_lst[0][2]:
        return True
    if date_lst[0][0] <= from_lst[0][0] and date_lst[0][1] <= from_lst[0][1] and date_lst[0][2] <= from_lst[0][2] and date_lst[1][0] < from_lst[1][0]:
        return True
    if date_lst[0][0] <= from_lst[0][0] and date_lst[0][1] <= from_lst[0][1] and date_lst[0][2] <= from_lst[0][2] and date_lst[1][0] <= from_lst[1][0] and date_lst[1][1] < from_lst[1][1]:
        return True
    if date_lst[0][0] <= from_lst[0][0] and date_lst[0][1] <= from_lst[0][1] and date_lst[0][2] <= from_lst[0][2] and date_lst[1][0] <= from_lst[1][0] and date_lst[1][1] < from_lst[1][1] and date_lst[1][2] < from_lst[1][2]:
        return True
    return False