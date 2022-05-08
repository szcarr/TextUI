import time

import time_related.countdown.countdown as countdown
import fileHandling as fh
import myvariables as mv

def main():
    for i in range(50):
        print("\n")
    while True:
        try:
            do_countdown()
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"Exiting standby mode.")
            break

def do_countdown():
    countdown_list = countdown.initialize_countdowns()
    for e in countdown_list:
        print(e)

def get_states():
    pass

def setup():
    file = mv.usr_folder + f"standby_settings.txt"
    if not fh.checkIfFileExist(file):
        fh.createFileInSpecifiedDir(file)

        to_add = [
            f""
        ]

        for e in to_add:
            fh.addTextToSpecifiedFile(file, f"{e}\n")