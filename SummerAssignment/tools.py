#Converts Numbers To Words
def convert(number):
    tenNeeded = False #Varible used to find out if teen/eleven type numbers should be used
    strNumber = str(number) #converts number to string
    length = len(strNumber) #finds out how many digits in the number
    output = list() #creates empty list to be filled with the words
    if length == (4): #If the number is 4 digits long, it will start at the thousands and go down
        if strNumber[0] == ("1"): #Will check every digit for a number then put relevant word in the output list
            output.append("one thousand")
        elif strNumber[0] == ("2"):
            output.append("two thousand")
        elif strNumber[0] == ("3"):
            output.append("three thousand")
        elif strNumber[0] == ("4"):
            output.append("four thousand")
        elif strNumber[0] == ("5"):
            output.append("five thousand")
        elif strNumber[0] == ("6"):
            output.append("six thousand")
        elif strNumber[0] == ("7"):
            output.append("seven thousand")
        elif strNumber[0] == ("8"):
            output.append("eight thousand")
        elif strNumber[0] == ("9"):
            output.append("nine thousand")
        output.append(",")
        if strNumber[1] == ("1"):
            output.append("one hundred")
        elif strNumber[1] == ("2"):
            output.append("two hundred")
        elif strNumber[1] == ("3"):
            output.append("three hundred")
        elif strNumber[1] == ("4"):
            output.append("four hundred")
        elif strNumber[1] == ("5"):
            output.append("five hundred")
        elif strNumber[1] == ("6"):
            output.append("six hundred")
        elif strNumber[1] == ("7"):
            output.append("seven hundred")
        elif strNumber[1] == ("8"):
            output.append("eight hundred")
        elif strNumber[1] == ("9"):
            output.append("nine hundred")
        output.append("and")
        if strNumber[2] == ("1"):
            tenNeeded = True
        elif strNumber[2] == ("2"):
            output.append("twenty")
        elif strNumber[2] == ("3"):
            output.append("thirty")
        elif strNumber[2] == ("4"):
            output.append("fourty")
        elif strNumber[2] == ("5"):
            output.append("fifty")
        elif strNumber[2] == ("6"):
            output.append("sixty")
        elif strNumber[2] == ("7"):
            output.append("seventy")
        elif strNumber[2] == ("8"):
            output.append("eighty")
        elif strNumber[2] == ("9"):
            output.append("ninety")
        if strNumber[3] == ("1"):
            if tenNeeded:
                output.append("eleven")
            else:
                output.append("one")
        elif strNumber[3] == ("2"):
            if tenNeeded:
                output.append("twelve")
            else:
                output.append("two")
        elif strNumber[3] == ("3"):
            if tenNeeded:
                output.append("thirteen")
            else:
                output.append("three")
        elif strNumber[3] == ("4"):
            output.append("four")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[3] == ("5"):
            if tenNeeded:
                output.append("fifteen")
            else:
                output.append("five")
        elif strNumber[3] == ("6"):
            output.append("six")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[3] == ("7"):
            output.append("seven")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[3] == ("8"):
            output.append("eight")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[3] == ("9"):
            output.append("nine")
            if tenNeeded:
                output.extend("teen")
    elif length == (3): #If the number is 3 digits long, it will start at the hundreds and go down
        if strNumber[0] == ("1"):
            output.append("one hundred")
        elif strNumber[0] == ("2"):
            output.append("two hundred")
        elif strNumber[0] == ("3"):
            output.append("three hundred")
        elif strNumber[0] == ("4"):
            output.append("four hundred")
        elif strNumber[0] == ("5"):
            output.append("five hundred")
        elif strNumber[0] == ("6"):
            output.append("six hundred")
        elif strNumber[0] == ("7"):
            output.append("seven hundred")
        elif strNumber[0] == ("8"):
            output.append("eight hundred")
        elif strNumber[0] == ("9"):
            output.append("nine hundred")
        output.append("and")
        if strNumber[1] == ("1"):
            tenNeeded = True
        elif strNumber[1] == ("2"):
            output.append("twenty")
        elif strNumber[1] == ("3"):
            output.append("thirty")
        elif strNumber[1] == ("4"):
            output.append("fourty")
        elif strNumber[1] == ("5"):
            output.append("fifty")
        elif strNumber[1] == ("6"):
            output.append("sixty")
        elif strNumber[1] == ("7"):
            output.append("seventy")
        elif strNumber[1] == ("8"):
            output.append("eighty")
        elif strNumber[1] == ("9"):
            output.append("ninety")
        if strNumber[2] == ("1"):
            if tenNeeded:
                output.append("eleven")
            else:
                output.append("one")
        elif strNumber[2] == ("2"):
            if tenNeeded:
                output.append("twelve")
            else:
                output.append("two")
        elif strNumber[2] == ("3"):
            if tenNeeded:
                output.append("thirteen")
            else:
                output.append("three")
        elif strNumber[2] == ("4"):
            output.append("four")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[2] == ("5"):
            if tenNeeded:
                output.append("fifteen")
            else:
                output.append("five")
        elif strNumber[2] == ("6"):
            output.append("six")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[2] == ("7"):
            output.append("seven")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[2] == ("8"):
            output.append("eight")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[2] == ("9"):
            output.append("nine")
            if tenNeeded:
                output.extend("teen")
    elif length == (2): #If the number is 2 digits long, it will start at the tens and go down
        if strNumber[0] == ("1"):
            tenNeeded = True
        elif strNumber[0] == ("2"):
            output.append("twenty")
        elif strNumber[0] == ("3"):
            output.append("thirty")
        elif strNumber[0] == ("4"):
            output.append("fourty")
        elif strNumber[0] == ("5"):
            output.append("fifty")
        elif strNumber[0] == ("6"):
            output.append("sixty")
        elif strNumber[0] == ("7"):
            output.append("seventy")
        elif strNumber[0] == ("8"):
            output.append("eighty")
        elif strNumber[0] == ("9"):
            output.append("ninety")
        if strNumber[1] == ("1"):
            if tenNeeded:
                output.append("eleven")
            else:
                output.append("one")
        elif strNumber[1] == ("2"):
            if tenNeeded:
                output.append("twelve")
            else:
                output.append("two")
        elif strNumber[1] == ("3"):
            if tenNeeded:
                output.append("thirteen")
            else:
                output.append("three")
        elif strNumber[1] == ("4"):
            output.append("four")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[1] == ("5"):
            if tenNeeded:
                output.append("fifteen")
            else:
                output.append("five")
        elif strNumber[1] == ("6"):
            output.append("six")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[1] == ("7"):
            output.append("seven")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[1] == ("8"):
            output.append("eight")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[1] == ("9"):
            output.append("nine")
            if tenNeeded:
                output.extend("teen")
    elif length == (1): #If the number is 1 digit long, it will start at the digits and go down
        if strNumber[0] == ("1"):
            if tenNeeded:
                output.append("eleven")
            else:
                output.append("one")
        elif strNumber[0] == ("2"):
            if tenNeeded:
                output.append("twelve")
            else:
                output.append("two")
        elif strNumber[0] == ("3"):
            if tenNeeded:
                output.append("thirteen")
            else:
                output.append("three")
        elif strNumber[0] == ("4"):
            output.append("four")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[0] == ("5"):
            if tenNeeded:
                output.append("fifteen")
            else:
                output.append("five")
        elif strNumber[0] == ("6"):
            output.append("six")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[0] == ("7"):
            output.append("seven")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[0] == ("8"):
            output.append("eight")
            if tenNeeded:
                output.extend("teen")
        elif strNumber[0] == ("9"):
            output.append("nine")
    words = ""
    run = 0
    for item in output:
        if run == 0:
            words = item
        elif run > 0:
            words = (words+' '+item)
        run = run + 1
    return words
