ISBN = list()
for Count in range(0,13):
  print("Please enter next digit of ISBN: ")
  ISBN.append(input())
CalculatedDigit = 1
Count = 0
print(ISBN)
while Count:
    print(Count)
    CalculatedDigit = CalculatedDigit + int(ISBN[Count])
    Count = Count + 1
    CalculatedDigit = CalculatedDigit + int(ISBN[Count]) * 3
    Count = Count + 1
while CalculatedDigit >= 10:
  CalculatedDigit = CalculatedDigit - 10
CalculatedDigit = 10 - CalculatedDigit
if CalculatedDigit == 10:
  CalculatedDigit = 0
print(CalculatedDigit)
if CalculatedDigit == int(ISBN[12]):
   print("Valid ISBN")
else:
   print("Invalid ISBN")