#Number Wording Quiz
#Adam Baker
import random, tools, time #Imports Modules And Tools.py

wins = 0 #Creates Variable for how many questions they got right

file = open("data.pak" ,"a") #Creates data.pak file if it doesn't already exist
file.close()

correct = list() #Grabs all data from data.pak and puts it in list variable
file = open("data.pak", "r")
for line in file:
    correct.append(line)
file.close()

def questGen(): #Defines the system for generating and asking a question
    global correct
    global wins
    digits = random.randint(0,9999) #picks a random number smaller than 10,000 and larger than -1
    for item in correct: #Checks if number has been correct before
        if item == digits:
            questGen() #Gets a new number
        else:
            break #Continues the question generation
    words = tools.convert(digits) #Converts Number to Words
    text = "Write: |"+words+"| as a number! "
    question = int(input(text)) #Asks The Question
    if question == digits:
        print("You got it right!")
        wins = wins + 1 #adds a score to the variable
        file = open("data.pak", "a") #Saves Question To data.pak as it was answered correctly
        file.write(str(digits)+",")
        file.close()
    elif question != digits:
        print("You got it wrong!") #User got it wrong so question can still be asked, no score is added
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
file = open("scores.pak","a")
file.write(str(wins)+",")
file.close()
file = open("tests.pak","a")
file.close()
file = open("tests.pak","r")
score = 0
for line in file:
    print(line)
    score = int(line)
score = score +1
file.close()
file = open("tests.pak","w")
file.write(str(score))
file.close()
