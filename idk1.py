print( "Enter a whole number: ")
Number1 = int(input())
print("Enter another whole number: ")
Number2 = int(input())
Temp1 = Number1
Temp2 = Number2
while Temp1 != Temp2:
    if Temp1 > Temp2:
        Temp1 -= Temp2
    else:
        Temp2 -= Temp1
Result = Temp1
print( Result, " is GCF of ", Number1, " and ", Number2)