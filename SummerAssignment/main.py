#Number Wording Quiz
#Adam Baker
import random, tools, time, os #Imports Modules And Tools.py

wins = 0 #Creates Variable for how many questions they got right
username = input("What is your name? E.g JohnSmith ")
try:
    os.mkdir(username)
except:
    print ("Welcome Back")
file = open(username+'/'+"ca.pak" ,"a") #Creates ca.pak file if it doesn't already exist
file.close()

correct = list() #Grabs all data from ca.pak and puts it in list variable
file = open(username+'/'+"ca.pak", "r")
line = file.readline()
correct = line.split(',')
file.close()
correct.remove('')
try:
    incorrect = list() #Grabs all data from ia.pak and puts it in list variable
    file = open(username+'/'+"ia.pak", "r")
    line = file.readline()
    incorrect = line.split(',')
    incorrect.remove('')
except:
    print()
file.close()
def questGen(): #Defines the system for generating and asking a question
    global correct
    global incorrect
    global wins
    if len(incorrect) == (0): #Checks if there are any questions that where answered incorrectly
        digits = random.randint(0,9999) #picks a random number smaller than 10,000 and larger than -1
    elif len(incorrect) > (0):
        digits = int(random.choice(incorrect)) #Will get the user a question they got wrong before until they get it right
        incorrect.remove(str(digits)) #Removes given question from the file/list
        os.remove(username+'/'+'ia.pak')
        file = open(username+'/'+"ia.pak","a")
        for item in incorrect:
                file.write(item+',')
        file.close
    for item in correct: #Checks if number has been correct before
        if int(item) == digits:
            questGen() #Gets a new number
        else:
            break #Continues the question generation
    words = tools.convert(digits) #Converts Number to Words
    text = "Write: |"+words+"| as a number! "
    question = int(input(text)) #Asks The Question
    if question == digits:
        print("You got it right!")
        wins = wins + 1 #adds a score to the variable
        file = open(username+'/'+"ca.pak", "a") #Saves Question To ca.pak as it was answered correctly
        file.write(str(digits)+',')
        file.close()
    elif question != digits:
        print("You got it wrong!") #User got it wrong so question can still be asked, no score is added
        file = open(username+'/'+"ia.pak", "a") #Saves Question To ia.pak as it was answered incorrectly
        file.write(str(digits)+',')
        file.close()
    print()
def repeat(): #system for testing the program, should never actually get used
    print()
    menu = input("Do you want another question? [yes] or [no]? ")
    if menu.lower() == ("yes"):
        questGen()
    elif menu.lower() == ("no"):
        exit()
    else:
        print("Please Input [yes] or [no]!")
        print()
        repeat()
print("Welcome To The Number Test!!!")
time.sleep(1)
print("You will be given 10 questions") #Information For The Student To Be Ready For The Test
time.sleep(1)
print("Overall score will given at the end")
time.sleep(1)
for x in range (1,11): #Generates 10 Questions And Tells Them What Number They Are On
    print("Question",x)
    time.sleep(0.2)
    questGen()
print("You got "+str(wins)+" right!")
file = open(username+'/'+"scores.pak","a")
file.write(str(wins)+'\n')
file.close()
file = open(username+'/'+"StudentScores.txt","a")
file.write(str(wins)+'\n')
file.close()
file = open(username+'/'+"tests.pak","a")
file.close()
file = open(username+'/'+"tests.pak","r")
score = 0
for line in file:
    print(line)
    score = int(line)
score = score +1
if score == (3):
    print("You have completed 3 tests!")
    time.sleep(1)
    print("Here is your average score!")
    file = open(username+'/'+"scores.pak","r")
    total = 0
    for line in file:
        total = total + int(line)
    mean = total/3
    print ("You got an average of "+str(mean))
    score = 0
    input()
    file.close()
    os.remove(username+'/'+"tests.pak")
    os.remove(username+'/'+"scores.pak")
file = open(username+'/'+"tests.pak","w+")
file.write(str(score))
file.close()
