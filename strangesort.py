alist = [23,121,11,9,69,420,42,1,12,47]
sorted = []
while len(alist) > 0:
    for item in alist:
        count = 0
        for item2 in alist:
            if not item == item2:
                if item < item2:
                    count += 1
        if count == (len(alist)-1):
            alist.remove(item)
            sorted.append(item)
print(sorted)