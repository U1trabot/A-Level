import thorpy, pygame
pygame.init()
canvas = pygame.display.set_mode((800,600))
oName = thorpy.Inserter(name="",value="Object Name",size=(100,30))
oColour = thorpy.ColorSetter("Object Colour",value=(128,128,128))
oVHeading = thorpy.make_text("Object Attributes",15)
attributes = [
    ["Mass",10,False],
    ["XAcceleration",10,False],
    ["YAcceleration",10,False],
    ["XVelocity",10,False],
    ["YVelocity",10,False],
    ["XLocation",10,False],
    ["YLocation",10,False],
    ["Shape",10,False],
    ["Size",10,False],
    ["XLength",10,False],
    ["YLength",10,False],
    ]
base = thorpy.Background(elements=[oName,oColour,oVHeading],color=(100,100,100))
for value in attributes:
   aValue = thorpy.Inserter(name=value[0],value=str(value[1]),size=(50,20))
   aFrozen = thorpy.Checker(value=value[2])
   aHost = thorpy.Box(elements=[aValue,aFrozen],size=(180,20))
   thorpy.store(aHost,mode="h")
   base.add_element(aHost)
thorpy.store(base,mode="v")
menu = thorpy.Menu(base)
menu.play()