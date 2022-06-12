
from calendar import monthrange

def add_time(add, date_and_time):
    '''
    add arg should be passed in the format:
    'HH:MM:SS'

    date_and_time should be passed in the format:
    'YYYY-MM-DD HH:MM:SS'
    
    '''

    add_lst = add.split(":")
    y_m_d, h_m_s = date_and_time.split(" ")

    date = y_m_d.split("-")
    time = h_m_s.split(":")

    new_list = [i for i in range(6)]

    for i in range(2, -1, -1):
        to_add = int(add_lst[i])
        time_time = int(time[i])
        new_list[i + 3] = to_add + time_time

    for i in range(len(date)):
        new_list[i] = int(date[i])

    fstring = datelist_to_string(new_list)
    return fstring

def format_time_to_within_bounds(date_and_time):
    y_m_d, h_m_s = date_and_time.split(" ")

    date = y_m_d.split("-")
    time = h_m_s.split(":")
    
    date_and_time_limits = [9999, 12, monthrange(int(date[0]), int(date[1]))[1], 24, 60, 60]

    new_list = [i for i in range(len(date_and_time_limits))]

    for i, e in enumerate(date):
        new_list[i] = int(e)

    for i, e in enumerate(time):
        new_list[i + 3] = int(e)

    for i in range(len(new_list) - 1, -1, -1):
        if new_list[i] >= date_and_time_limits[i] and i > 0:
            new_list[i] = new_list[i] - date_and_time_limits[i]
            new_list[i - 1] = new_list[i - 1] + 1

    fstring = datelist_to_string(new_list)
    return fstring

def datelist_to_string(datelist):
    '''
    Takes a list = [year, month, day, hour, minutes, seconds]
    Returns a string: 'YYYY-MM-DD HH:MM:SS' 
    '''    

    fstring = ""
    for i, e in enumerate(datelist):
        split = " "
        if i < 2:
            split = "-"
        elif i > 2 and i < len(datelist) - 1:
            split = ":"
        elif i == len(datelist) - 1:
            split = ""
        fstring += str(e) + split

    return fstring