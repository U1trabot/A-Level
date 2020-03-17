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
    def binToHexConv(self):
        dec = random.randint(0,255)
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
        print("Convert",binaryStr,"to hexadecimal")
        answer = input(">>> ")
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
        hex = str(first)+str(second)
        if answer == hex:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",hex)
            return False
    def hexToBinConv(self):
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
            hex = str(first)+str(second)
            print("Convert",hex,"to binary")
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
            if answer == binaryStr:
                print("Correct")
                return True
            else:
                print("Incorrect")
                print("The answer was",binaryStr)
                return False
    def hexToDecConv(self):
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
        hex = str(first)+str(second)
        print("Convert",hex,"to decimal")
        answer = input(">>> ")
        if answer == str(dec):
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",dec)
            return False
    def subtraction(self):
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
        binaryStr1 = "".join(map(str,binary1))
        binaryStr2 = "".join(map(str,binary2))
        print("Subtract",binaryStr1,"from",binaryStr2)
        calc = num2 - num1
        num = calc
        binaryOut = []
        for x in range (9):
            power = 2**(8-x)
            if x == 0:
                power = -power
            if num - power >= 0:
                num -= power
                binaryOut.append(1)
            else:
                binaryOut.append(0)
        answer = input(">>> ")
        binaryStrOut = "".join(map(str,binaryOut))
        if answer == binaryStrOut:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",binaryStrOut)
    def negToBin(self):
        num = random.randint(-256,0)
        print("Convert",num,"to a signed binary number")
        binaryOut = []
        for x in range (9):
            power = 2**(8-x)
            if x == 0:
                power = -power
            if num - power >= 0:
                num -= power
                binaryOut.append(1)
            else:
                binaryOut.append(0)
        answer = input(">>> ")
        binaryStr = "".join(map(str,binaryOut))
        if answer == binaryStr:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",binaryStr)
            return False
    def binToNeg(self):
        number = random.randint(-256,0)
        num = number
        binaryOut = []
        for x in range (9):
            power = 2**(8-x)
            if x == 0:
                power = -power
            if num - power >= 0:
                num -= power
                binaryOut.append(1)
            else:
                binaryOut.append(0)
        binaryStr = "".join(map(str,binaryOut))
        print("Convert",binaryStr,"to a negative decimal")
        answer = input(">>> ")
        if answer == str(number):
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",number)
            return False
    def fixToBin(self):
        number = round(random.uniform(0, 15.9375),4)
        numberStr = str(number)
        numberList = numberStr.split(".")
        integers = int(numberList[0])
        decimals = float("0."+numberList[1])
        num = integers
        binaryInt = []
        for x in range(4):
            power  = 2**(3-x)
            if num - power >= 0:
                num -= power
                binaryInt.append(1)
            else:
                binaryInt.append(0)
        binaryIntStr = "".join(map(str,binaryInt))
        num = (decimals)
        binaryDec = []

        for x in range(4):
            power  = (1/(2**(x+1)))
            if num - power >= 0:
                num -= power
                binaryDec.append(1)
            else:
                binaryDec.append(0)
        binaryDecStr = "".join(map(str,binaryDec))
        binary = binaryIntStr+binaryDecStr
        print("Convert",number,"to a fixed point, 8 bit, binary number (4bits.4bits)")
        answer = input(">>> ")
        if answer == binary:
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",binary)
            return False
    def binToFixed(self):
        number = 0.625*round(random.uniform(0, 15.9375)/0.0625)
        print(number)
        numberStr = str(number)
        numberList = numberStr.split(".")
        integers = int(numberList[0])
        decimals = float("0."+numberList[1])
        num = integers
        binaryInt = []
        for x in range(4):
            power  = 2**(3-x)
            if num - power >= 0:
                num -= power
                binaryInt.append(1)
            else:
                binaryInt.append(0)
        binaryIntStr = "".join(map(str,binaryInt))
        num = (decimals)
        binaryDec = []

        for x in range(4):
            power  = (1/(2**(x+1)))
            if num - power >= 0:
                num -= power
                binaryDec.append(1)
            else:
                binaryDec.append(0)
        binaryDecStr = "".join(map(str,binaryDec))
        binary = binaryIntStr+binaryDecStr
        print("Convert the fixed point binary number:",binary,"to a decimal number")
        answer = input(">>> ")
        if answer == str(number):
            print("Correct")
            return True
        else:
            print("Incorrect")
            print("The answer was",number)
            return False
Question().binToFixed()