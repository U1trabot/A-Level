import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hides the default pygame welcome promt
import pygame, random, math, thorpy #Imports the required python modules. pygame for rendering the simulation, thorpy for the GUI, math for the calculations and random for random number generation
pygame.init() #Initialises pygame

screenWidth = (1366) #Sets variables for the screen size
screenHeight = (768)

cursorMode = 'selection' #Creates variable for cursor mode, and sets it to the default
scale = 10 #Creates varible for scale, and sets it to the default value
fonty = pygame.font.Font('freesansbold.ttf',20) #Creates the smaller font for rendering distance and other text
fonty2 = pygame.font.Font('freesansbold.ttf',48) #Creates the larger font for rendering time and other text
hidden = True #Creates the variable for if the object panel is hidden, and sets it to the default value
settingsShown = False #Creates the varible for if the settings menu is shown, and sets it to the default value
boxes = 0 #Creates the variable for the number of boxes, and sets it to the default value
timers = [] #Creates the list for the timer lines, and sets it to the default value
measureLines = [] #Creates the list for the measure lines, and sets it to the default value
currentRate = 0 #Creates the variable for the the rate store, and sets it to 0 as it is not needed yet
timerLine = pygame.K_SPACE #Creates the variables for the keybinds, and sets them to their default value
timerReset = pygame.K_r
timerPause = pygame.K_p
timerErase = pygame.K_e
measureErase = pygame.K_e
simPause = pygame.K_TAB
bgColour = [255,255,255] #Creates the variable for the background colour, and sets it to the default value
selectionCursor, creationCursor, timerCursor, measureCursor, laserCursor, deletionCursor = 'selection_cursor.png', 'creation_cursor.png', 'timer_cursor.png', 'measure_cursor.png', 'laser_cursor.png', 'deletion_cursor.png' #Creates the variables for the cursor images

timerLineWait = False #Creates the variables for waiting for keybind change
timerResetWait = False
timerPauseWait = False
timerEraseWait = False
measureEraseWait = False
simPauseWait = False
laserExists = False

run = True #Creates the variable that continues the main loop

class Instance():
    #Main class for all objects within the simulation
    global xM #Takes in variables for mouse velocity
    global yM
    global scale #Takes in variable for the simulation scale
    def __init__(self,name="New Object",colour=[255,255,255],density=10,xpos=0,ypos=0,mass=10,shape="blank",size=1,xLength=1,yLength=1,thickness=1,youngs=1000):
        #Defines the attributes for the object
        self.frozen = { #List of which variables are frozen
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
        self.xLocation = xpos #Object X and Y Posistions (S)
        self.yLocation = ypos
        self.xVelocity = 0 #Object X and Y Velocities (V)
        self.yVelocity = 0
        self.xVelocityDelayed = 0 #Delayed X and Y velociteies used in SUVAT equations (U)
        self.yVelocityDelayed = 0
        self.xAcceleration = 0 #Object X and Y acceleration (A)
        self.yAcceleration = 0
        self.shape = shape #Object shape, not really used
        self.shapeOriginal = self.shape
        self.size = size #Object size variable, is reset to one at the end of a recalibrate, but is used to multiply an objects size
        self.xLength = xLength #Object X and Y lengths
        self.yLength = yLength
        self.xLengthDelayed = 0 #Delayed X and Y lengths used for Young's Modulus Calcuations
        self.yLengthDelayed = 0
        self.thickness = thickness #Thickness of object, usually set to 1
        self.YoModulus = youngs #Young's Modulus value x10^6
        self.density = density #Objects density, used to calculate mass
        self.mass = self.size*self.density #Objects mas, used to calcuate acceleration
        self.xForce = 0 #Object X and Y resultant forces
        self.yForce =  0
        self.colour = colour #Object colour used when rendering the object
        self.name = name #Object name used for identifing the object in the dictionary and for the user
        self.visual = pygame.Rect(int(self.xLocation), int(self.yLocation), int(self.xLength), int(self.yLength)) #The pygame Rectangle which is used for rendering
        self.selected = False #Boolean for if the object is currently selected and therfore should be dragged by the mouse
        self.drag = 0.98 #Attribute for the percentage efficiency the object has on the ground (98% by default, means that every recalibrate the XVelocity will be 98% of what it was before)
        self.elasticity = 0.75 #Attribute for how much an object bounces when colliding with another object, cannot be changed mid simulation but here so that a developer can adjust it
        self.xforce = 0 #Temporary X and Y forces used for calcuations
        self.yforce = 0
    def recalibrate(self): #Main method for recalcuating all the attributes, called every loop cycle (1/120 of a second)
        #Method for resetting variables (unless frozen)
        for attribute in self.frozen: #Checks first if the attribute is frozen
            if not self.frozen[attribute]:
                if attribute == "xLocation": #If not frozen, it identifies which attribute it is and does the corresponding equation
                    if not self.selected:
                        self.xLocation += (((self.xVelocity+self.xVelocityDelayed)/2*rateOfTime)/120)*scale
                    else:
                        self.xVelocityDelayed = self.xVelocity #If selected the object moves with the mouse and keeps the mouse's momentum
                        self.xVelocity = xM*0.5
                        self.xLocation = pygame.mouse.get_pos()[0]-self.xLength/2
                        self.xforce = self.mass * self.xVelocityDelayed - self.xVelocity
                elif attribute == "yLocation":
                    if not self.selected:
                        self.yLocation += (((self.yVelocity+self.yVelocityDelayed)/2*rateOfTime)/120)*scale
                    else:
                        self.yVelocityDelayed = self.yVelocityDelayed #If selected the object moves with the mouse and keeps the mouse's momentum
                        self.yVelocity = yM*0.5
                        self.yLocation = pygame.mouse.get_pos()[1] -self.yLength/2
                        self.yforce = self.mass * self.yVelocityDelayed - self.yVelocity
                    if self.yLocation > screenHeight - self.yLength - 49: #Defines the bottom of the screen where the object cannot go below
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
            else:
                if attribute == "xLocation": #When the posistion variables are frozen, that is when the young's modulus takes into effect
                    try:
                        self.xLengthDelayed = self.xLength #Calcutes new xLength as XLocation is frozen
                        self.xLength = ((self.xForce*self.xLengthDelayed)/(self.thickness*self.yLength*self.YoModulus*10**6))*rateOfTime + self.xLengthDelayed
                    except:
                        pass
                elif attribute == "yLocation":
                    try:
                        self.yLengthDelayed = self.yLength #Calculates new YLength as YLocation is frozen
                        self.yLength = ((self.yForce*self.yLengthDelayed)/(self.thickness*self.xLength*self.YoModulus*10**6))*rateOfTime + self.yLengthDelayed
                    except:
                        pass
        self.size = 1 #Resets the size back to 1
        self.visual = pygame.Rect(int(self.xLocation), int(self.yLocation), int(self.xLength), int(self.yLength)) #Sets the pygame rectangle to use the new values
        pygame.draw.rect(canvas, self.colour, self.visual) #Renders the object
class Ray():
    #Class for basic light rays
    def __init__(self,wavelength,startPos,gradient): #Sets the ray attributes
        self.wavelength = wavelength #Wavelength used to calcuate colour and perhaps more in the future
        self.startPos = startPos #The starting posistion of the ray
        self.endPos = [(),()] #The final position of the ray
        self.gradient = gradient #The gradient of the y=mx+c line that represents the ray
        self.intersect = (screenHeight-startPos[1])-(self.gradient*startPos[0]) #Intersect of the y=mx+c line that represents the ray
        self.rayCollider = None #Creates blank variable used for a pygame rectangle to see if the end of the ray collides with anything
        try: #Calcuates the colour values
            r = round(-((self.wavelength-750)/10.95892509)**2+255)
            if r < 0:
                raise ValueError
        except:
            r = 0
        try:
            g = round(-((self.wavelength-575)/10.95892509)**2+255)
            if g < 0:
                raise ValueError
        except:
            g = 0
        try:
            b = round(-((self.wavelength-400)/10.95892509)**2+255)
            if b < 0:
                raise ValueError
        except:
            b = 0
        self.colour = [r,g,b]
    def plot(self):
        try: #Recalculates the colour values encase the wavelength has changed
            r = round(-((self.wavelength-750)/10.95892509)**2+255)
            if r < 0:
                raise ValueError
        except:
            r = 0
        try:
            g = round(-((self.wavelength-575)/10.95892509)**2+255)
            if g < 0:
                raise ValueError
        except:
            g = 0
        try:
            b = round(-((self.wavelength-400)/10.95892509)**2+255)
            if b < 0:
                raise ValueError
        except:
            b = 0
        self.colour = [r,g,b]
        plotting = True
        x = 0
        startPositions = []
        endPositions = [] #Defines empty lists and variables to be assigned to in the loop
        gradients = []
        startPositions.append(self.startPos) #Addes the initial start position and gradient to the corresponding lists
        gradients.append(self.gradient)
        count = 0
        face = "tb" #Sets the face as top-bottom, used to see which reverse gradient to use when reflecting
        while plotting and count < 10000: #Limits to 10,000 loops to prevent bugs that cause infinite loops. (10,000 is enough for a normal loop)
            y = screenHeight - (gradients[-1]*x + self.intersect) #Calculates the y value of the next point with y=mx+c
            self.endPos = [x,y] #Sets the end position to the next point
            if x > screenWidth: #Tests if this end position is off the screen
                endPositions.append(self.endPos) #Adds the final end position to the list
                plotting = False #The loop ends since more line will not be seen
            if y > screenHeight:
                endPositions.append(self.endPos)
                plotting = False
            self.rayCollider = pygame.Rect(self.endPos[0], int(self.endPos[1]), 1, 1) #Creates small pygame rectangle for collision
            hit = False #Variable for if an object has been hit is set too false
            for object in instances: #Checks every object
                if self.rayCollider.colliderect(instances[object].visual): #If the ray collides with the object
                    hit = True #Says it has hit something
                    hitObject = instances[object] #Stores the object that it hit
            if face == "lr":
                x -= 1 #Goes backwards if it hit the left-right sides
            else:
                x += 1 #Goes forwards if it hit the top-bottom sides or if it hit nothing
            if hit: #If the ray it something
                if laserAngle != 0: #And the ray is not horizontal (reflection is meaningless if there is no angle of incidence)
                    endPositions.append(self.endPos) #Adds the end postion to the list
                    startPositions.append(endPositions[-1]) #Adds the end position as the next start position to the list
                    if (hitObject.xLocation+1) > self.endPos[0]: #Figues out with face it hit
                        face = "lr"
                    else:
                        face = "tb"
                    gradients.append(math.tan(math.radians(-laserAngle)))
                    x = 0 #Resets x to 0
            count += 1 #Adds one to the loop limiter
        for value in range(len(startPositions)): #For every start position
            try:
                pygame.draw.aaline(canvas, self.colour, startPositions[value-1], endPositions[value-1]) #Render the corresponding line
            except:
                pygame.draw.aaline(canvas, self.colour, self.startPos, (screenWidth,self.startPos[1]))#If that errors then render the original line
instances = {} #Empty dict used to store the existing objects


box = Instance("Box",[random.randint(1,255),random.randint(1,255),random.randint(1,255)],10,screenWidth/2, screenHeight/2, 10,"Rect", 1, 100, 100) #Defines the starting object
instances[box.name] = box #Adds it to the dict

def collide(i1,i2): #Function used for object collisions
    if i1.visual.colliderect(i2.visual):
        try: #Calculates the two objects velocities for after the collision
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
permaSelection = instances[random.choice(list(instances))] #Creates variable for the constantly selected object (used for the object panel) and sets it to the default box. (Or one of the default boxes if more than one are created)
canvas = pygame.display.set_mode((screenWidth,screenHeight)) #Creates the background pygame surface which all objects are rendered onto
pygame.display.set_caption("Simulation Space") #Sets the title of the window
canvas.fill(bgColour) #Sets the colour of the surface to the background colour

#Variables for the object panel and other GUI bits
oName = thorpy.Inserter(name="Name:",value="Object Name",size=(100,30)) #Inserter for the object's name
oColour = thorpy.ColorSetter("Object Colour",value=(128,128,128)) #Colour setter for the object's colour
oVHeading = thorpy.make_text("Object Attributes",15) #Text label to tell the user that the following are the attributes
attributes = [ #2D array used to generate the editable attribute list (so that a developer can add or remove some) and also sets them to all to not paused
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
    ["Drag",permaSelection.drag,True,False],
    ["Y.Mod (10^6)",permaSelection.YoModulus,True,False]
    ]
base = thorpy.Background(elements=[oName,oColour,oVHeading],color=(255,255,255),image="object_panel.png",mode=None) #Creates the main background of the GUI
def disableChange(element): #Function for pausing the update of inserters so that text can be entered
    if element.get_text() == "Mass": #Find out which inserter it is
        attributes[0][3] = True #Pauses it
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
    elif element.get_text() == "Y.Mod (10^6)":
        attributes[14][3] = True
def setAt(element,value): #Function for setting and object's attributes to the inserted value
    global rateOfTime, scale, timerLine, timerReset, timerPause, timerErase, measureErase, simPause #Imports variables that may need to be accessed or changed
    if element.get_text() == "Mass": #Find out which inserter is it
        try:
            permaSelection.mass = float(value) #Attempts to set the value
        except:
            pass #If and error occurs, e.g. text is entered for velocity, or the box is left blank. Then it does nothing
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
    elif element.get_text() == "Y.Mod (10^6)":
        try:
            permaSelection.YoModulus = float(value)
        except:
            pass
        attributes[14][3] = False
    elif element.get_text() == "Name:":
        try:
            permaSelection.name = value
        except:
            pass
    elif element.get_text() == "Rate:": #Also used for inserters that are not in the object panel such those in the settings menu
        try:
            rateOfTime = float(value)
        except:
            pass
    elif element.get_text() == "Simulation Scale":
        try:
            scale = float(value)
        except:
            pass
def freeze(row): #Function for freezing attributes when a clickbox is checked
    if row == (0): #Finds out which clickbox it was
        permaSelection.frozen["mass"] = not(permaSelection.frozen["mass"]) #Freezes the corresponding attribute (in the frozen dict)
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
for x in range(0,15): #For everyrow in the attribute list
   aValue = thorpy.Inserter(name=(attributes[x])[0],value=str((attributes[x])[1]),size=(50,20)) #Create the inserter
   aFrozen = thorpy.Checker(value=(attributes[x])[2]) #Create the frozen clickbox
   aFrozen.user_func = freeze #Set the clickbox function and params
   aFrozen.user_params = {'row':x}
   aHost = thorpy.Box(elements=[aValue,aFrozen],size=(180,20)) #Create a box to hold each row
   thorpy.store(aHost,mode="h") #Align the elements horizontally
   base.add_element(aHost) #Add the box to the main background
def show(): #Function for showing the object pannel
    global hidden #Imports the hidden variable
    menu.set_elements(screenBack) #Displays the object panel (setting menu to the object panel background)
    menu.blit_and_update()
    menu.refresh()
    hidden = False #Sets the hidden variable to false as the panel is not hidden
showTab, showTabHover = "open_tab.png", "open_tab_hover.png" #Sets variables for the images of the open and close tabs
hideTab, hideTabHover = "close_tab.png", "close_tab_hover.png"
showButton = thorpy.make_image_button(showTab,None,showTabHover) #Creates the show tab
showButton.user_func = show #Sets it's function
showButton.set_size((43,100)) #Set's it's size
showButton.set_center_pos((screenWidth-22,screenHeight/2)) #Set's it's posision
def hide(): #Function for hiding the object panel
    global hidden #Imports the hidden variable
    menu.set_elements([showButton,bar]) #Hides the object panel (setting menu to the toolbar and the show button)
    menu.blit_and_update()
    menu.refresh()
    hidden = True #Sets the hidden variable to true as the panel is hidden
hideButton = thorpy.make_image_button(hideTab,None,hideTabHover) #Creates the hide button
hideButton.user_func = hide #Sets it's function
hideButton.set_size((43,100)) #Set it's size
base.add_element(hideButton) #Add's it to the main background
def selectionClick(): #Functions for the  different toolbar buttons
    global cursorMode, cursor_picture
    cursorMode = 'selection' #Sets the mode to selection
    cursor_picture = pygame.image.load(selectionCursor).convert_alpha() #Sets the custom cursor
def creationClick():
    global cursorMode, creating, cursor_picture
    cursorMode = 'creation' #Sets the mode to creation
    creating = False
    cursor_picture = pygame.image.load(creationCursor).convert_alpha()
def timerClick():
    global cursorMode, cursor_picture
    cursorMode = 'timer' #Sets the mode to timer
    cursor_picture = pygame.image.load(timerCursor).convert_alpha()
def measureClick():
    global cursorMode, measuring, cursor_picture
    cursorMode = 'measure' #Sets the mode to measure
    measuring = False
    cursor_picture = pygame.image.load(measureCursor).convert_alpha()
def laserClick():
    global cursorMode, cursor_picture
    cursorMode = 'laser' #Sets the mode to laser
    cursor_picture = pygame.image.load(laserCursor).convert_alpha()
def deletionClick():
    global cursorMode, cursor_picture
    cursorMode = 'deletion' #Sets the mode to deletion
    cursor_picture = pygame.image.load(deletionCursor).convert_alpha()
def blankClick():
    global instances
    instances = {} #Makes the simulation blank
def playPause(): #Function for pausing and playing the simulation
    global rateOfTime, timePause, currentRate, timeDisplay #Imports the needed variables
    if rateOfTime > 0: #If not paused
        currentRate = rateOfTime #Set the current rate variable to the main rate variable
        rateOfTime = 0 #Set the main rate to 0
        timeDisplay.set_value(str(0)) #Update the rate inserter
        timePause._hovered = True #Makes the pause button look like it's hovered
    elif rateOfTime == 0: #If paused
        rateOfTime = currentRate #Set the main rate to the current rate variable
        timeDisplay.set_value(str(currentRate))#Update the rate inserter
def showSetttings(): #Function for showing the settings menu
    global showButton,bar,settingsBg,menu,settingsShown #Imports the required variables
    if not settingsShown: #If the settings menu is currently not shown
        menu.set_elements([showButton,bar,settingsBg]) #Show the settings menu
        menu.blit_and_update()
        menu.refresh()
        settingsShown = not(settingsShown) #Invert the settingsShown variable
    elif settingsShown: #If the settings menu is currently shown
        menu.set_elements([showButton,bar]) #Hide the settings menu
        menu.blit_and_update()
        menu.refresh()
        settingsShown = not(settingsShown) #Invert the settingsShown variable
def leave(): #Function for closing the simulation with the exit button
    global run
    run = False #Sets the loop variable to false so the loop will end
def timerLineChange(): #Functions for keybind changing which listens for the next key hit by setting the __Wait variables to True
    global timerLineWait
    timerLineWait = True
def timerResetChange():
    global timerResetWait
    timerResetWait = True
def timerPauseChange():
    global timerPauseWait
    timerPauseWait = True
def timerEraseChange():
    global timerEraseWait
    timerEraseWait = True
def measureEraseChange():
    global measureEraseWait
    measureEraseWait = True
def simPauseChange():
    global simPauseWait
    simPauseWait = True
timeDisplay = thorpy.Inserter(name="Rate:",value_type=float,size=(60,45),value="1") #Creates the rate inserter
selection, creation, timer, measure, laser_measure, deletion, blank = "selection.png", "creation.png", "timer.png", "measure.png", "laser.png", "deletion.png", "blank.png" #Defines the images for the toolbar buttons
selectionH, creationH, timerH, measureH, laser_measureH, deletionH, blankH = "selection_hover.png", "creation_hover.png", "timer_hover.png", "measure_hover.png", "laser_hover.png", "deletion_hover.png", "blank_hover.png" #Defines the images for the toolbar buttons when hovered
sTool, cTool, tTool, mTool, aTool, dTool, bTool = thorpy.make_image_button(selection,img_hover=selectionH),thorpy.make_image_button(creation,img_hover=creationH),thorpy.make_image_button(timer,img_hover=timerH),thorpy.make_image_button(measure,img_hover=measureH),thorpy.make_image_button(laser_measure,img_hover=laser_measureH),thorpy.make_image_button(deletion,img_hover=deletionH),thorpy.make_image_button(blank,img_hover=blankH) #Defines the toolbar buttons
sTool.user_func = selectionClick #Sets the buttons to their corresponding functions
cTool.user_func = creationClick
tTool.user_func = timerClick
mTool.user_func = measureClick
aTool.user_func = laserClick
dTool.user_func = deletionClick
bTool.user_func = blankClick
pause, pauseH = "pause.png","pause_hover.png" #Defines the images for the pause button
timePause = thorpy.make_image_button(pause,img_hover=pauseH) #Creates the pause button
timePause.user_func = playPause #Sets the pause button to it's function
settings,settingsH  = "settings.png", "settings_hover.png" #Defines images for the settings button
settingsButton = thorpy.make_image_button(settings,img_hover=settingsH) #Creates the settings button
settingsButton.user_func = showSetttings #Sets the settings button to the show/hide settings function
bar = thorpy.Box(elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool, settingsButton, timePause, timeDisplay],size=(screenWidth,50)) #Creates the box that holds the toolbar
bar.set_main_color(color=[100,100,100]) #Sets the colour of the toolbar
thorpy.store(bar,mode="h",align="center",gap=50,margin=350,elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool]) #Aligns the main toolbar buttons to the left
thorpy.store(bar,mode="h",align="center",margin=-600,elements=[settingsButton, timePause, timeDisplay]) #Aligns the time and settings buttons to the right
screenBack = thorpy.Background(elements=[base,bar],color=[0,0,0,0],mode="scale to screen") #Creates the object panel background (parent used for hiding the panel and aligning the panel's location)
thorpy.store(base,mode="v",align=("center"),y=0) #Aligns the elements of the base
hideButton.set_center_pos((-22,screenHeight/2)) #Sets the hide tab's position relative to it's parent
thorpy.store(screenBack,mode="v",x=screenWidth/2,y=(screenHeight-54),elements=[bar]) #Aligns the toolbar
thorpy.store(screenBack,mode="v",align="right",x=screenWidth,y=-5,elements=[base]) #Aligns the base (main background for object panel)
scaleInserter = thorpy.Inserter("Simulation Scale",value=str(scale),size=(100,20)) #Creates scale inserter for settings menu
timerLineText = thorpy.make_text("Timer Line Keybind") #Labels for the following keybinds
timerLineButton = thorpy.make_button(text=str(pygame.key.name(timerLine)),func=timerLineChange) #Buttons for the keybinds
timerResetText = thorpy.make_text("Timer Reset Keybind")
timerResetButton = thorpy.make_button(text=str(pygame.key.name(timerReset)),func=timerResetChange)
timerPauseText = thorpy.make_text("Timer Pause Keybind")
timerPauseButton = thorpy.make_button(text=str(pygame.key.name(timerPause)),func=timerPauseChange)
timerEraseText = thorpy.make_text("Timer Erase Keybind")
timerEraseButton = thorpy.make_button(text=str(pygame.key.name(timerErase)),func=timerEraseChange)
measureEraseText = thorpy.make_text("Measure Erase Keybind")
measureEraseButton = thorpy.make_button(text=str(pygame.key.name(measureErase)),func=measureEraseChange)
simPauseText = thorpy.make_text("Pause Simulation Keybind")
simPauseButton = thorpy.make_button(text=str(pygame.key.name(simPause)),func=simPauseChange)
bgColourSelector = thorpy.ColorSetter("Background Colour",value=[255,255,255]) #Colour setter for the background colour
exitButton = thorpy.make_button("Exit Program",leave) #Creates button for leaving the simulation
container = thorpy.Box(elements=[scaleInserter,timerLineText,timerLineButton,timerResetText,timerResetButton,timerPauseText,timerPauseButton,timerEraseText,timerEraseButton,measureEraseText,measureEraseButton,simPauseText,simPauseButton,bgColourSelector,exitButton],size=(1200,600)) #Creates the main box for the settings menu
container.set_main_color([100,100,100]) #Sets the colour of the settings menu
settingsBg = thorpy.Background(elements=[container],color=[0,0,0,0]) #Creates an invisible background used to align the settings menu
thorpy.store(settingsBg,mode="v") #Aligns the settings menu
menu = thorpy.Menu([showButton,bar],fps=120) #Creates the main 'menu'

laserAngle = 0 #Creates variable for a light ray's angle and sets it to 0 (Horizontal-Right)
time = pygame.time.Clock() #Creates the pygame clock variable used to control the flow of time in the main loop
stopwatch = 0.00 #Creates the stopwatch variable used to count time for the timer mode
stopwatch_pause = True #Creates the varianle for if the stopwatch is paused
rateOfTime = 1 #Creates the main rate variable used to speed up, slow down and pause the simulation
selection = None #Creates the selection variable used to store when an object is selected
pygame.display.set_mode(flags=pygame.FULLSCREEN) #Makes the window fullscreen
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #Makes the windows cursour invisable so custom cursors can be used
cursor_picture = pygame.image.load(selectionCursor).convert_alpha() #Sets the custom cursour to the selection cursor
while run: #Main loop
    time.tick(rateOfTime*120) #Ticks based on the rate of time * 120 for 120 fps at rate = 1
    if not stopwatch_pause: #Updates the stopwatch if it is not paused
        stopwatch += (rateOfTime*120)
    canvas.fill(bgColour) #Blank out the rendering to the background colour
    for event in pygame.event.get(): #Gets the pygame events for things like keybinds, mouse clicks and GUI usage
        if event.type == pygame.QUIT: #Quits if the X button is hit (Not needed for fullscreen but encase you change the code to windowed)
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'selection': #If you left-click in selection mode
            clickbox = pygame.Rect(event.pos[0]-10, event.pos[1]-10, 20, 20) #Creates a small box around the cursor
            for instance in instances: #Checks every object
                if clickbox.colliderect(instances[instance].visual): #Tests if the box collides with it
                    instances[instance].selected = True #If it does it is selected and the attributes and variables are set
                    selection = instances[instance]
                    permaSelection = instances[instance]
                    base._elements[0].set_value(permaSelection.name) #Object panel information is set
                    base._elements[1].set_value(permaSelection.colour)
                    if not hidden: #If the panel is not hidden
                        menu.set_elements(screenBack) #Re-render the panel
                        menu.blit_and_update()
                        menu.refresh()
                    break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'creation': #If you click in creation mode
            creating = True #Start the creating functions
            startPos = event.pos #Set the starting position as the mouse posistion
            moved = False #Define variable that says the cursor hasn't moved since clicking
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cursorMode == 'measure': #If you click in measure mode
            measuring = True #Start the measuring functions
            startPosM = event.pos #Set the starting posistions as the mouse position
            movedM = False #Define variable that says the cursor hasn't moved since clicking
        if event.type == pygame.KEYDOWN and event.key == timerLine and cursorMode == "timer": #If you press the timerLine keybind in timer mode
            newLine = pygame.Rect(pygame.mouse.get_pos()[0],0,4,screenHeight) #Create the new timer line
            timers.append([newLine,None]) #Add it to the timer lines list
        if event.type == pygame.KEYDOWN and event.key == timerReset and cursorMode == "timer": #If you press the timerReset keybind in timer mode
            stopwatch = 0.0 #Resets the stopwatch
        if event.type == pygame.KEYDOWN and event.key == timerPause and cursorMode == "timer": #If you press the timerPause keybind in timer mode
            stopwatch_pause = not(stopwatch_pause) #Pause or play the stopwatch
        if event.type == pygame.KEYDOWN and event.key == timerErase and cursorMode == "timer": #If you press the timerErase keybind in timer mode
            timers = [] #Delete all timer lines
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and cursorMode == 'laser': #If you press space in laser mode
            laserExists = True #Set a variable that says a laser exists
            laserStartPos = pygame.mouse.get_pos() #Gets the strrt position as the position of the mouse
            laserRay = Ray(random.randint(400,750),laserStartPos,math.tan(math.radians(laserAngle))) #Creates a ray object with the start pos and a gradient of a tangent of the laser angle
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and cursorMode == 'laser': #If you press up in laser mode
            laserAngle += 1 #Rotate the laser by 1
            if laserAngle > 360:
                laserAngle = 1 #Loop if going above 360
            if laserAngle > 90 and laserAngle < 270:
                laserRay.gradient = -math.tan(math.radians(laserAngle)) #Recalculate the gradient, if in negative region
            else:
                laserRay.gradient = math.tan(math.radians(laserAngle)) #Recalculate the gradient
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and cursorMode == 'laser':
            laserAngle -= 1 #Rotate the laser by -1
            if laserAngle < 0:
                laserAngle  = 359 #Loop if going into negatives
            if laserAngle > 90 and laserAngle < 270:
                laserRay.gradient = -math.tan(math.radians(laserAngle)) #Recalculate the gradient, if in negative region
            else:
                laserRay.gradient = math.tan(math.radians(laserAngle)) #Recalculate the gradient
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and cursorMode == 'laser': #If you press e in laser mode
            laserExists = False #Sets variable to say that no lasers exist
        if event.type == pygame.KEYDOWN and event.key == measureErase and cursorMode == "measure": #If you press the measureErase keybind in measure mode
            measureLines = [] #Empties the list of measure lines
        if event.type == pygame.KEYDOWN and event.key == simPause: #If you press the simPause keybind
            playPause() #Call function to play/pause the simulation
        if event.type == pygame.KEYDOWN and timerLineWait: #If key is pressed when listening for keybind changes
            timerLineWait = False #Stop listening
            timerLine = event.key #Change the keybind
            timerLineButton.set_text(str(pygame.key.name(event.key))) #Update the button text
        if event.type == pygame.KEYDOWN and timerResetWait:
            timerResetWait = False
            timerReset = event.key
            timerResetButton.set_text(str(pygame.key.name(event.key)))
        if event.type == pygame.KEYDOWN and timerPauseWait:
            timerPauseWait = False
            timerPause = event.key
            timerPauseButton.set_text(str(pygame.key.name(event.key)))
        if event.type == pygame.KEYDOWN and timerEraseWait:
            timerEraseWait = False
            timerErase = event.key
            timerEraseButton.set_text(str(pygame.key.name(event.key)))
        if event.type == pygame.KEYDOWN and measureEraseWait:
            measureEraseWait = False
            measureErase = event.key
            measureEraseButton.set_text(str(pygame.key.name(event.key)))
        if event.type == pygame.KEYDOWN and simPauseWait:
            simPauseWait = False
            simPause = event.key
            simPauseButton.set_text(str(pygame.key.name(event.key)))
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'selection': #If you stop clicking in selection mode
            for instance in instances:
                if instances[instance].selected:
                    instances[instance].selected = False
                    selection = None #Diselect any selected object
        if event.type == pygame.MOUSEMOTION and cursorMode == 'selection': #If the mouse moves in selection mode
            xM = event.rel[0] #Calcuate momentums for objects that are diselected
            yM = event.rel[1]
        if event.type == pygame.MOUSEMOTION and cursorMode == 'creation' and creating: #If the mouse moves in creation mode and it is currently creating
            xDis = -(startPos[0] - event.pos[0]) #Work out the distances between the cursor start and current posistion
            yDis = -(startPos[1] - event.pos[1])
            example = pygame.Rect(startPos[0],startPos[1],xDis,yDis) #Create an example rectangle to show the user what they are creating
            moved = True #Set the variable to tell the simulation that the cursour has moved
        if event.type == pygame.MOUSEMOTION and cursorMode == 'measure' and measuring: #If the mouse moves in measure mode and it is currently measuring
            xDisM = -(startPosM[0] - event.pos[0])#Work out the distances between the cursor start and current posistion
            yDisM = -(startPosM[1] - event.pos[1])
            tDisM = math.hypot(xDisM,yDisM)/scale #Work out the actual distance between the points
            measure_line = [startPosM,[event.pos[0],event.pos[1]]] #Create the line between the two points
            movedM = True #Set the variable to tell the simulation that the cursour has moved
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'creation' and creating: #If you stop clicking in creation mode
            creating = False #Stop creation functions
            if moved: #If the cursor moved, i.e. not a standalone click
                boxes += 1 #Add one to the number of boxes
                spawn = Instance("New Box "+str(boxes),[random.randint(1,255),random.randint(1,255),random.randint(1,255)],10,startPos[0], startPos[1], 10,"Rect", 1, xDis, yDis) #Create the new instance
                instances[spawn.name] = spawn #Add it to the dict of instances
        if event.type == pygame.MOUSEBUTTONUP and cursorMode == 'measure' and measuring: #If you stop clicking in measure mode and it is measuring
            measuring = False #Stop measuring functions
            if movedM: #If the cursor moved, i.e. not a standalone click
                measure_line.append(tDisM) #Define the attributes for the full measure line
                measure_line.append(startPosM)
                measure_line.append([xDisM,yDisM])
                measureLines.append(measure_line) #Add it to the list of measure lines
                measure_line = None #Clear the temp variable
        if event.type == pygame.MOUSEBUTTONDOWN and cursorMode == "deletion": #If you click in deletion mode
            clickbox = pygame.Rect(event.pos[0]-10, event.pos[1]-10, 20, 20) #Create a collider rectangle around the cursor
            toBeDeleted = [] #Create an empty list of the objects to be removed
            for instance in instances: #Check every object
                if clickbox.colliderect(instances[instance].visual): #If the collider rectangle collides with ti
                    toBeDeleted.append(instance) #Add it to the deletion list
            for item in toBeDeleted: #Delete every item in the deletion list
                del instances[item]
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_PRESS: #If an inserter is pressed
            disableChange(event.el) #Call the function is disable the inserter's updates
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_INSERT: #If text in entered in an inserter
            setAt(event.el,event.value) #Call the function to set it to the appropriate attribute
        if event.type == thorpy.constants.THORPY_EVENT and event.id == thorpy.constants.EVENT_SLIDE: #If a slider is used
            if event.el == oColour._r_element or event.el == oColour._g_element or event.el == oColour._b_element: #Check if it is the object panel sliders
                permaSelection.colour = oColour.get_color() #If it is then set the colour of the object
            else:
                bgColour = bgColourSelector.get_color() #If not then set the colour of the background
        menu.react(event) #Intergrate the thorpy GUI to pygame
    for item in instances: #For every instance
        for item2 in instances: #For every other instance
            if instances[item] != instances[item2]:
                collide(instances[item],instances[item2]) #Call the collision function to test and calculate collisions
        instances[item].recalibrate() #Call the recalibration method of every instance
    pygame.draw.rect(canvas, [255,0,0,255], permaSelection.visual,3) #Draw a red outline around the last selected object
    clicked = [] #Create blank list for which inserters are paused
    for row in attributes:
        clicked.append(row[3]) #Set the clicked list to the values for which inserters are paused
    attributes = [ #Define the new attribute 2D array using the clicked list
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
        ["Drag",permaSelection.drag,True,clicked[13]],
        ["Y.Mod (10^6)",permaSelection.YoModulus,True,clicked[14]],
        ]
    for x in range(4,17): #For every attribute
        if not attributes[x-3][3]: #If not paused
            base._elements[x]._elements[0].set_value(str(attributes[x-3][1])) #Update the inserter's value
        base._elements[x]._elements[1].set_value(attributes[x-3][2]) #Update the clickbox's value
    if cursorMode == 'creation' and creating: #If creating in creation mode
        try:
            pygame.draw.rect(canvas,[100,100,100], example) #Render the example rectangle
        except:
            pass
    for line in timers:
        pygame.draw.rect(canvas,[0,0,0],line[0]) #Render every timer line
    for line in measureLines:
        pygame.draw.aaline(canvas,[15,15,15],line[0],line[1]) #Render every measure line
        line_distance = fonty.render(str(round(line[2],2)),False,[15,15,15]) #Generate text for that line's distance
        canvas.blit(line_distance,(int(line[4][0]/2+line[3][0]),int(line[4][1]/2+line[3][1]))) #Render the distance text in the center of the line

    try:
        pygame.draw.aaline(canvas,[15,15,15],measure_line[0],measure_line[1]) #Draw the temporary line that's generated as the mouse drags
        line_distance_fresh = fonty2.render(str(round(tDisM,2)),False,[15,15,15]) #Generate the temporary distance of the line as text
        canvas.blit(line_distance_fresh,(int(screenWidth/2),int(screenHeight/2))) #Render the text as large in the center of the screen
    except:
        pass
    stopwatch_text = fonty2.render(str(stopwatch/12000),False,[0,0,0]) #Generate the text for the stopwatch
    canvas.blit(stopwatch_text,(int(screenWidth/2),0)) #Render the text
    if laserExists:
        laserRay.plot() #Call plot method of the laser ray if one exists
    menu.blit_and_update()
    menu.refresh() #Update the GUI to include any changes
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #Reset the cursor as transparent
    canvas.blit(cursor_picture, pygame.mouse.get_pos()) #Render the custom cursor
    pygame.display.update() #Display all new renders
