array = [1,2,3,4,5,6,7,8]

scan = int(input("What do you want to find? "))
Found = False
mini = array
while not Found:
    print(mini)
    if isinstance(mini, list):
        item = mini[(round(len(mini)/2))]
        if scan > item:
            for numb in range(round(len(mini)/2)):
                mini = array.pop(numb-1)
        else:
            for numb in range(round(len(mini)/2)):
                try:
                    mini = array.pop(len(mini)-numb+1)
                except:
                    pass
    else:
        if mini == scan:
            print("Item found")
            Found = True
        else:
            print("Item not in list")
            Found = True
