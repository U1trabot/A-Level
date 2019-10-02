import pygame
pygame.init()

screenWidth = (800)
screenHeight = (600)

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Test")

walkRight = [pygame.image.load('sprites/R1.png'), pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'), pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png'), pygame.image.load('sprites/R6.png'), pygame.image.load('sprites/R7.png'), pygame.image.load('sprites/R8.png'), pygame.image.load('sprites/R9.png')]
walkLeft = [pygame.image.load('sprites/L1.png'), pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'), pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png'), pygame.image.load('sprites/L6.png'), pygame.image.load('sprites/L7.png'), pygame.image.load('sprites/L8.png'), pygame.image.load('sprites/L9.png')]
bg = pygame.image.load('sprites/bg.jpg')
char = pygame.image.load('sprites/standing.png')

clock = pygame.time.Clock()
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 6
        self.standing = True
        self.firstLoad = True
    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[4], (self.x,self.y))
            elif self.left:
                win.blit(walkLeft[4], (self.x,self.y))
            elif self.firstLoad:
                win.blit(char, (self.x,self.y))
class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.velocity = 12*facing
    def draw(self,win):
        pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius)
def redrawGameWindow():
    global walkCount
    win.fill((0,0,100))
    block.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run = True
block = player(300,530,64,64)
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if block.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5000:
            bullets.append(projectile(round(block.x + block.width //2),round(block.y +block.height//2), 6, (255,0,0), facing))
    if keys[pygame.K_LEFT] and block.x > block.velocity:
        block.x -= block.velocity
        block.left = True
        block.right = False
        block.standing = False
        block.firstLoad = False
    elif keys[pygame.K_RIGHT] and block.x < (screenWidth - block.width):
        block.x += block.velocity
        block.left = False
        block.right = True
        block.standing = False
        block.firstLoad = False
    else:
        block.walkCount = 0
        block.standing = True
    if not(block.isJump):
        if keys[pygame.K_UP]:
            block.isJump = True
            block.walkCount = 0
    else:
        if block.jumpCount >= -6:
            neg = 1
            if block.jumpCount < 0:
                neg = -1
            block.y -= (block.jumpCount ** 2)*neg
            block.jumpCount -= 1
        else:
            block.isJump = False
            block.jumpCount = 6
    redrawGameWindow()
pygame.quit()