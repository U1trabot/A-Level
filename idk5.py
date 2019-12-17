answer = 0
column = 8
while not (column < 1):
    print("Enter bit value: ")
    bit = int(input())
    answer = answer + (column*bit)
    column = column/2
print("Decimal value is: ")
print(answer)