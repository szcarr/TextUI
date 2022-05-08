import string

letters = string.ascii_letters
numbers = string.octdigits
symbols = string.punctuation

def convertListToString(lst):
    string = ""
    for e in lst:
        string = string + e
    return string

def excludeCharsFromString(string, exclude):

    '''
    Exclude is a list with chars to exclude.\n
    String is the string to be operated on.\n
    Returns formatted string.
    '''

    fString = ""
    for c in string:
        skip = False
        for e in exclude:
            if c == e:
                skip = True
                continue
        if not skip:
            fString = fString + c        
    return fString

def removeSpacesBeforeAndAfterString(string):

    '''
    s = String to be formatted
    Returns s but formatted 
    '''

    firstCharIndex = -1
    lastCharIndex = -1
    hasNotFoundFirstChar = True
    for c in range(len(string)):
        if string[c] == " ":
            continue
        elif hasNotFoundFirstChar and string[c] != " ":
            hasNotFoundFirstChar = False
            firstCharIndex = c
        elif string[c] != " ":
            lastCharIndex = c

    newString = ""
    for i in range(firstCharIndex, lastCharIndex):
        newString = newString + string[i]

    return newString

def title(titlestring):

    '''
    Try to keep arg string an even amount of chars
    '''
    titlestring = list(titlestring)
    length = 50
    string_startpoint = int(round(length / 2 - len(titlestring) / 2, 0))
    string_endpoint = int(round(string_startpoint + len(titlestring)))
    char_lst = []
    for i in range(length):
        char = ""
        if i == 0:
            char = "<"
        elif i == length - 1:
            char = ">"
        elif i == string_startpoint - 1 or i == string_endpoint:
            char = "|"
        elif i > string_startpoint - 1 and i < string_endpoint:
            char = titlestring[i - string_startpoint]
        else:
            char = "="
        char_lst.append(char)
    fstring = convertListToString(char_lst)
    return fstring

def testTitle(fstring):
    lst = list(fstring)
    lookfor = "="
    count_lst = []
    counter = 0
    for e in lst:
        if e == lookfor:
            counter += 1
        else:
            if counter != 0:
                count_lst.append(counter)
            counter = 0
    print(count_lst)

#mys = "COCKMANNNNNsNNNNN"
#s = title(mys)
#print(s, len(s), len(mys))
#
#testTitle(s)