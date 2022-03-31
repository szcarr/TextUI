import timeHandling

exitProgram = False
firstRun = True

parent = "schedule"

modeHelpList = {
    "setup": "Setup | Sets up a new schedule | Syntax: " + parent + " setup",
}

def setup():
    print("When do you usually go to bed? Enter digital clock time(00:00-23:59). In format 'HH:MM.")
    print(">> ", end="")
    startToSleep = input()

    print("When do you usually wake up? Enter digital clock time(00:00-23:59). In format 'HH:MM.")
    print(">> ", end="")
    wakeUpTime = input()

    print(startToSleep)
    print(wakeUpTime)

def printModes():
    keysForModeList = list(modeHelpList.keys())
    counter = 0
    print("\n<=========================|SCHEDULE|=========================>")
    for key in keysForModeList:
        counter += 1
        print(str(counter) + ": " + str(modeHelpList.get(key)))

#playsound("/home/scp092/Downloads/yt5s.com - The Wilhelm scream sound effect (128 kbps).mp3")