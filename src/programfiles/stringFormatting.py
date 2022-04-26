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