import random, sys, time

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()


class Question:
    """Class For Housing Question Generation"""
    def __init__(self):
        pass #Has No Attributes
    def addition(self):
        """Generates An Addition Question"""
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

        type("Add the binary numbers "+"".join(map(str,binary1))+" and "+"".join(map(str,binary2))+". Input your answer as a 9 bit number")
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
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+"".join(map(str,binaryOut)))
            return False
    def decToBinConv(self):
        """Generates A Decimal To Binary Conversion Question"""
        dec = random.randint(0,255)
        type("Conver "+str(dec)+" to binary")
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
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+binaryStr)
            return False
    def binToDecConv(self):
        """Generates A Binary To Decimal Conversion Question"""
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
        type("Convert "+binaryStr+" to decimal")
        answer = input(">>> ")
        try:
            intAnswer = int(answer)
        except:
            intAnswer = (-1)
        if dec == intAnswer:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+str(dec))
            return False
    def decToHexConv(self):
        """Generates A Decimal To Hexadecimal Conversion Question"""
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
        type("Convert "+str(dec)+" to hexadecimal")
        answer = input(">>> ")
        hex = str(first)+str(second)
        if answer.upper() == hex:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+hex)
            return False
    def binToHexConv(self):
        """Generates A Binary To Hexadecimal Conversion Question"""
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
        type("Convert "+binaryStr+" to hexadecimal")
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
        if answer.upper() == hex:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+hex)
            return False
    def hexToBinConv(self):
        """Generates A Hexadecimal To Binary Conversion Question"""
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
        type("Convert "+hex+" (Hex) to binary")
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
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+binaryStr)
            return False
    def hexToDecConv(self):
        """Generates A Hexadecimal To Decimal Conversion Question"""
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
        type("Convert "+hex+" (Hex) to decimal")
        answer = input(">>> ")
        if answer == str(dec):
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+str(dec))
            return False
    def subtraction(self):
        """Generates A Binary Subtraction Question"""
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
        type("Subtract "+binaryStr1+" from ",binaryStr2)
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
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+binaryStrOut)
    def negToBin(self):
        """Generates A Negative Decimal To Signed Binary Conversion Question"""
        num = random.randint(-256,0)
        type("Convert "+str(num)+" to a signed binary number")
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
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+binaryStr)
            return False
    def binToNeg(self):
        """Generates A Signed Binary To Negative Decimal Conversion Question"""
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
        type("Convert "+binaryStr+" to a negative decimal")
        answer = input(">>> ")
        if answer == str(number):
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+str(number))
            return False
    def fixToBin(self):
        """Generates A Fixed Point Decimal To Binary Conversion Question"""
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
        type("Convert "+str(number)+" to a fixed point, 8 bit, binary number (4bits.4bits)")
        answer = input(">>> ")
        if answer == binary:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+binary)
            return False
    def binToFixed(self):
        """Generates A Binary To Fixed Point Decimal Conversion Question"""
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
        type("Convert the fixed point binary number: "+binary+"to a decimal number")
        answer = input(">>> ")
        if answer == str(number):
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The answer was "+str(number))
            return False
    def floatToBin(self):
        """Generates A Floating Point Decimal To Binary Conversion Question"""
        number = 0.625*round(random.uniform(0,128)/0.625)
        if number < 1:
            number = 0.625*round(number/0.0625)
        elif number < 10:
            number = 0.125*round(number/0.125)
        elif number < 100:
            number = 0.25*round(number/0.25)
        else:
            number = 0.5*round(number/0.5)
        numberStr = str(number)
        numberList = numberStr.split(".")
        integers = int(numberList[0])
        decimals = float("0."+numberList[1])
        num = integers
        binaryInt = []
        for x in range(8):
            power  = 2**(7-x)
            if num - power >= 0:
                num -= power
                binaryInt.append(1)
            elif (1) in binaryInt:
                binaryInt.append(0)
        binaryIntStr = "".join(map(str,binaryInt))
        num = (decimals)
        binaryDec = []

        for x in range(8-len(binaryInt)):
            power  = (1/(2**(x+1)))
            if num - power >= 0:
                num -= power
                binaryDec.append(1)
            else:
                binaryDec.append(0)
        binaryDecStr = "".join(map(str,binaryDec))
        exponent = (len(binaryInt)-1)
        num = exponent
        binaryExp = []
        for x in range(3):
            power  = (2**(2-x))
            if num - power >= 0:
                num -= power
                binaryExp.append(1)
            else:
                binaryExp.append(0)
        binaryExpStr = "".join(map(str,binaryExp))
        solution = binaryIntStr+binaryDecStr+" "+binaryExpStr
        type("Convert the number "+str(number)+" to an 8 bit floating point binary number, with a 3 bit exponent. E.g. 45 = 10110100 101")
        answer = input(">>> ")
        if answer == solution:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The Answer was "+solution)
            return False
    def binToFloat(self):
        """Generates A Binary To Floating Point Decimal Conversion Question"""
        number = 0.625*round(random.uniform(0,128)/0.625)
        if number < 1:
            number = 0.625*round(number/0.0625)
        elif number < 10:
            number = 0.125*round(number/0.125)
        elif number < 100:
            number = 0.25*round(number/0.25)
        else:
            number = 0.5*round(number/0.5)
        numberStr = str(number)
        numberList = numberStr.split(".")
        integers = int(numberList[0])
        decimals = float("0."+numberList[1])
        num = integers
        binaryInt = []
        for x in range(8):
            power  = 2**(7-x)
            if num - power >= 0:
                num -= power
                binaryInt.append(1)
            elif (1) in binaryInt:
                binaryInt.append(0)
        binaryIntStr = "".join(map(str,binaryInt))
        num = (decimals)
        binaryDec = []

        for x in range(8-len(binaryInt)):
            power  = (1/(2**(x+1)))
            if num - power >= 0:
                num -= power
                binaryDec.append(1)
            else:
                binaryDec.append(0)
        binaryDecStr = "".join(map(str,binaryDec))
        exponent = (len(binaryInt)-1)
        num = exponent
        binaryExp = []
        for x in range(3):
            power  = (2**(2-x))
            if num - power >= 0:
                num -= power
                binaryExp.append(1)
            else:
                binaryExp.append(0)
        binaryExpStr = "".join(map(str,binaryExp))
        solution = binaryIntStr+binaryDecStr+" "+binaryExpStr
        type("Convert the number "+solution+" to a decimal number E.g. 10110100 101 = 45 ")
        answer = input(">>> ")
        if float(answer) == (number):
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The Answer was "+str(number))
            return False
    def multipleChoice(self):
        """Generates A Multiple Choice Question"""
        correct = [
        "ASCII Uses 7 Bits",
        "Unicode Uses Up To 48 Bits",
        "Parity Checks Are Used To Check That Recieved Data Is Correct",
        "In Majority Voting The Modal Bit Recieved Is Used",
        "Checksums Use Unique Algorithms To Check If Data Recieved Is Correct",
        "Checkdigits Are Specific Checksums That Product Only One Extra Digit",
        "Lossy Compression Loses Data When Compressing Files",
        "Lossless Compression Doesn't Lose Data When Compressing Files",
        "Run length encoding removes repeated information and replaces it with one occurrence of the repeated information aswell as the number of times it is repeated",
        "When a file is compressed with a dictionary-based method, a dictionary containing repeated data is appended to the file",
        "Encryption is the process of scrambling data so that it cannot be understood if intercepted",
        "Caesar ciphers encrypt information by replacing characters",
        "The Vernam cipher is an example of a one-time pad cipher. "
        ]
        incorrect = [
        "ASCII Uses 6 Bits",
        "Unicode Uses Up To 64 Bits",
        "Parity Checks Are Used To Check That Data Was Recieved",
        "In Majority Voting The Least Modal Bit Recieved Is Used",
        "Checksums Use Unique Algorithms To Check If Data Was Recieved",
        "Checkdigits Are Specific Checksums That Product Only Six Extra Digits",
        "Lossy Compression Doesn't Lose Data When Compressing Files",
        "Lossless Compression Loses Data When Compressing Files",
        "Run length encoding increases the size of a file",
        "When a file is compressed with a dictionary-based method, a dictionary containing repeated data is removed from the file",
        "Encryption is the process of unscrambling data so that it can be understood if intercepted",
        "Caesar ciphers are a type of food made by Caesar",
        "The Vernam cipher is a type of food made by Verman",
        "Hexadecimal is a fancy shape invented by a mathematician",
        "Binary is a base 4 number system",
        "Hexadecimal is a base 32 number system",
        "ASCII uses 12 bits",
        "When adding 1 and 1 the result is 1",
        "Compression makes files larger",
        "When the Modal bit recieved is used that is called Minority voting",
        "11 In Hexadecimal is F",
        "Unicode uses 128 bits",
        "Run length encoding is a form of Encryption",
        "The caesar cipher is an example of one-time pad cipher",
        "The Vernam cipher encrypts information by replacing characters",
        "There are no errors when data is transmitted from computer to computer",
        "Odd Parity works to make the number of 1s even",
        "Even Parity works to make the number of 1s odd",
        "When Majority voting is being used each bit is only transmitted once",
        "Checksums can correct errors",
        "With lossy compression file size can be reduced without impacting the quality of the file",
        "An XOR is not used in a Vernam Cipher",
        "No extra data needs to be added with dictionary-based compression",
        "Encrypted information is known as plaintext",
        "Unencrypted information is known as ciphertext",
        "The Vernam cipher uses a non-random key"
        ]
        letters = ["A","B","C","D"]
        correctLetter = random.choice(letters)
        letters.remove(correctLetter)
        output = [None,None,None,None]
        if correctLetter == "A":
            output[0] = "[A]"+" "+random.choice(correct)
        elif correctLetter == "B":
            output[1] = "[B]"+" "+random.choice(correct)
        elif correctLetter == "C":
            output[2] = "[C]"+" "+random.choice(correct)
        elif correctLetter == "D":
            output[3] = "[D]"+" "+random.choice(correct)
        for item in range(len(output)):
            if output[item] is None:
                incorrectans = random.choice(incorrect)
                if item == 0:
                    output[item] = "[A]"+" "+incorrectans
                elif item == 1:
                    output[item] = "[B]"+" "+incorrectans
                elif item == 2:
                    output[item] = "[C]"+" "+incorrectans
                elif item == 3:
                    output[item] = "[D]"+" "+incorrectans
                incorrect.remove(incorrectans)
        type("Input the letter of the true answer")
        for item in output:
            print(item)
        answer = input(">>> ")
        if answer.upper() == correctLetter:
            type("Correct")
            return True
        else:
            type("Incorrect")
            type("The correct answer was "+correctLetter)
            return False