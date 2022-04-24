import time
import timeHandling as th

countdown_description = '''
User can create countdowns to keep track of their stuff.
Add example: countdown -a "Christmas" "2022-12-24 00:00:00"
User can remove countdowns by their index gotten from the command: countdown -l
Remove example: countdown -r 0
User can list current tracked countdowns and get their index
List example: countdown -l
'''

def countdown(countdown_date, countdown_from) -> str:

    '''
    countdown_date is where the target date is
    countdown_from is where to start the countdown from

    Passed in the form 'YYYY-MM-DD HH:MM:SS' as a string.\n

    Returns
    '''

    ct_date = countdown_date.split(" ")
    ct_date_ymd = th.getYearMonthDay(ct_date[0])
    ct_date_hms = th.getHoursMinutesSeconds(ct_date[1])

    ct_from = countdown_from.split(" ")
    ct_from_ymd = th.getYearMonthDay(ct_from[0])
    ct_from_hms = th.getHoursMinutesSeconds(ct_from[1])

    days_remaining = 0
    
    start_month, end_month = int(ct_from_ymd[1]), int(ct_date_ymd[1])
    start_year, end_year = int(ct_from_ymd[0]), int(ct_date_ymd[0])

    month_counter = start_month + 1
    year_counter = int(ct_from_ymd[0])
    if start_year != end_year or start_month != end_month:
        #print(year_counter, end_year, month_counter, end_month)
        while year_counter != end_year or month_counter != end_month: # Skal vere good
            if month_counter % 13 == 0:
                year_counter += 1
                month_counter = 1
            if year_counter == end_year and month_counter == end_month:
                break
            #print(year_counter, end_year, month_counter, end_month)
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
Countdown to '{countdown_name}'.
    {days:>3} {timelist[0]:>4} {timelist[1]:>6} {timelist[2]:>7}
    {"Days":>4} {"Hours":>5} {"Minutes":>5} {"Seconds":>5}
    '''
    return fstring

FERIE = "2022-06-16 14:15:00"

RAGNBRUSDAG = "2023-01-30 00:00:00"
IMORGON = "2022-04-24 14:15:30"

YEAR = "2025-04-22 14:15:30"
TESTTIME = "2022-04-25 19:56:30"

DARKSECRET = "2022-04-23 23:00:00"

dateandtime = f"{th.getDateToday()} {th.get_local_time()}"

while True:
    dateandtime = f"{th.getDateToday()} {th.get_local_time()}"
    print(toString("Sommar ferie", countdown(FERIE, dateandtime)))
    time.sleep(1)