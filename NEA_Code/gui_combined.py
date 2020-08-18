#ThorPy hello world tutorial : full code
import pygame, random, math, thorpy
pygame.init()

screenWidth = (1366)
screenHeight = (768)
mouseForce = 15
scale = 10
fonty = pygame.font.Font('freesansbold.ttf',20)

class Instance():
    #Main class for all objects within the simulation
    global xM
    global yM
    global mouseForce
    global scale
    def __init__(self,name="New Object",colour=[255,255,255],density=10,xpos=0,ypos=0,mass=10,shape="blank",size=1,xLength=1,yLength=1,thickness=1,youngs=1000,refractive=99999999,roughness=99999999):
        #Defines the attributes for the object
        self.frozen = {
            "mass":False,
            "xAcceleration":False,
            "yAcceleration":False,
            "xVelocity":False,
            "yVelocity":False,
            "xLocation":False,
            "yLocation":False,
            "shape":False,
            "size":False,
            "xLength":False,
            "yLength":False,
            "xVelocityDelayed":False,
            "yVelocityDelayed":False
            }
        self.xLocation = xpos
        self.yLocation = ypos
        self.xVelocity = 0
        self.yVelocity = 0
        self.xVelocityDelayed = 0
        self.yVelocityDelayed = 0
        self.xAcceleration = 0
        self.yAcceleration = 0
        self.shape = shape
        self.shapeOriginial = self.shape
        self.size = size
        self.xLength = xLength
        self.yLength = yLength
        self.thickness = thickness
        self.reIndex = refractive
        self.YoModulus = youngs
        self.density = density
        self.mass = self.size*self.density
        self.xForce = 0
        self.yForce =  0
        self.roughness = roughness
        self.colour = colour
        self.name = name
        self.visual = pygame.Rect(int(self.xLocation), int(self.yLocation), int(self.xLength), int(self.yLength))
        self.selected = False
        self.drag = 0.98
        self.elasticity = 0.75
        self.xforce = 0
        self.yforce = 0
    def recalibrate(self):
        #Method for resetting variables (unless frozen)
        for attribute in self.frozen:
            if not self.frozen[attribute]:
                if attribute == "xLocation":
                    if not self.selected:
                        self.xLocation += (((self.xVelocity+self.xVelocityDelayed)/2)/120)*scale
                    else:
                        self.xVelocityDelayed = self.xVelocity
                        self.xVelocity = xM*0.5
                        self.xLocation += ((((self.xVelocity+self.xVelocityDelayed)/2)/120))*mouseForce
                        self.xforce = self.mass * self.xVelocityDelayed - self.xVelocity
                elif attribute == "yLocation":
                    if not self.selected:
                        self.yLocation += (((self.yVelocity+self.yVelocityDelayed)/2)/120)*scale
                    else:
                        dy = event.pos[1] - self.yLocation
                        self.yVelocityDelayed = self.yVelocityDelayed
                        self.yVelocity = yM*0.5
                        self.yLocation += ((((self.yVelocity+self.yVelocityDelayed)/2)/120))*mouseForce
                        self.yforce = self.mass * self.yVelocityDelayed - self.yVelocity
                    if self.yLocation > screenHeight - self.yLength:
                        self.yLocation = 2 * (screenHeight - self.yLength) - self.yLocation
                        self.yVelocity *= self.elasticity
                        self.xVelocity *= self.drag
                elif attribute == "xVelocity":
                    self.xVelocity += self.xAcceleration/120
                elif attribute == "yVelocity":
                    self.yVelocity += self.yAcceleration/120
                elif attribute == "xAcceleration":
                    self.xAcceleration = self.xForce/self.mass
                elif attribute == "yAcceleration":
                    self.yAcceleration = (self.yForce + self.mass*9.81)/self.mass
                elif attribute == "mass":
                    self.mass = self.density*self.size
                elif attribute == "shape":
                    self.shape = self.shape
                elif attribute == "size":
                    self.size = self.size
                elif attribute == "xLength":
                    self.xLength = self.xLength
                elif attribute == "yLength":
                    self.yLength = self.yLength
                elif attribute == "xVelocityDelayed":
                    self.xVelocityDelayed = self.xVelocity
                elif attribute == "yVelocityDelayed":
                    self.yVelocityDelayed = self.yVelocity
        self.visual = pygame.Rect(int(self.xLocation), int(self.yLocation), int(self.xLength), int(self.yLength))
        pygame.draw.rect(canvas, self.colour, self.visual)

instances = {}
for n in range(random.randint(11,15)):
    xsize = random.randint(10, 100)
    ysize = random.randint(10, 100)
    x = random.randint(0, screenWidth - xsize)
    y = random.randint(0, screenHeight - ysize)
    box = Instance("Box"+str(n),[random.randint(1,255),random.randint(1,255),random.randint(1,255)],10,x, y, 10,"blank", 1, xsize, ysize)
    overlap = False
    for item in instances:
        if (instances[item].xLocation < (box.xLocation + box.xLength) and instances[item].xLocation > box.xLocation) or (instances[item].yLocation < (box.yLocation + box.yLength) and instances[item].yLocation > box.yLocation):
            overlap = True
    if not overlap:
        instances[box.name] = box
    else:
        n -= 1

def collide(i1,i2):
    if i1.visual.colliderect(i2.visual):
        try:
            (i1.xVelocity,i2.xVelocity) = (i2.xVelocity,i1.xVelocity)
            (i1.yVelocity,i2.yVelocity) = (0,0)
            (i1.yVelocityDelayed,i2.yVelocityDelayed) = (0,0)
            (i1.yForce,i2.yForce) = (-i1.mass*9.81,-i2.mass*9.81)
            i1.xVelocity *= i1.drag
            i2.xVelocity *= i2.drag
            if i1.yVelocity < 0:
                i1.yLocation -= 1
                i2.yLocation += 1
            else:
                i1.yLocation += 1
                i2.yLocation -= 1
            if i1.xVelocity < 0:
                i1.xLocation -= 1
                i2.xLocation += 1
            else:
                i1.xLocation += 1
                i2.xLocation -= 1

        except:
            pass
    else:
        (i1.yForce,i2.yForce) = (0,0)
permaSelection = instances[random.choice(list(instances))]
canvas = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Simulation Space")
canvas.fill([255,255,255])

oName = thorpy.Inserter(name="",value="Object Name",size=(100,30))
oColour = thorpy.ColorSetter("Object Colour",value=(128,128,128))
oVHeading = thorpy.make_text("Object Attributes",15)
attributes = [
    ["Mass",permaSelection.mass,permaSelection.frozen["mass"]],
    ["XAcceleration",permaSelection.xAcceleration,permaSelection.frozen["xAcceleration"]],
    ["YAcceleration",permaSelection.yAcceleration,permaSelection.frozen["yAcceleration"]],
    ["XVelocity",permaSelection.xVelocity,permaSelection.frozen["xVelocity"]],
    ["YVelocity",permaSelection.yVelocity,permaSelection.frozen["yVelocity"]],
    ["XLocation",permaSelection.xLocation,permaSelection.frozen["xLocation"]],
    ["YLocation",permaSelection.yLocation,permaSelection.frozen["yLocation"]],
    ["Shape",permaSelection.shape,permaSelection.frozen["shape"]],
    ["Size",permaSelection.size,permaSelection.frozen["size"]],
    ["XLength",permaSelection.xLength,permaSelection.frozen["xLength"]],
    ["YLength",permaSelection.yLength,permaSelection.frozen["yLength"]]
    ]
base = thorpy.Background(elements=[oName,oColour,oVHeading],color=(255,255,255),image="object_panel.png",mode=None)
for x in range(0,11):
   aValue = thorpy.Inserter(name=(attributes[x])[0],value=str((attributes[x])[1]),size=(50,20))
   aFrozen = thorpy.Checker(value=(attributes[x])[2])
   aHost = thorpy.Box(elements=[aValue,aFrozen],size=(180,20))
   thorpy.store(aHost,mode="h")
   base.add_element(aHost)
def show():
    menu.set_elements(screenBack)
    menu.blit_and_update()
    menu.refresh()
showButton = thorpy.make_button("Show",show)
def hide():
    menu.set_elements(showButton)
    menu.blit_and_update()
    menu.refresh()
hideButton = thorpy.make_button("Hide",hide)
base.add_element(hideButton)
screenBack = thorpy.Background(elements=[base],color=[255,255,0,10],mode="scale to screen")
thorpy.store(base,mode="v",align=("center"),y=0)
thorpy.store(screenBack,mode="v",align="right",x=screenWidth,y=-5,)
menu = thorpy.Menu(showButton,fps=120)

time = pygame.time.Clock()
rateOfTime = 1
run = True
selection = None
totalforce = 0
pygame.display.toggle_fullscreen()
while run:
    time.tick(rateOfTime*120)
    canvas.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clickbox = pygame.Rect(event.pos[0]-10, event.pos[1]-10, 20, 20)
            pygame.draw.rect(canvas, [255,255,255], clickbox)
            for instance in instances:
                if clickbox.colliderect(instances[instance].visual):
                    instances[instance].selected = True
                    selection = instances[instance]
                    permaSelection = instances[instance]
                    menu.set_elements(screenBack)
                    menu.blit_and_update()
                    menu.refresh()
                    break
        if event.type == pygame.MOUSEBUTTONUP:
            for instance in instances:
                if instances[instance].selected:
                    instances[instance].selected = False
                    selection = None
        if event.type == pygame.MOUSEMOTION:
            xM = event.rel[0]
            yM = event.rel[1]
        menu.react(event)
    try:
        pygame.draw.aaline(canvas, [255,0,0], pygame.mouse.get_pos(), [selection.xLocation+(selection.xLength/2),selection.yLocation+(selection.yLength/2)])
        totalforce = round(math.hypot(selection.xforce/scale,selection.yforce/scale),2)
        text = fonty.render(str(totalforce)+"N",False,[0,0,0])
        canvas.blit(text,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+10))
    except:
        text = fonty.render(str(totalforce)+"N",True,[0,0,0])
        canvas.blit(text,(pygame.mouse.get_pos()[0]+5,pygame.mouse.get_pos()[1]+10))
    for item in instances:
        for item2 in instances:
            if instances[item] != instances[item2]:
                collide(instances[item],instances[item2])
        instances[item].recalibrate()
    pygame.draw.rect(canvas, [255,0,0,255], permaSelection.visual,3)
    attributes = [
        ["Mass",round(permaSelection.mass,2),permaSelection.frozen["mass"]],
        ["XAcceleration",round(permaSelection.xAcceleration,2),permaSelection.frozen["xAcceleration"]],
        ["YAcceleration",round(permaSelection.yAcceleration,2),permaSelection.frozen["yAcceleration"]],
        ["XVelocity",round(permaSelection.xVelocity,2),permaSelection.frozen["xVelocity"]],
        ["YVelocity",round(permaSelection.yVelocity,2),permaSelection.frozen["yVelocity"]],
        ["XLocation",round(permaSelection.xLocation,2),permaSelection.frozen["xLocation"]],
        ["YLocation",round(permaSelection.yLocation,2),permaSelection.frozen["yLocation"]],
        ["Shape",permaSelection.shape,permaSelection.frozen["shape"]],
        ["Size",round(permaSelection.size,2),permaSelection.frozen["size"]],
        ["XLength",round(permaSelection.xLength,2),permaSelection.frozen["xLength"]],
        ["YLength",round(permaSelection.yLength,2),permaSelection.frozen["yLength"]]
        ]
    for x in range(4,14):
        base._elements[x]._elements[0].set_value(str(attributes[x-3][1]))
        base._elements[x]._elements[1].set_value(attributes[x-3][2])
    base._elements[0].set_value(permaSelection.name)
    base._elements[1].set_value(permaSelection.colour)
    menu.blit_and_update()
    pygame.display.update()
