def get_prev_user(statefile_output):
    for e in statefile_output:
        if "User" in e and "logged in:" in e:
            user = e.split("'")[1]
            return user

def get_prev_login_date(statefile_output):
    for e in statefile_output:
        if "User" in e and "logged in:" in e:
            date = e.split("logged in: ")[1].split("\n")[0]
            return date

#get_prev_user()