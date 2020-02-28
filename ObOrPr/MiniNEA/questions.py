import random
class Question:
    def __init__(self):
        pass
    def addition(self):
        num1 = random.randint(0,255)
        num2 = random.randint(0,255)

        num = num1
        binary1 = []

        for x in range(8):
            power  = 2**(7-x)
            if num - power >= 0:
                num -= power
                binary1.append(1)
            else:
                binary1.append(0)
        num = num2
        binary2 = []


        for x in range(8):
            power = 2**(7-x)
            if num - power >= 0:
                num-= power
                binary2.append(1)
            else:
                binary2.append(0)

        print("Add the binary numbers","".join(map(str,binary1)),"and","".join(map(str,binary2)))
        answer = input(">>> ")
        numOut = num1 + num2
        num = numOut
        binaryOut = []
        for x in range(9):
            power = 2**(8-x)
            if num - power >= 0:
                num-= power
                binaryOut.append(1)
            else:
                binaryOut.append(0)
        answerList = []
        for char in answer:
            try:
                answerList.append(int(char))
            except:
                pass
        if len(answerList) == 8:
            answerList.insert(0, 0)
        if answerList == binaryOut:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was","".join(map(str,binaryOut)))
            return False
    def decToBinConv(self):
        dec = random.randint(0,255)
        print("Conver",dec,"to binary")
        num = dec
        binary = []

        for x in range(8):
            power  = 2**(7-x)
            if num - power >= 0:
                num -= power
                binary.append(1)
            else:
                binary.append(0)
        binaryStr = "".join(map(str,binary))
        answer = input(">>> ")
        if binaryStr == answer:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",binaryStr)
            return False
    def binToDecConv(self):
        dec  = random.randint(0,255)
        num = dec
        binary = []

        for x in range(8):
            power  = 2**(7-x)
            if num - power >= 0:
                num -= power
                binary.append(1)
            else:
                binary.append(0)
        binaryStr = "".join(map(str,binary))
        print("Convert",binaryStr,"to decimal")
        answer = input(">>> ")
        try:
            intAnswer = int(answer)
        except:
            intAnswer = (-1)
        if dec == intAnswer:
            print("Correct")
            return
        else:
            print("Incorrect")
            print("The answer was",dec)
            return False
    def decToHexConv(self):
        dec = random.randint(0,255)
        first = dec//16
        second = dec - (16*first)
        if first == (10):
            first = "A"
        elif first == (11):
            first = "B"
        elif first == (12):
            first = "C"
        elif first == (13):
            first = "D"
        elif first == (14):
            first ="E"
        elif first == (15):
            first = "F"
        if second == (10):
            second = "A"
        elif second == (11):
            second = "B"
        elif second == (12):
            second = "C"
        elif second == (13):
            second = "D"
        elif second == (14):
            second ="E"
        elif second == (15):
            second = "F"
        print("Convert",dec,"to hexadecimal")
        answer = input(">>> ")
        hex = str(first)+str(second)
        if answer == hex:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",hex)
            return False