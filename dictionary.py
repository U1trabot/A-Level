

dictionary = {
"Name" : "Tom",
"Gender" : "Unknown",
"Age" : "17",
"Occupation" : "White Hat Hacker",
"Age Of Death" : "42069"
}

type = str(input("What do you want to know about Tom? [Name],[Gender],[Age],[Occupation],[Age Of Death]: "))
print()
try:
    print(dictionary[type])
except:
    pass