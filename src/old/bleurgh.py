import time
import timeHandling as th

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
    
    years_remaining = 0

    start_month = int(ct_from_ymd[1])
    end_month = int(ct_date_ymd[1])

    start_year, end_year = int(ct_from_ymd[0]), int(ct_date_ymd[0])

    for i in range(start_year, end_year): # Calculating how many years to add
        #print(i == end_year - 1, end_month == start_month)
        future = False
        if i == end_year - 1 and end_month == start_month:
            print("AOISDJASOD")
            if int(ct_date_ymd[2]) >= int(ct_from_ymd[2]):
             #   print("DAY")
                future = True
            elif int(ct_date_ymd[2]) >= int(ct_from_ymd[2]) and int(ct_date_hms[0]) >= int(ct_from_hms[0]):
              #  print("HOURS")
                future = True
            elif int(ct_date_ymd[2]) >= int(ct_from_ymd[2]) and int(ct_date_hms[0]) >= int(ct_from_hms[0]) and int(ct_date_hms[1]) >= int(ct_from_hms[1]):
               # print("MINUTES")
                future = True
            elif int(ct_date_ymd[2]) >= int(ct_from_ymd[2]) and int(ct_date_hms[0]) >= int(ct_from_hms[0]) and int(ct_date_hms[1]) >= int(ct_from_hms[1]) and int(ct_date_hms[2]) >= int(ct_from_hms[2]):
                #print("SECONDS")
                future = True
        elif i < end_year and end_month > start_month:
#            print("SJÅ PÅ DINNA DEN E NOK LITT FEIL")
            years_remaining += 1
        elif i < end_year - 2: # Means that its more than a whole year
 #           print("AOOOGA")
            years_remaining += 1
        elif future:
            years_remaining += 1
    #    print(i, years_remaining)
    #    print(future)

    if years_remaining > 0 or start_month != end_month: # If different years or
        if years_remaining > 0:
            for i in range(years_remaining): # Converting years to days
                days_remaining += 365
        else: # If one year
            end_month = (12 - start_month) + end_month - 1

        #print(end_month)

        month_counter = start_month
        year_counter = int(ct_from_ymd[0])
        

        starting_point = start_month + 1
        end_point = end_month + starting_point
        print(starting_point, end_point)
        for i in range(starting_point, end_point): # Adding days in months
            if month_counter % 12 == 0:
                month_counter = 1
                year_counter += 1
            print("MONTH YEAR", month_counter, year_counter)
            days_remaining += th.monthrange(year_counter, month_counter)[1]
            month_counter += 1

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

    for i, e in enumerate(lst):
        addon = ":"
        if i == len(lst) - 1:
            addon = ""
        timeleft += str(e) + addon
        
    return f"{days_remaining} {timeleft}"


def toString(countdown_name, time):
    lst = str(time).split(" ")
    timelist = lst[1].split(":")
    days = lst[0]
    fstring = f'''
Countdown to '{countdown_name}'.
{days:>6} {days:>4}
                
    '''
    return fstring

FERIE = "2022-06-16 14:15:00"

RAGNBRUSDAG = "2023-01-30 00:00:00"
IMORGON = "2022-04-24 14:15:30"


YEAR = "2025-04-22 14:15:30"
TESTTIME = "2022-04-23 19:56:30"

DARKSECRET = "2022-04-23 23:00:00"

dateandtime = f"{th.getDateToday()} {th.get_local_time()}"

while True:
    dateandtime = f"{th.getDateToday()} {th.get_local_time()}"
    print(toString("Dark secret",countdown(FERIE, dateandtime)))
    time.sleep(1)