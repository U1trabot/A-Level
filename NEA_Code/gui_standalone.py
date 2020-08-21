import thorpy, pygame
pygame.init()
screenWidth = (1366)
screenHeight = (768)
cursorMode = 'selection'
canvas = pygame.display.set_mode((screenWidth,screenHeight))
def selectionClick():
    global cursorMode
    cursorMode = 'selection'
def creationClick():
    global cursorMode
    cursorMode = 'creation'
def timerClick():
    global cursorMode
    cursorMode = 'timer'
def measureClick():
    global cursorMode
    cursorMode = 'measure'
def angleClick():
    global cursorMode
    cursorMode = 'angle'
def deletionClick():
    global cursorMode
    cursorMode = 'deletion'
def blankClick():
    global cursorMode
    cursorMode = 'blank'
timeDisplay = thorpy.Inserter(value_type=float,size=(60,45),value="x1")
selection, creation, timer, measure, angle_measure, deletion, blank = "selection.png", "creation.png", "timer.png", "measure.png", "angle_measure.png", "deletion.png", "blank.png"
selectionH, creationH, timerH, measureH, angle_measureH, deletionH, blankH = "selection_hover.png", "creation_hover.png", "timer_hover.png", "measure_hover.png", "angle_measure_hover.png", "deletion_hover.png", "blank_hover.png"
sTool, cTool, tTool, mTool, aTool, dTool, bTool = thorpy.make_image_button(selection,img_hover=selectionH),thorpy.make_image_button(creation,img_hover=creationH),thorpy.make_image_button(timer,img_hover=timerH),thorpy.make_image_button(measure,img_hover=measureH),thorpy.make_image_button(angle_measure,img_hover=angle_measureH),thorpy.make_image_button(deletion,img_hover=deletionH),thorpy.make_image_button(blank,img_hover=blankH)
play, playH, pause, pauseH = "play.png","play_hover.png","pause.png","pause_hover.png"
timePause = thorpy.make_image_button(pause,img_hover=pauseH)
bar = thorpy.Box(elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool, timePause, timeDisplay],size=(screenWidth,50))
bar.set_main_color(color=[100,100,100])
thorpy.store(bar,mode="h",align="center",gap=50,margin=350,elements=[sTool, cTool, tTool, mTool, aTool, dTool, bTool])
thorpy.store(bar,mode="h",align="center",margin=-600,elements=[timePause, timeDisplay])
screenBack = thorpy.Background([0,255,255],elements=[bar])
menu = thorpy.Menu(screenBack,fps=120)
thorpy.store(screenBack,mode="v",x=screenWidth/2,y=(screenHeight-55),elements=[bar])
menu.play()