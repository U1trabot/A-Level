alist = [23,121,11,9,69,420,42,11,1,12,47]
sorted = []
while len(alist) > 0:
    for item in alist:
        count = 0
        for item2 in alist:
            if item <= item2:
                count += 1
        if count == (len(alist)):
            alist.remove(item)
            sorted.append(item)
print(sorted)
