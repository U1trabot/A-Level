#Caeser Cypher program

text = str(input("Input the string to be cyphered: "))
shift = int(input("Input the number of shifts: "))
def splitstr(stri):
    return list(stri)
textList = splitstr(text)
length = len(textList)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x = 0
for x in range (len(textList)):
    for i in range (len(alphabet)):
        if textList[x] == alphabet[i]:
            textList[x] = alphabet[i+shift]
            break
    x = 1
output = str()
for x in range (len(textList)):
    output = output+(textList[x])
print(output)