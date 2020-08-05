import pygame
pygame.init()

screenWidth = (800)
screenHeight = (600)

class Instance():
    #Main class for all objects within the simulation
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
        self.yForce = self.mass*9.81
        self.roughness = roughness
        self.colour = colour
        self.name = name
        self.visual = pygame.Rect((screenWidth/2)+self.xLocation, (screenHeight/2)-self.yLocation, self.xLength, self.yLength)
        self.selected = False
    def recalibrate(self):
        #Method for resetting variables (unless frozen)
        for attribute in self.frozen:
            if not self.frozen[attribute]:
                if attribute == "xLocation":
                    blocked = False
                    for instance in instances:
                        if instances[instance] != self:
                            if self.visual.colliderect(instances[instance].visual):
                                blocked = True
                    if not self.selected:
                        if not blocked:
                            self.xLocation += ((self.xVelocity+self.xVelocityDelayed)/2)/6
                    else:
                        self.xLocation = pygame.mouse.get_pos()[0] - 50
                elif attribute == "yLocation":
                    blocked = False
                    for instance in instances:
                        if instances[instance] != self:
                            if self.visual.colliderect(instances[instance].visual):
                                blocked = True
                    if not self.selected:
                        if not blocked:
                            self.yLocation += ((self.yVelocity+self.yVelocityDelayed)/2)/6
                    else:
                        self.yLocation = pygame.mouse.get_pos()[1] - 50
                elif attribute == "xVelocity":
                    blocked = False
                    for instance in instances:
                        if instances[instance] != self:
                            if self.visual.colliderect(instances[instance].visual):
                                blocked = True
                    if not blocked:
                        self.xVelocity += self.xAcceleration/60
                    else:
                        self.xVelocity = 0
                elif attribute == "yVelocity":
                    blocked = False
                    for instance in instances:
                        if instances[instance] != self:
                            if self.visual.colliderect(instances[instance].visual):
                                blocked = True
                    if not blocked:
                        self.yVelocity += self.yAcceleration/60
                    else:
                        self.yVelocity = 0
                elif attribute == "xAcceleration":
                    self.xAcceleration = self.xForce/self.mass
                elif attribute == "yAcceleration":
                    self.yAcceleration = self.yForce/self.mass
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
        self.visual = pygame.Rect(self.xLocation, self.yLocation, self.xLength, self.yLength)
        pygame.draw.rect(canvas, self.colour, self.visual)

instances = {}
floor = Instance("Floor",[40,40,40],5,0,580,10,"blank",1,1000,100)
floor.yForce = 0
box = Instance("Box",[0,255,0],50,140,220,10,"blank",1,100,100)
box2 = Instance("Box2",[255,0,0],50,100,100,10,"blank",1,100,100)
box3 = Instance("Box3",[0,0,255],50,60,-100,10,"blank",1,100,100)
instances[box.name] = box
instances[floor.name] = floor
instances[box2.name] = box2
instances[box3.name] = box3


canvas = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Simulation Space")
canvas.fill([255,255,255])

time = pygame.time.Clock()
rateOfTime = 1
run = True
while run:
    time.tick(rateOfTime*60)
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
                    floor.selected = False
        if event.type == pygame.MOUSEBUTTONUP:
            for instance in instances:
                if instances[instance].selected:
                    instances[instance].selected = False
    for item in instances:
        instances[item].recalibrate()
    pygame.draw.rect(canvas, floor.colour, floor.visual)
    pygame.display.update()



