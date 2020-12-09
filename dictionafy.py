import re
diction = {}
inputname = str(input("Input the name of the file including extension [e.g. input.txt]: "))
inputfile = open(inputname, 'r')
for line in inputfile:
    splitline = line.split(" ")
    for word in splitline:
        if re.sub(r'[^\w\s]', '', word.split('\n')[0]).lower() in diction:
            diction[re.sub(r'[^\w\s]', '', word.split('\n')[0]).lower()] += 1
        else:
            diction[re.sub(r'[^\w\s]', '', word.split('\n')[0]).lower()] = 1
for row in diction:
    print(row,":",diction[row])