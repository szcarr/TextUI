import os

import fileHandling as fh

projectFolderLocation = "D:\\Documents\\Viktig\\Programmering\\TextUI\\"

loc = projectFolderLocation + fh.detectOS() + "src" + fh.detectOS() + "cfg" + fh.detectOS() + "user" + fh.detectOS()
splitlist = os.popen("dir " + loc).read().split("\n")
#print(len(splitlist))
for i in range(len(splitlist)):
    if "userconfig.txt" in splitlist[i]:
        temp = splitlist[i].split(" ")
        for i in range(len(temp)):
            if temp[i] == "userconfig.txt":
                fileSize = temp[i - 1]


print(fileSize)