#ThorPy hello world tutorial : full code
import pygame, random, math, thorpy
pygame.init()

screenWidth = (1366)
screenHeight = (768)
mouseForce = 15
cursorMode = 'selection'
scale = 10
fonty = pygame.font.Font('freesansbold.ttf',20)
fonty2 = pygame.font.Font('freesansbold.ttf',48)
hidden = True
boxes = 0
timers = []
measureLines = []

selectionCursor, creationCursor, timerCursor, measureCursor, angleCursor, deletionCursor = 'selection_cursor.png', 'creation_cursor.png', 'timer_cursor.png', 'measure_cursor.png', 'angle_cursor.png', 'deletion_cursor.png'



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
                        self.xLocation += (((self.xVelocity+self.xVelocityDelayed)/2*rateOfTime)/120)*scale
                    else:
                        self.xVelocityDelayed = self.xVelocity
                        self.xVelocity = xM*0.5
                        self.xLocation = pygame.mouse.get_pos()[0]-self.xLength/2
                        self.xforce = self.mass * self.xVelocityDelayed - self.xVelocity
                elif attribute == "yLocation":
                    if not self.selected:
                        self.yLocation += (((self.yVelocity+self.yVelocityDelayed)/2*rateOfTime)/120)*scale
                    else:
                        self.yVelocityDelayed = self.yVelocityDelayed
                        self.yVelocity = yM*0.5
                        self.yLocation = pygame.mouse.get_pos()[1] -self.yLength/2
                        self.yforce = self.mass * self.yVelocityDelayed - self.yVelocity
                    if self.yLocation > screenHeight - self.yLength - 49:
                        self.yLocation = 2 * (screenHeight - self.yLength -49) - self.yLocation
                        self.yVelocity *= self.elasticity
                        self.xVelocity *= self.drag
                elif attribute == "xVelocity":
                    self.xVelocity += self.xAcceleration*rateOfTime/120
                elif attribute == "yVelocity":
                    self.yVelocity += self.yAcceleration*rateOfTime/120
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
                    self.xLength = self.xLength*self.size
                elif attribute == "yLength":
                    self.yLength = self.yLength*self.size
                elif attribute == "xVelocityDelayed":
                    self.xVelocityDelayed = self.xVelocity
                elif attribute == "yVelocityDelayed":
                    self.yVelocityDelayed = self.yVelocity
        self.size = 1
        self.visual = pygame.Rect(int(self.xLocation), int(self.yLocation), int(self.xLength), int(self.yLength))
        pygame.draw.rect(canvas, self.colour, self.visual)

instances = {}
box = Instance("Box",[random.randint(1,255),random.randint(1,255),random.randint(1,255)],10,screenWidth/2, screenHeight/2, 10,"Rect", 1, 100, 100)
instances[box.name] = box

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

oName = thorpy.Inserter(name="Name:",value="Object Name",size=(100,30))
oColour = thorpy.ColorSetter("Object Colour",value=(128,128,128))
oVHeading = thorpy.make_text("Object Attributes",15)
attributes = [
    ["Mass",permaSelection.mass,permaSelection.frozen["mass"],False],
    ["XAcceleration",permaSelection.xAcceleration,permaSelection.frozen["xAcceleration"],False],
    ["YAcceleration",permaSelection.yAcceleration,permaSelection.frozen["yAcceleration"],False],
    ["XVelocity",permaSelection.xVelocity,permaSelection.frozen["xVelocity"],False],
    ["YVelocity",permaSelection.yVelocity,permaSelection.frozen["yVelocity"],False],
    ["XLocation",permaSelection.xLocation,permaSelection.frozen["xLocation"],False],
    ["YLocation",permaSelection.yLocation,permaSelection.frozen["yLocation"],False],
    ["Shape",permaSelection.shape,permaSelection.frozen["shape"],False],
    ["Size",permaSelection.size,permaSelection.frozen["size"],False],
    ["XLength",permaSelection.xLength,permaSelection.frozen["xLength"],False],
    ["YLength",permaSelection.yLength,permaSelection.frozen["yLength"],False],
    ["XForce",permaSelection.xForce,True,False],
    ["YForce",permaSelection.yForce,True,False],
    ["Drag",permaSelection.drag,True,False]
    ]
base = thorpy.Background(elements=[oName,oColour,oVHeading],color=(255,255,255),image="object_panel.png",mode=None)
def disableChange(element):
    if element.get_text() == "Mass":
        attributes[0][3] = True
    elif element.get_text() == "XAcceleration":
        attributes[1][3] = True
    elif element.get_text() == "YAcceleration":
        attributes[2][3] = True
    elif element.get_text() == "XVelocity":
        attributes[3][3] = True
    elif element.get_text() == "YVelocity":
        attributes[4][3] = True
    elif element.get_text() == "XLocation":
        attributes[5][3] = True
    elif element.get_text() == "YLocation":
        attributes[6][3] = True
    elif element.get_text() == "Shape":
        attributes[7][3] = True
    elif element.get_text() == "Size":
        attributes[8][3] = True
    elif element.get_text() == "XLength":
        attributes[9][3] = True
    elif element.get_text() == "YLength":
        attributes[10][3] = True
    elif element.get_text() == "XForce":
        attributes[11][3] = True
    elif element.get_text() == "YForce":
        attributes[12][3] = True
    elif element.get_text() == "Drag":
        attributes[13][3] = True
def setAt(element,value):
    global rateOfTime
    if element.get_text() == "Mass":
        try:
            permaSelection.mass = float(value)
        except:
            pass
        attributes[0][3] = False
    elif element.get_text() == "XAcceleration":
        try:
            permaSelection.xAcceleration = float(value)
        except:
            pass
        attributes[1][3] = False
    elif element.get_text() == "YAcceleration":
        try:
            permaSelection.yAcceleration = float(value)
        except:
            pass
        attributes[2][3] = False
    elif element.get_text() == "XVelocity":
        try:
            permaSelection.xVelocity = float(value)
        except:
            pass
        attributes[3][3] = False
    elif element.get_text() == "YVelocity":
        try:
            permaSelection.yVelocity = float(value)
        except:
            pass
        attributes[4][3] = False
    elif element.get_text() == "XLocation":
        try:
            permaSelection.xLocation = float(value)
        except:
            pass
        attributes[5][3] = False
    elif element.get_text() == "YLocation":
        try:
            permaSelection.yLocation = float(value)
        except:
            pass
        attributes[6][3] = False
    elif element.get_text() == "Shape":
        try:
            permaSelection.shape = value
        except:
            pass
        attributes[7][3] = False
    elif element.get_text() == "Size":
        try:
            permaSelection.size = float(value)
        except:
            pass
        attributes[8][3] = False
    elif element.get_text() == "XLength":
        try:
            permaSelection.xLength = float(value)
        except:
            pass
        attributes[9][3] = False
    elif element.get_text() == "YLength":
        try:
            permaSelection.yLength = float(value)
        except:
            pass
        attributes[10][3] = False
    elif element.get_text() == "XForce":
        try:
            permaSelection.xForce = float(value)
        except:
            pass
        attributes[11][3] = False
    elif element.get_text() == "YForce":
        try:
            permaSelection.yForce = float(value)
        except:
            pass
        attributes[12][3] = False
    elif element.get_text() == "Drag":
        try:
            permaSelection.drag = float(value)
        except:
            pass
        attributes[13][3] = False
    elif element.get_text() == "Name:":
        try:
            permaSelection.name = value
        except:
            pass
    elif element.get_text() == "Rate:":
        try:
            rateOfTime = float(value)
        except:
            pass
def freeze(row):
    if row == (0):
        permaSelection.frozen["mass"] = not(permaSelection.frozen["mass"])
    elif row == (1):
        permaSelection.frozen["xAcceleration"] = not(permaSelection.frozen["xAcceleration"])
    elif row == (2):
        permaSelection.frozen["yAcceleration"] = not(permaSelection.frozen["yAcceleration"])
    elif row == (3):
        permaSelection.frozen["xVelocity"] = not(permaSelection.frozen["xVelocity"])
    elif row == (4):
        permaSelection.frozen["yVelocity"] = not(permaSelection.frozen["yVelocity"])
    elif row == (5):
        permaSelection.frozen["xLocation"] = not(permaSelection.frozen["xLocation"])
    elif row == (6):
        permaSelection.frozen["yLocation"] = not(permaSelection.frozen["yLocation"])
    elif row == (7):
        permaSelection.frozen["shape"] = not(permaSelection.frozen["shape"])
    elif row == (8):
        permaSelection.frozen["size"] = not(permaSelection.frozen["size"])
    elif row == (9):
        permaSelection.frozen["xLength"] = not(permaSelection.frozen["mxLength"])
    elif row == (10):
        permaSelection.frozen["yLength"] = not(permaSelection.frozen["yLength"])
for x in range(0,14):
   aValue = thorpy.Inserter(name=(attributes[x])[0],value=str((attributes[x])[1]),size=(50,20))
   aFrozen = thorpy.Checker(value=(attributes[x])[2])
   aFrozen.user_func = freeze
   aFrozen.user_params = {'row':x}
   aHost = thorpy.Box(elements=[aValue,aFrozen],size=(180,20))
   thorpy.store(aHost,mode="h")
   base.add_element(aHost)
def show():
    global hidden
    menu.set_elements(screenBack)
    menu.blit_and_update()
    menu.refresh()
    hidden = False
showTab, showTabHover = "open_tab.png", "open_tab_hover.png"
hideTab, hideTabHover = "close_tab.png", "close_tab_hover.png"
showButton = thorpy.make_image_button(showTab,None,showTabHover)
showButton.user_func = show
showButton.set_size((43,100))
showButton.set_center_pos((screenWidth-22,screenHeight/2))
def hide():
    global hidden
    menu.set_elements([showButton,bar])
    menu.blit_and_update()
    menu.refresh()
    hidden = True
hideButton = thorpy.make_image_button(hideTab,None,hideTabHover)
hideButton.user_func = hide
hideButton.set_size((43,100))
base.add_element(hideButton)
def selectionClick():
    global cursorMode, cursor_picture
    cursorMode = 'selection'
    cursor_picture = pygame.image.load(selectionCursor).convert_alpha()
def creationClick():
    global cursorMode, creating, cursor_picture
    cursorMode = 'creation'
    creating = False
    cursor_picture = pygame.image.load(creationCursor).convert_alpha()
def timerClick():
    global cursorMode, cursor_picture
    cursorMode = 'timer'
    cursor_picture = pygame.image.load(timerCursor).convert_alpha()
def measureClick():
    global cursorMode, measuring, cursor_picture
    cursorMode = 'measure'
    measuring = False
    cursor_picture = pygame.image.load(measureCursor).convert_alpha()
def angleClick():
    global cursorMode, cursor_picture
    cursorMode = 'angle'
    cursor_picture = pygame.image.load(angleCursor).convert_alpha()
def deletionClick():
    global cursorMode, cursor_picture
    cursorMode = 'deletion'
    cursor_picture = pygame.image.load(deletionCursor).convert_alpha()
def blankClick():
    global instances
    instances = {}
def playPause():
    pass
timeDisplay = thorpy.Inserter(name="Rate:",value_type=float,size=(60,45),value="1")
selection, creation, timer, measure, angle_measure, deletion, blank = "selection.png", "creation.png", "timer.png", "measure.png", "angle_measure.png", "deletion.png", "blank.png"
selectionH, creationH, timerH, measureH, angle_measureH, deletionH, blankH = "selection_hover.png", "creation_hover.png", "timer_hover.png", "measure_hover.png", "angle_measure_hover.png", "deletion_hover.png", "blank_hover.png"
sTool, cTool, tTool, mTool, aTool, dTool, bTool = thorpy.make_image_button(selection,img_hover=selectionH),thorpy.make_image_button(creation,img_hover=creationH),thorpy.make_image_button(timer,img_hover=timerH),thorpy.make_image_button(measure,img_hover=measureH),thorpy.make_image_button(angle_measure,img_hover=angle_measureH),thorpy.make_image_button(deletion,img_hover=deletionH),thorpy.make_image_button(blank,img_hover=blankH)
sTool.user_func = selectionClick
cTool.user_func = creationClick
tTool.user_func = timerClick
mTool.user_func = measureClick
aTool.user_func = angleClick
dTool.user_func = deletionClick
bTool.user_func = blankClick
play, playH, pause, pauseH = "play.png","play_hover.png","pause.png","pause_hover.png"
timePause = thorpy.make_image_button(pause,img_hover=pauseH)
timePause.user_func = playPause
settings,settingsH  = "settings.png", "settings_hover.png"
settingsButton = thorpy.make_image_button(settings,img_hover=settingsH)
bar = thorpy.Box(elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool, settingsButton, timePause, timeDisplay],size=(screenWidth,50))
bar.set_main_color(color=[100,100,100])
thorpy.store(bar,mode="h",align="center",gap=50,margin=350,elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool])
thorpy.store(bar,mode="h",align="center",margin=-600,elements=[settingsButton, timePause, timeDisplay])
screenBack = thorpy.Background(elements=[base,bar],color=[255,255,255,0],mode="scale to screen")
thorpy.store(base,mode="v",align=("center"),y=0)
hideButton.set_center_pos((-22,screenHeight/2))
thorpy.store(screenBack,mode="v",x=screenWidth/2,y=(screenHeight-54),elements=[bar])
thorpy.store(screenBack,mode="v",align="right",x=screenWidth,y=-5,elements=[base])
menu = thorpy.Menu([showButton,bar],fps=120)

time = pygame.time.Clock()
stopwatch = 0.00
stopwatch_pause = True
rateOfTime = 1
run = True
selection = None
pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
cursor_picture = pygame.image.load(selectionCursor).convert_alpha()
while run:
    time.tick(rateOfTime*120)
    if not stopwatch_pause:
        stopwatch += (rateOfTime*120)
    canvas.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'selection':
            clickbox = pygame.Rect(event.pos[0]-10, event.pos[1]-10, 20, 20)
            pygame.draw.rect(canvas, [255,255,255], clickbox)
            for instance in instances:
                if clickbox.colliderect(instances[instance].visual):
                    instances[instance].selected = True
                    selection = instances[instance]
                    permaSelection = instances[instance]
                    base._elements[0].set_value(permaSelection.name)
                    base._elements[1].set_value(permaSelection.colour)
                    if not hidden:
                        menu.set_elements(screenBack)
                        menu.blit_and_update()
                        menu.refresh()
                    break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'creation':
            creating = True
            startPos = event.pos
            moved = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'measure':
            measuring = True
            startPosM = event.pos
            movedM = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and cursorMode == "timer":
            newLine = pygame.Rect(pygame.mouse.get_pos()[0],0,4,screenHeight)
            timers.append([newLine,None])
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and cursorMode == "timer":
            stopwatch = 0.0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p and cursorMode == "timer":
            stopwatch_pause = not(stopwatch_pause)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and cursorMode == "timer":
            timers = []
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and cursorMode == "measure":
            measureLines = []
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'selection':
            for instance in instances:
                if instances[instance].selected:
                    instances[instance].selected = False
                    selection = None
        if event.type == pygame.MOUSEMOTION and cursorMode == 'selection':
            xM = event.rel[0]
            yM = event.rel[1]
        if event.type == pygame.MOUSEMOTION and cursorMode == 'creation' and creating:
            xDis = -(startPos[0] - event.pos[0])
            yDis = -(startPos[1] - event.pos[1])
            example = pygame.Rect(startPos[0],startPos[1],xDis,yDis)
            moved = True
        if event.type == pygame.MOUSEMOTION and cursorMode == 'measure' and measuring:
            xDisM = -(startPosM[0] - event.pos[0])
            yDisM = -(startPosM[1] - event.pos[1])
            tDisM = math.hypot(xDisM,yDisM)/scale
            measure_line = [startPosM,[event.pos[0],event.pos[1]]]
            movedM = True
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'creation' and creating:
            creating = False
            if moved:
                boxes += 1
                spawn = Instance("New Box "+str(boxes),[random.randint(1,255),random.randint(1,255),random.randint(1,255)],10,startPos[0], startPos[1], 10,"Rect", 1, xDis, yDis)
                instances[spawn.name] = spawn
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'measure' and measuring:
            measuring = False
            if movedM:
                measure_line.append(tDisM)
                measure_line.append(startPosM)
                measure_line.append([xDisM,yDisM])
                measureLines.append(measure_line)
                measure_line = None
        if event.type == pygame.MOUSEBUTTONDOWN and cursorMode == "deletion":
            clickbox = pygame.Rect(event.pos[0]-10, event.pos[1]-10, 20, 20)
            pygame.draw.rect(canvas, [255,255,255], clickbox)
            toBeDeleted = []
            for instance in instances:
                if clickbox.colliderect(instances[instance].visual):
                    toBeDeleted.append(instance)
            for item in toBeDeleted:
                del instances[item]
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_PRESS:
            disableChange(event.el)
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_INSERT:
            setAt(event.el,event.value)
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_SLIDE:
            permaSelection.colour = oColour.get_color()
        menu.react(event)
    for item in instances:
        for item2 in instances:
            if instances[item] != instances[item2]:
                collide(instances[item],instances[item2])
        instances[item].recalibrate()
    pygame.draw.rect(canvas, [255,0,0,255], permaSelection.visual,3)
    clicked = []
    for row in attributes:
        clicked.append(row[3])
    attributes = [
        ["Mass",round(permaSelection.mass,2),permaSelection.frozen["mass"],clicked[0]],
        ["XAcceleration",round(permaSelection.xAcceleration,2),permaSelection.frozen["xAcceleration"],clicked[1]],
        ["YAcceleration",round(permaSelection.yAcceleration,2),permaSelection.frozen["yAcceleration"],clicked[2]],
        ["XVelocity",round(permaSelection.xVelocity,2),permaSelection.frozen["xVelocity"],clicked[3]],
        ["YVelocity",round(permaSelection.yVelocity,2),permaSelection.frozen["yVelocity"],clicked[4]],
        ["XLocation",round(permaSelection.xLocation,2),permaSelection.frozen["xLocation"],clicked[5]],
        ["YLocation",round(permaSelection.yLocation,2),permaSelection.frozen["yLocation"],clicked[6]],
        ["Shape",permaSelection.shape,permaSelection.frozen["shape"],clicked[7]],
        ["Size",round(permaSelection.size,2),permaSelection.frozen["size"],clicked[8]],
        ["XLength",round(permaSelection.xLength,2),permaSelection.frozen["xLength"],clicked[9]],
        ["YLength",round(permaSelection.yLength,2),permaSelection.frozen["yLength"],clicked[10]],
        ["XForce",permaSelection.xForce,True,clicked[11]],
        ["YForce",permaSelection.yForce,True,clicked[12]],
        ["Drag",permaSelection.drag,True,clicked[13]]
        ]
    for x in range(4,16):
        if not attributes[x-3][3]:
            base._elements[x]._elements[0].set_value(str(attributes[x-3][1]))
        base._elements[x]._elements[1].set_value(attributes[x-3][2])
    if cursorMode == 'creation' and creating:
        try:
            pygame.draw.rect(canvas,[100,100,100], example)
        except:
            pass
    for line in timers:
        pygame.draw.rect(canvas,[0,0,0],line[0])
    for line in measureLines:
        pygame.draw.aaline(canvas,[15,15,15],line[0],line[1])
        line_distance = fonty.render(str(round(line[2],2)),False,[15,15,15])
        canvas.blit(line_distance,(int(line[4][0]/2+line[3][0]),int(line[4][1]/2+line[3][1])))

    try:
        pygame.draw.aaline(canvas,[15,15,15],measure_line[0],measure_line[1])
        line_distance_fresh = fonty2.render(str(round(tDisM,2)),False,[15,15,15])
        canvas.blit(line_distance_fresh,(int(screenWidth/2),int(screenHeight/2)))
        #xDisM/2+startPosM[0] yDisM/2+startPos[1]
    except:
        pass
    if cursorMode == 'selection':
        pygame.draw.rect(canvas, [255,0,0,255], sTool.get_fus_rect(),3)
    elif cursorMode == 'creation':
        pygame.draw.rect(canvas, [255,0,0,255], cTool.get_fus_rect(),3)
    stopwatch_text = fonty2.render(str(stopwatch/12000),False,[0,0,0])
    canvas.blit(stopwatch_text,(int(screenWidth/2),0))
    menu.blit_and_update()
    menu.refresh()
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    canvas.blit(cursor_picture, pygame.mouse.get_pos())
    pygame.display.update()
