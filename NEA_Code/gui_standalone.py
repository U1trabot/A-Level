import thorpy, pygame
pygame.init()
screenWidth = (1366)
screenHeight = (768)
mouseForce = 15
cursorMode = 'selection'
scale = 10
timerLine = pygame.K_SPACE
timerReset = pygame.K_r
timerPause = pygame.K_p
timerErase = pygame.K_e
measureErase = pygame.K_e
simPause = pygame.K_TAB
bgColour = [255,255,255]

def leave():
    print("Exiting Program")
canvas = pygame.display.set_mode((screenWidth,screenHeight))
forceInserter = thorpy.Inserter("Cursor Force",value=str(mouseForce),size=(100,20))
scaleInserter = thorpy.Inserter("Simulation Scale",value=str(scale),size=(100,20))
timerLineInserter = thorpy.Inserter("Timer Line Keybind",value=str(pygame.key.name(timerLine)),size=(100,20))
timerResetInserter = thorpy.Inserter("Timer Reset Keybind",value=str(pygame.key.name(timerReset)),size=(100,20))
timerPauseInserter = thorpy.Inserter("Timer Pause Keybind",value=str(pygame.key.name(timerPause)),size=(100,20))
timerEraseInserter = thorpy.Inserter("Timer Erase Keybind",value=str(pygame.key.name(timerErase)),size=(100,20))
measureEraseInserter = thorpy.Inserter("Measure Erase Keybind",value=str(pygame.key.name(measureErase)),size=(100,20))
simPauseInserter = thorpy.Inserter("Pause Simulation Keybind",value=str(pygame.key.name(simPause)),size=(100,20))
bgColourSelector = thorpy.ColorSetter("Background Colour",value=[255,255,255])
exitButton = thorpy.make_button("Exit Program",leave)
container = thorpy.Box(elements=[forceInserter,scaleInserter,timerLineInserter,timerResetInserter,timerPauseInserter,timerEraseInserter,measureEraseInserter,simPauseInserter,bgColourSelector,exitButton],size=(850,650))
container.set_main_color([100,100,100])
menu = thorpy.Menu(elements=[container])
menu.play()