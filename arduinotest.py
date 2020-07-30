temp = int(input("> "))

colours = ["dark blue","light blue","turquiose","green","yellow","orange","red"]
temps = [0,10,15,20,25,30,40,50]
for temperature in temps:
    if temp >= temperature:
        location = (temps.index(temperature))
print(colours[location])
print()

blue = 5*(50-temp)
red = 5*temp
colour = [red,255,blue]
print(colour)
