def format_text(mystring):
    mystring = mystring.strip()
    mystring = mystring.lower()
    return mystring
mylist = []
end = False
while not end:
    next_item = format_text(input("Please enter an item or 'END' to finish: "))
    if next_item != 'end':
        mylist.append(next_item)
    else:
        end = True