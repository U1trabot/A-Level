Names = list()
Names.append("Ben")
Names.append("Thor")
Names.append("Zoe")
Names.append("Kate")
Max = 4
Current = 1
Found = False
print("What player are you looking for?")
PlayerName = input()
Current = 0
while not Found and Current <= Max:
  if Names[Current] == PlayerName:
    Found = True
  else:
    Current = Current + 1
if Found:
  print("Yes, they have a top score")
else:
  print("No, they do not have a top score")
if PlayerName == "Thor":
    print("Welcome Strongest Avenger")
    print("UUH WHAT")