#Rena Liu Paint Project - Percy Jackson Paint

##LIST OF FEATURES-----------------------------------------------------------------------------------------------------------
##1. Pencil
##2. Eraser (erases on background too)
##3. Brush
##4. Spray Paint
##5. Color Picker
##6. Clear Canvas
##7. Rectangle (F/NF)
##8. Elise (F/NF)
##9. Triangle (F/NF)
##10. Polygon (F/NF)
##11. Line
##12. Text
##13. Background Filler
##14. Selection Tool
##15. Stamps
##16. Save
##17. Load
##18. Undo/Redo
##19. Music Player (pause/play, next, previous, restart, volume up/volume down)
##20. Brush Thickness 
##21. Gradient Color Palette
##22. Tool Explanation Box
##23. Background Wallpaper


#IMPORTING----------------------------------------------------------------
from pygame import *
from tkinter import *
from tkinter import filedialog
from random import *
from math import *


#SETUP---------------------------------------------------------------------
#hides the small window that pops up
Tk().withdraw()

#initializes font and mixer
font.init()
mixer.init()

width, height = 1200, 700
screen = display.set_mode((width, height))

#timer for frequency of spray paint tool
myClock = time.Clock()

#making custom endevent to signal when a song ends
MUSICEND = USEREVENT + 1
mixer.music.set_endevent(MUSICEND)


#BACKGROUNDS AND STAMPS---------------------------------------------------
#BACKGROUND
wallpaper = image.load("Pics/waves background.jpg")
#displaying background
screen.blit(wallpaper, (0, 0))

#STAMPS FILE ADDRESSES
stampsFileNames = ["Pics/stamps/posiden.jpg", "Pics/stamps/hades.jpg", "Pics/stamps/nike.jpg", "Pics/stamps/athena.jpg",
                   "Pics/stamps/hephaestus.jpg", "Pics/stamps/hypnos.jpg", "Pics/stamps/hermes.jpg", "Pics/stamps/artemis.jpg",
                   "Pics/stamps/ares.jpg", "Pics/stamps/iris.jpg", "Pics/stamps/hecate.jpg", "Pics/stamps/hera.jpg",
                   "Pics/stamps/dionysus.jpg", "Pics/stamps/tyche.jpg", "Pics/stamps/hebe.jpg", "Pics/stamps/apollo.jpg",
                   "Pics/stamps/aphrodite.jpg", "Pics/stamps/demeter.png", "Pics/stamps/nemisis.jpg"]

#MAKING LIST OF STAMPS
stamps = []
for name in stampsFileNames:
    stamps.append(image.load(name))

#BACKGROUND PATTERNS FILE ADDRESSES
BKGDFileNames = ["Pics/backgrounds/trident background.png", "Pics/backgrounds/riptide background.jpg", "Pics/backgrounds/waves.png",
                 "Pics/backgrounds/lightning.png", "Pics/backgrounds/camp-half-blood.png"]

#MAKING LIST OF BACKGROUND PATTERNS
BKGDPatterns = []
for name in BKGDFileNames:
    BKGDPatterns.append(image.load(name))


#TOOLS AND FILE BUTTONS----------------------------------------------------------
#TOOL ICONS FILE ADDRESSES
toolFileNames = ["Pics/tools/pencil.png", "Pics/tools/eraser.png", "Pics/tools/brush.png", "Pics/tools/dropper.png",
                 "Pics/tools/square.png", "Pics/tools/circle.png", "Pics/tools/triangle.png", "Pics/tools/polygon.png",
                 "Pics/tools/line.png", "Pics/tools/roller.png", "Pics/tools/spray.png", "Pics/tools/select.png", "Pics/tools/clear.png",
                 "Pics/tools/text.png"]

#MAKING LIST OF TOOL ICONS
toolIcons = []
for name in toolFileNames:
    toolIcons.append(image.load(name))

#LIST OF TOOLS POSITIONS
toolPos = [(20, 125), (80, 125), (140, 125), (200, 125), (20, 185), (80, 185), (140, 185),
           (200, 185), (20, 245), (80, 245), (140, 245), (200, 245), (20, 305), (80, 305)]

#LIST OF TOOL NAMES (TO CALL ON)
toolNames = ["pencil", "eraser", "brush", "dropper", "rect", "circle",
             "triangle", "polygon", "line", "roller", "spray", "select", "clear", "text"]

#TOOL RECTS (for collidepoint and hover, select, default borders)
pencilRect = Rect(17, 122, 56, 56)
eraserRect = Rect(77, 122, 56, 56)
brushRect = Rect(137, 122, 56, 56)
dropperRect = Rect(197, 122, 56, 56)
rectRect = Rect(17, 182, 56, 56)
circleRect = Rect(77, 182, 56, 56)
triangleRect = Rect(137, 182, 56, 56)
polygonRect = Rect(197, 182, 56, 56)
lineRect = Rect(17, 242, 56, 56)
rollerRect = Rect(77, 242, 56, 56)
sprayRect = Rect(137, 242, 56, 56)
selectRect = Rect(197, 242, 56, 56)
clearRect = Rect(17, 302, 56, 56)
textRect = Rect(77, 302, 56, 56)

#LIST OF TOOL RECTS
tools = [pencilRect, eraserRect, brushRect, dropperRect, rectRect,
         circleRect, triangleRect, polygonRect, lineRect, rollerRect,
         sprayRect, selectRect, clearRect, textRect]

#list of tools that need to have canvaCap (screenshot of canvas) blitted constantly as they need to be moved around
screenCapTools = ["rect", "circle", "triangle", "polygon", "line", "select", "stamp"]

#FILE BUTTON ICONS 
saveIcon = image.load("Pics/file buttons/save.png")
openIcon = image.load("Pics/file buttons/open.png")
undoIcon = image.load("Pics/file buttons/undo.png")
redoIcon = image.load("Pics/file buttons/redo.png")

#ICONS THAT ARE ONLY USED IF BUTTON CANNOT BE CLICKED
undoGreyIcon = image.load("Pics/file buttons/undogrey.png") 
redoGreyIcon = image.load("Pics/file buttons/redogrey.png")

#LIST OF FILE BUTTON ICONS
fileIcons = [saveIcon, openIcon, undoIcon, redoIcon]

#LIST OF FILE BUTTON POSITIONS
filePos = [(30, 70), (80, 70), (130, 70), (180, 70)]

#FILE BUTTON RECTS (for collidepoint and hover, select, default borders)
saveRect = Rect(27, 67, 46, 46)
openRect = Rect(77, 67, 46, 46)
undoRect = Rect(127, 67, 46, 46)
redoRect = Rect(177, 67, 46, 46)


#DRAWING THE BUTTONS---------------------------------------------------------
#DRAWIGN THE TOOLS AND FILE BUTTONS BACKGROUND
draw.rect(screen, (7, 59, 77), (15, 67, 240, 293)) 

#BLITTING ALL OF THE TOOL AND FILE BUTTON ICONS
for i in range(4):
    screen.blit(fileIcons[i], filePos[i])

for t in range(14):
    screen.blit(toolIcons[t], toolPos[t])


#DEFINING VARIABLES-----------------------------------------------------------
#COLORS
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0, 25)
BLUE = (7, 59, 77)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
DARKBLUE = (24, 71, 173)
LIGHTBLUE = (176, 231, 255)
LIGHTGREY = (200, 200, 200)

#color of pencil, line, rectangle, etc. (default is black)
col = BLACK

#current selected tool
tool = None

#radius/thickness of brush, rectangle, etc.
radius = 1

#the radius/thickness for the rectangle, circle, triangle, and polygon tool (same as radius if fill is unselected, otherwise 0)
fill = radius

#if fill is selected or not (False for not selected)
fillSelect = False

#if user used a background pattern (to know which eraser to use)
backgroundPattern = False

#if user is currently in the middle of drawing a polygon
drawPoly = False

#current stamp and background
stampPos = 0
backgroundPos = 0

#user's word for text tool
word = ""

#which tool is selected (-1 is no tool)
selectedTool = -1

#current song and volume marker position on slider
songPos = 0
volumePosX = 782

#if music is playing or paused (0 means music has not played yet (will need to load music), 1 means currently playing, 2 means paused)
#defaulted to not play until user click on play button
playOrPause = 0

#if the user is dragging the volume slider
volumeChange = False


#COLOR PALATTE------------------------------------------------------------------
#LOADING AND BLITTING PALETTE, MAKING PALETTE RECT (for collidepoint)
palette = image.load("Pics/color palette.png")
paletteRect = Rect(20, 500, 280, 187)
screen.blit(palette, (20, 500))

#MAKING CURRENT COLOR DISPLAY
currentColorBKGD = Rect(310, 540, 80, 110)
currentColorRectBKGD = Rect(315, 575, 70, 70)
currentColorRect = Rect(320, 580, 60, 60)

#DISPLAYING THE UNCHANGING RECTS
draw.rect(screen, LIGHTBLUE, currentColorBKGD)
draw.rect(screen, WHITE, currentColorRectBKGD)


#THICKNESS CONTORLS-------------------------------------------------------------
#LOADING BUTTON ICONS
smallerRadius = image.load("Pics/next stamp.png")
biggerRadius = image.load("Pics/prev stamp.png")

#ICONS THAT ARE ONLY USED IF BUTTON CANNOT BE CLICKED
smallerRadiusGrey = image.load("Pics/next grey.png")
biggerRadiusGrey = image.load("Pics/prev grey.png")

#MAKING THE RECTS (for collidepoint)
smallerRadiusRect = Rect(990, 77, 30, 30)
biggerRadiusRect = Rect(1030, 77, 30, 30)

#MAKING AND DISPLAYING THE BACKGROUND
thicknessBackground = Rect(890, 65, 280, 50)
thicknessDisplayBKGD = Rect(1070, 70, 95, 40) #this one is drawn later with the actual thickness bar 
draw.rect(screen, LIGHTBLUE, thicknessBackground)

#BLITTING THE DEFAULT BUTTONN ICONS
screen.blit(smallerRadius, (990, 77))
screen.blit(biggerRadius, (1030, 77))

#EXPLANATION BOX----------------------------------------------------------------
#MAKING AND DRAWING THE EXPLANATION BOX
explanationRect = Rect(20, 365, 230, 125)
draw.rect(screen, LIGHTBLUE, explanationRect)


#TEXT---------------------------------------------------------------------------
#LOADING ALL THE FONTS
arial = font.SysFont("Arial", 20)
arialTitle = font.SysFont("Arial", 40)
arialTitle.set_bold(True)

#TOOL EXPLANAITON FILE ADRESSES
explainFileNames = ["Pics/explains/pencil explain.png", "Pics/explains/eraser explain.png", "Pics/explains/brush explain.png",
                    "Pics/explains/color picker explain.png", "Pics/explains/rectangle explain.png", "Pics/explains/circle explain.png",
                    "Pics/explains/triangle explain.png", "Pics/explains/polygon explain.png", "Pics/explains/line explain.png",
                    "Pics/explains/roller explain.png", "Pics/explains/spray paint explain.png", "Pics/explains/select explain.png",
                    "Pics/explains/clear explain.png", "Pics/explains/text explain.png", "Pics/explains/save explain.png",
                    "Pics/explains/open explain.png", "Pics/explains/undo explain.png", "Pics/explains/redo explain.png"]

#TOOLS WITH EXPLANATIONS THAT AREN'T IN "hover tools"
backgroundText = image.load("Pics/explains/backgrounds.png")
stampText = image.load("Pics/explains/stamps.png")
defaultText = image.load("Pics/explains/default.png")

#position that all these images will be loaded at
explainTextPos = (20, 365)

#MAKING LIST OF TOOL EXPLANATIONS
explainTexts = []
for name in explainFileNames:
    explainTexts.append(image.load(name))

#OTHER TEXT
title = arialTitle.render("P E R C Y   J A C K S O N   P A I N T", True, LIGHTBLUE)
thickness = arial.render("thickness: ", True, BLACK)
fillText = arial.render("fill:", True, WHITE)
currentColor = arial.render("current:", True, BLACK)

defaultTexts = [thickness, fillText, currentColor, title]
textPos = [(900, 77), (180, 318), (325, 545), (315, 15)]

#LOADING THE TEXTS
for t in range(len(defaultTexts)):
    screen.blit(defaultTexts[t], textPos[t])


#MAKING THE CANVAS--------------------------------------------------------------
canvasRect = Rect(400, 125, 780, 550)
draw.rect(screen, WHITE, canvasRect)


#STAMPS AND BACKGROUNDS----------------------------------------------------------
#IMPORTING ICONS
prevIcon = image.load("Pics/prev bkgd.png")
nextIcon = image.load("Pics/next bkgd.png")

#STAMPS RECTS
prevStampRect = Rect(275, 350, 100, 20)
nextStampRect = Rect(275, 470, 100, 20)
showStampRect = Rect(275, 370, 100, 100)

#BACKGORUND PATTERNS RECTS
prevBackgroundRect = Rect(260, 150, 130, 20)
nextBackgroundRect = Rect(260, 305, 130, 20)
showBackgroundRect = Rect(260, 170, 130, 135)

#DRAWING BUTTONS AND BACKGROUNDS FOR BOTH STAMPS AND BACKGROUNDS
draw.rect(screen, LIGHTBLUE, prevStampRect)
draw.rect(screen, LIGHTBLUE, nextStampRect)
draw.rect(screen, LIGHTBLUE, prevBackgroundRect)
draw.rect(screen, LIGHTBLUE, nextBackgroundRect)
screen.blit(prevIcon, (320, 353))
screen.blit(nextIcon, (320, 473))
screen.blit(prevIcon, (320, 153))
screen.blit(nextIcon, (320, 308))


#MUSIC PLAYER--------------------------------------------------------------------
#LOADING MUSIC BUTTON ICONS
prevSong = image.load("Pics/music/prev song.png")
nextSong = image.load("Pics/music/next song.png")
playing = image.load("Pics/music/playing.png")
paused = image.load("Pics/music/paused.png")
volumeUp = image.load("Pics/music/volume up.png")
volumeDown = image.load("Pics/music/volume down.png")
restart = image.load("Pics/music/restart.png")

#LIST OF DEFAUlT ICONS
musicIcons = [prevSong, paused, nextSong, restart, volumeUp, volumeDown]

#LIST OF SONGS' FILE ADDRESSES
#Note: some songs start off with no sound
songs = ["Music/BOBD.ogg", "Music/LEU.ogg", "Music/TIW.ogg", "Music/HOO.ogg",
         "Music/S.ogg", "Music/YV.ogg"]

#NAMES OF THE SONGS RENDERED AS TEXT TO DISPLAY
bobd = arial.render("Boulevard of Broken Dreams", True, BLACK)
leu = arial.render("Light 'Em Up", True, BLACK)
tiw = arial.render("This is War", True, BLACK)
hoo = arial.render("Heroes of Olympus", True, BLACK)
s = arial.render("Soldatino", True, BLACK)
yv = arial.render("Young Volcano", True, BLACK)

#LIST OF SONG NAMES
songNames = [bobd, leu, tiw, hoo, s, yv]

#MUSIC BUTTONS (for collidepoint)
musicRect = Rect(270, 70, 600, 40)
prevSong = Rect(560, 75, 30, 30)
pauseSong = Rect(595, 75, 30, 30)
nextSong = Rect(630, 75, 30, 30)
restartSong = Rect(665, 75, 30, 30)
volumeDown = Rect(700, 80, 20, 20)
volumeUp = Rect(845, 80, 20, 20)
volumeRect = Rect(volumePosX-4, 86, 8, 8)

musicButtons = [prevSong, pauseSong, nextSong, restartSong, volumeDown, volumeUp]

#drawing music player background
draw.rect(screen, LIGHTBLUE, musicRect)

#drawing music player border
draw.rect(screen, BLUE, (267, 67, 606, 46), 3)

#drawing the line for the volume slider
draw.line(screen, BLUE, (725, 90), (840, 90), 3)

#BLITTING EACH ICON
for icon in range(len(musicIcons)):
    screen.blit(musicIcons[icon], musicButtons[icon])

#taking a screenshot of the unchanging buttons and rectangles to blit later when user is moving volume slider
musicCap = screen.subsurface(musicRect).copy()


#BORDERS--------------------------------------------------------------------
#DRAWING BORDERS FOR AREAS TO MAKE IT LOOK BETTER VISUALLY
draw.rect(screen, BLUE, (17, 497, 286, 193), 3) #PALETTE BORDER
draw.rect(screen, BLUE, (307, 537, 86, 116), 3) #CURRENT COLOR BORDER
draw.rect(screen, BLUE, (887, 62, 286, 56), 3) #THICKNESS BORDER
draw.rect(screen, BLUE, (17, 362, 236, 131), 3) #EXPLAIN BOX BORDER
draw.rect(screen, BLUE, (272, 347, 106, 146), 3) #STAMP BORDER
draw.rect(screen, BLUE, (257, 147, 136, 181), 3) #BKGD BORDER
draw.rect(screen, BLUE, (397, 122, 786, 556), 3) #CANVAS BORDER

    
#SCREENSHOTS-----------------------------------------------------------------
##taking screenshots to blit later when needed (and to add to undo and redo lists)
canvasCap = screen.subsurface(canvasRect).copy()
toolCap = screen.subsurface((10, 50, 245, 310)).copy()


#UNDO AND REDO LISTS--------------------------------------------------------
undoList = [canvasCap] #starts off with the blank canvas
redoList = []


#OTEHR LISTS-----------------------------------------------------------------
polygonPoints = [] #list that stores the points for the polygon

#all of the tools that will have a different color border when mouse hovers over it
hoverTools = [t for t in tools] + [saveRect, openRect, undoRect, redoRect]


#FILL------------------------------------------------------------------------
#CHECKMARK IMAGE FOR FILL
fillCheck = image.load("Pics/check.png")

#MAKING AND DRAWING FILL BOX
fillRect = Rect(210, 320, 20, 20)
draw.rect(screen, WHITE, fillRect)


running = True

while running:
   
    for evt in event.get():
        
        keys = key.get_pressed() #gets which keys are pressed
        
        if evt.type == QUIT:
            running = False

            
        #IF LEFT CLICK OR CTRL IS PRESSED----------------------------------------------------------------------------------------------------
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1 or keys[K_LCTRL]:
            
            #GETTING STARTING POSITIONS (for tools that need starting and end positions, eg. pencil, rectangle, circle, etc.)
            startx, starty = mouse.get_pos() #changes everytime the loop runs - updated at the end of the loop (for pencil, eraser, brush)
            clickx, clicky = mouse.get_pos() #unchanging (for rectangle, circle, etc.)
            

            #SAVE IMAGE----------------------------------------------------------------------------------------------------
            #if save button is clicked or if user typed "S" (CTRL + S)
            if saveRect.collidepoint(mx, my) or keys[K_s]:
                #gets name/location for where user wants to save their file
                fileName = filedialog.asksaveasfilename(defaultextension = ".png")
                if fileName != "": #if they didnt click cancel
                    image.save(screen.subsurface(canvasRect), fileName) #saves image at inputted file location

                tool = None #so that it won't automatically resume drawing wherever your mouse goes even while you don't press down


            #LOAD IMAGE----------------------------------------------------------------------------------------------------
            #if load button is clicked or if user typed "O" (CTRL + O)
            if openRect.collidepoint(mx, my) or keys[K_o]:
                #gets name/location of file (thats either "PNG" or "JPG") that user choses
                loadFileName = filedialog.askopenfilename(filetypes = (("PNG File", ".png"), ("JPG File", ".jpg")))
                if loadFileName != "": #if they didnt click cancel
                    loadedImage = image.load(loadFileName) #loads the image
                    #if the image is bigger than the canvas, shrink image but keep the same ratio
                    if loadedImage.get_width() > 780: #if it's wider
                        loadedImage = transform.scale(loadedImage, (780, int(loadedImage.get_height()/(loadedImage.get_width()/780))))
                    if loadedImage.get_height() > 550: #if it's taller
                        height = (int(loadedImage.get_width()/(loadedImage.get_height()/550)))
                        loadedImage = transform.scale(loadedImage, (height, 550))
                    #clear the canvas before blitting the selected image
                    draw.rect(screen, WHITE, canvasRect)
                    screen.blit(loadedImage, canvasRect).copy()

                tool = None #so that it won't automatically start drawing wherever your mouse goes even while you don't press down


            #UNDO AND REDO------------------------------------------------------------------------------------------------
            #if undo button is clicked or if user typed "Z" (CTRL + Z)
            if undoRect.collidepoint(mx, my) or keys[K_z]:
                if len(undoList) > 1: #if there isn't just the one original blank canvasCap/if the user drew something
                    redoList.append(undoList.pop()) #moves the most recent canvasCap (the screenshot of the current canvas) to the redoList
                    screen.blit(undoList[-1], canvasRect) #blits the second most recent canvasCap taken
            #if redo button is clicked or if user typed "Y" (CTRL + Y)
            if redoRect.collidepoint(mx, my) or keys[K_y]:
                if len(redoList) != 0: #if the list isn't empty/the user has clicked undo before
                    undoList.append(redoList.pop()) #moves the first redo canvasCap to the undoList
                    screen.blit(undoList[-1], canvasRect) #blits that canvasCap


            #CLICKING ON TOOLS-------------------------------------------------------------------------------------------------
            for option in range(14): #runs through all the tools
                if tools[option].collidepoint(mx, my): #whichever tool (mx, my) is colliding with, the variable "tool" is set to that tool's name
                    tool = toolNames[option]
                    selectedTool = option #gets the index of the selected tool to use for drawing border later

            #if stamps or backgrounds are clicked(since there is no tool button for stamps and backgrounds)
            if showStampRect.collidepoint(mx, my) or showBackgroundRect.collidepoint(mx, my):
                tool = "stamp"


            #if the user clicks on the CLEAR tool
            if tool == "clear" and clearRect.collidepoint(mx, my):
                draw.rect(screen, WHITE, canvasRect) #draw a blank canvas
                backgroundPattern = False #if there was a background pattern used, it's not used anymore so backgroundPattern has to be False (no pattern)


            #FILL OR UNFILL----------------------------------------------------------------------------------------------------
            #if the user clicked on the fill box
            if fillRect.collidepoint(mx, my):
                if fillSelect == True: #if fill is selected, unselect it
                    fillSelect = False
                else:
                    fillSelect = True #otherwise select it


            #STAMPS----------------------------------------------------------------------------------------------------
            if prevStampRect.collidepoint(mx, my): #if user clicked on previous stamp button
                stampPos = (stampPos - 1 + len(stamps)) % len(stamps) #current stamp position moves up/less one
                #blits the stamp at the new stamp position
                currentStamp = stamps[stampPos].subsurface(24, 0, 100, 100) 
                screen.blit(currentStamp, (275, 370))
                
            if nextStampRect.collidepoint(mx, my): #if user clicked on next stamp button
                stampPos = (stampPos+1) % len(stamps) #current stamp position moves down/more one
                #blits the stamp at the new stamp position
                currentStamp = stamps[stampPos].subsurface(24, 0, 100, 100)
                screen.blit(currentStamp, (275, 370))

            #if the user clicked on the stamp itself (to drag onto the canvas and use)
            if showStampRect.collidepoint(mx, my):
                sticker = stamps[stampPos] #set variable "sticker" to current clicked on stamp
                #"sticker" is what will be shown when the user holds and drags mouse around on canvas


            #BACKGROUNDS----------------------------------------------------------------------------------------------------
            if prevBackgroundRect.collidepoint(mx, my): #if user clicked on previous background button
                backgroundPos = (backgroundPos - 1 + len(BKGDPatterns)) % len(BKGDPatterns) #current background position moves up/less one
                #blits the background at the new background position
                currentBKGD = transform.scale(BKGDPatterns[backgroundPos], (260, 170))
                screen.blit(currentBKGD.subsurface(50, 0, 130, 135), (260, 170))
            
            if nextBackgroundRect.collidepoint(mx, my): #if user clicked on next background button
                backgroundPos = (backgroundPos+1) % len(BKGDPatterns) #current background position moves down/more one
                #blits the background at the new background position
                currentBKGD = transform.scale(BKGDPatterns[backgroundPos], (231, 135))
                screen.blit(currentBKGD.subsurface(50, 0, 130, 135), (260, 170))

            #if the user clicked on the background itself (to drag onto the canvas and use)
            if showBackgroundRect.collidepoint(mx, my):
                sticker = BKGDPatterns[backgroundPos] #set variable "sticker" to current clicked on background


            #RADIUS/THICKNESS SIZE----------------------------------------------------------------------------------------------------
            if smallerRadiusRect.collidepoint(mx, my): #to make thickness smaller
                if radius > 2: #to make sure radius wont go into the negatives
                    radius -= 2
            if biggerRadiusRect.collidepoint(mx, my): #to make thickness larger
                if radius < 28: #maximum radius is 30 so to add 2, radius can't be higher than 28 
                    radius += 2

            
            #COLOR DROPPER----------------------------------------------------------------------------------------------------
            if tool == "dropper": #if dropper is selected
                #user can pick custom color from color palette or from the canvas
                if canvasRect.collidepoint(mx, my) or paletteRect.collidepoint(mx, my):
                    col = screen.get_at((mx,my)) #set color to color at the place where the mouse is clicked
                    


            #DRAWING POLYGONS----------------------------------------------------------------------------------------------------
            if tool == "polygon" and canvasRect.collidepoint(mx, my): #if the polygon tool is selected and they are LEFT CLICKING on the canvas
                drawPoly = True #currently drawing polygon
                                #used for telling program to not add screenshots to undoList until finshed drawing polygons
                polygonPoints.append((clickx, clicky)) #adds current click location to list of points for the polygon


            #takes a screenshot everytime mouse is clicked to constantly refresh display as new things are added
            canvasCap = screen.subsurface(canvasRect).copy()


            #MUSIC PLAYER----------------------------------------------------------------------------------------------------
            #PREVIOUS SONG
            if prevSong.collidepoint(mx, my): #if user clicked on the button for previous song
                songPos = (songPos - 1 + len(songs)) % len(songs) #the song position moves back
                playOrPause = 1 #is set to 1 since it will automatically start playing and 1 means currently playing
                mixer.music.load(songs[songPos]) #loads song at new song position and starts playing
                mixer.music.play()

            #NEXT SONG
            if nextSong.collidepoint(mx, my):#if user clicked on the button for next song
                songPos = (songPos + 1) % len(songs) #the song position moves forward
                playOrPause = 1 #is set to 1 since it will automatically start playing and 1 means currently playing
                mixer.music.load(songs[songPos]) #loads song at new song position and starts playing
                mixer.music.play()

            #RESTART SONG
            if restartSong.collidepoint(mx, my): #if user clicked to restart current song
                mixer.music.rewind() #rewind/restart

            #PAUSE/PLAY
            if pauseSong.collidepoint(mx, my): #if user clicked on pause/play
                if playOrPause == 0: #if its the first time the user clicked play
                    mixer.music.load(songs[songPos]) #need to load the music first
                    mixer.music.play() #plays music after loading
                    playOrPause = 1 #becomes 1 for currently playing as its now playing
                elif playOrPause == 1: #if currently playing music
                    mixer.music.pause() #pauses the music                
                    playOrPause = 2 #2 is for paused
                elif playOrPause == 2: #if currently paused
                    mixer.music.unpause() #unpauses music
                    playOrPause = 1 #goes back to 1 (playing)

            #VOLUME CHANGE
            if volumeRect.collidepoint(mx, my): #if user clicks on the volume marker on the slider
                volumeChange = True #tells program user is currently changing the volume
                                    #(even if the users mouse doesn't always collidepoint with the volume marker as they drag, volume will change)


        #IF LEFT CLICK IS PRESSED OR UP/DOWN KEYS OR M KEY----------------------------------------------------------------------------------------------------
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1 or keys[K_UP] or keys[K_DOWN] or keys[K_m]:
            if volumeDown.collidepoint(mx, my) or keys[K_DOWN]: #if volume down or down arrow is clicked
                if volumePosX >= 730: #min volume is 725
                    volumePosX -= 5 #changing the positon of the marker on the slider
                    mixer.music.set_volume((volumePosX-725)/115) #changing the actual volume
                    
            if volumeUp.collidepoint(mx, my) or keys[K_UP]: #if volume up or up arrow is clicked
                if volumePosX <= 840: #max vol is 845
                    volumePosX += 5 #changing the positon of the marker on the slider
                    mixer.music.set_volume((volumePosX-725)/115) #changing the actual volume

            if keys[K_m]: #instead of dragging, if user directly clicks "M", volume will mute
                volumePosX = 725
                mixer.music.set_volume(0)


        #WHEN SONG FINISHES PLAYING----------------------------------------------------------------------------------------------------             
        if evt.type == MUSICEND:
            songPos = (songPos + 1) % len(songs) #move song position one up (to the next song in line)
            playOrPause = 1 #will automatically start playing so its set to 1
            mixer.music.load(songs[songPos]) #load and play song
            mixer.music.play()


        #IF RIGHT CLICK IS PRESSED (finished drawing polygon)--------------------------------------------------------------------------------------
        if evt.type == MOUSEBUTTONDOWN and evt.button == 3:
            clickx, clicky = mouse.get_pos() #gets location of mouse click
            if tool == "polygon" and canvasRect.collidepoint(mx, my): #if selected tool is polygon and mouse is on canvas
                polygonPoints.append((clickx, clicky)) #add current location to the list of points for the polygon
            if len(polygonPoints) > 2: #if there are more than 2 points (polygons needs at least 3 points)
                drawPoly = False #user has finished drawing polygon so drawPoly becomes False
                draw.polygon(screen, col, polygonPoints, fill) #drawing the polygon
                polygonPoints = [] #clearing the list of points for the next polygon
            canvasCap = screen.subsurface(canvasRect).copy() #updating canvas with new polygon

            
        #IF MOUSE IS LIFTED----------------------------------------------------------------------------------------------------
        if evt.type == MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx, my) or tool == "clear" and clearRect.collidepoint(mx, my): #if mouse on canvas or user clicked clear tool
                                                        #(clear tool acts just like drawing tools but mouse won't collidepoint with canvas so this condition must be added)
                if tool == "stamp":
                    if backgroundPattern == True: #if user selected a background pattern and dropped it onto the screen
                        if h == 600: #if the current stamp being used is a background pattern (and not a regular stamp)
                            screen.set_clip(canvasRect) #set clip so background pattern wont run off the canvas
                            screen.blit(sticker, canvasRect) #blit the background sticker perfectly on the canvas (regardless of where the user dropped it)
                            screen.set_clip(None)

                if tool == "select": #if tool is select and the mouse is lifted
                    screen.blit(canvasCap, canvasRect) #blit canvasCap again to get rid of the grey box that is drawn for select
                    sticker = screen.subsurface(myRect).copy() #(myRect is the selected area) selected area becomes a custom stamp
                    tool = "stamp" #tool becomes stamp to use the custom stamp

                #if not currently drawing polygon, picking a color, or making custom text stamp, but has tool selected
                #(elif so that if tool was "select", it wouldn't append to undoList here once, then again with 'if tool == "stamp"')
                elif drawPoly == False and tool != None and tool != "dropper" and tool != "text": 
                    canvasCap = screen.subsurface(canvasRect).copy() #takes screenshot of canvas
                    undoList.append(canvasCap) #adds screenshot to undoList
                    redoList = [] #redoList has to be cleared since user drew something new and there isn't anything to 'redo' to

            if volumeChange: #is user was changing the volume and lifted mouse
                volumeChange = False #volume will stop being changed


        #IF USER TYPES ON KEYBOARD (while text tool is selected for making custom text stamp)---------------------------------------------------------------
        if evt.type == KEYDOWN and tool == "text":  
            if evt.key == K_BACKSPACE: #if user hit backspace
                word = word[:-1] #take off the last letter of the string
                sticker = arial.render(word, True, col) #render the text as an image
                h = sticker.get_height()
                w = sticker.get_width()
                if canvasRect.collidepoint(mx, my): #if mouse is on canvas blit the sticker
                    screen.blit(canvasCap, canvasRect) #reblit canvasCap so that the sticker won't be blitted ontop of itself every time
                    screen.blit(sticker, (mx - w//2, my - h//2))
            if evt.key == K_RETURN: #if user hits enter
                tool = "stamp" #tool becomes stamp and user will be able to use custom text sticker like a stamp
                selectedTool = -1 #no tool is selected anymore as there is no stamp tool
                word = "" #clears word for next use
            else:
                word += chr(evt.key) #adds every letter typed onto the end of the existing string
                sticker = arial.render(word, True, col) #renders the text as an image
                h = sticker.get_height()
                w = sticker.get_width()
                if canvasRect.collidepoint(mx, my): #if mouse is on canvas blit the sticker
                    screen.blit(canvasCap, canvasRect) #reblit canvasCap so that the sticker won't be blitted ontop of itself every time
                    screen.blit(sticker, (mx - w//2, my - h//2))

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    #TOOLS----------------------------------------------------------------------------------------------------        
    screen.blit(toolCap, (10, 50)) #reblit screenshot of tools so the old hovering and selected border will be erased
    screen.blit(defaultText, explainTextPos) #blit the default text that shows up when mouse isn't hovering over any tool

    #HOVERING----------------------------------------------------------------------------------------------------
    for b in range(len(hoverTools)):
        if hoverTools[b].collidepoint(mx, my): #if mouse is hovering over any of the tools that will change when mouse hovers over it
            draw.rect(screen, LIGHTBLUE, hoverTools[b], 4) #draw a new border around that tool
            screen.blit(explainTexts[b], explainTextPos) #blit the explanaiton for that tool in the explanation box

    #SELECTING----------------------------------------------------------------------------------------------------
    if tool in toolNames: #if a tool (that can be selected(has an icon)) is selected (excluding backgrounds and stamps)
        draw.rect(screen, DARKBLUE, tools[selectedTool], 4) #draw a new border (that's different from the hover border) around the tool


    #THICKNESS DISPLAY----------------------------------------------------------------------------------------------------
    draw.rect(screen, WHITE, thicknessDisplayBKGD) #redraw white background everytime so smaller thicknesses can be visible even if there was a thicker thickness previously
    thicknessDisplayRect = Rect(1080, 90-radius//2, 75, radius) #making and drawing a rectangle with the current radius
    draw.rect(screen, col, thicknessDisplayRect)
    

    #CURRENT COLOR----------------------------------------------------------------------------------------------------
    draw.rect(screen, col, currentColorRect) #drawing the currentColorRect in the current color
    

    #UNDO AND REDO BUTTONS----------------------------------------------------------------------------------------------------
    if len(undoList) > 1: #if user is able to click the undo button (images were appended to undoList)
        screen.blit(undoIcon, (130, 70)) #blit the black icon
    else:
        screen.blit(undoGreyIcon, (130, 70)) #else, blit the grey icon (to indicate it can't be clicked)
        
    if len(redoList) > 0: #if user is able to click the redo button
        screen.blit(redoIcon, (180, 70))  #blit the black icon
    else:
        screen.blit(redoGreyIcon, (180, 70)) #else, blit the grey icon (to indicate it can't be clicked)


    #RADIUS/THICKNESS----------------------------------------------------------------------------------------------------
    if radius <= 2: #if radius can't go any smaller (user can't click)
        draw.rect(screen, LIGHTBLUE, smallerRadiusRect) #blit the grey icon
        screen.blit(smallerRadiusGrey, (990, 77))
    else:
        draw.rect(screen, LIGHTBLUE, smallerRadiusRect) #otherwise, blit the black one
        screen.blit(smallerRadius, (990, 77))
        
    if radius >= 28: #if radius can't go any bigger
        draw.rect(screen, LIGHTBLUE, biggerRadiusRect) #blit the grey icon
        screen.blit(biggerRadiusGrey, (1030, 77))
    else:
        draw.rect(screen, LIGHTBLUE, biggerRadiusRect) #otherwise, blit the black one
        screen.blit(biggerRadius, (1030, 77))


    #FILL----------------------------------------------------------------------------------------------------
    if fillSelect == True: #if fill is selected
        draw.rect(screen, WHITE, fillRect) #drawing and blitting the checkmark in the white box
        screen.blit(fillCheck, (210, 320))
        fill = 0 #fill has value 0 so since shapes with value 0 are filled
    else:
        draw.rect(screen, WHITE, fillRect) #else, take off check by drawing white square over it
        fill = radius #the shapes thicknesses would just be the radius


    #MUSIC PLAYER----------------------------------------------------------------------------------------------------
    #reblitting musicCap incase any changes are made, so they dont appear ontop of each other
    screen.blit(musicCap, musicRect)

    if playOrPause == 1: #if song is playing
        screen.blit(playing, pauseSong) #blit the playing icon
    elif playOrPause == 2: #otherwise blit the paused icon
        screen.blit(paused, pauseSong)

    #draw the volume marker at the current volume position
    draw.circle(screen, BLUE, (volumePosX, 90), 4)

    #blit the current song name
    screen.blit(songNames[songPos], (280, 77))

    #if the user is currently changing the volume
    if volumeChange:
        if 725 <= mx <= 840: #if the volume marker is within proper range
            volumePosX = mx #the (x) position will be the positon of the mouse
            volumeRect = Rect(volumePosX-4, 86, 8, 8) #updating the Rect to where the volume marker currently is (so that the Rect will be correct for collidepoint)
            mixer.music.set_volume((volumePosX-725)/115) #changing the actual volume 
            draw.circle(screen, BLUE, (volumePosX, 90), 3) #drawing the volume marker at the new position


    #STAMPS AND BACKGROUNDS----------------------------------------------------------------------------------------------------
    currentStamp = stamps[stampPos].subsurface(24, 0, 100, 100) #preview (cropped section) of the current stamp being displayed
    currentBKGD = transform.scale(BKGDPatterns[backgroundPos], (231, 135)) #preview of the current background pattern being displayed

    #blitting the two previews
    screen.blit(currentStamp, (275, 370)) 
    screen.blit(currentBKGD.subsurface(50, 0, 130, 135), (260, 170))

    #if user hovered over the stamp, blit the explanation for using stamps
    if showStampRect.collidepoint(mx, my):
        screen.blit(stampText, explainTextPos)

    #if user hovered over the background patterns, blit the explanation for using them
    if showBackgroundRect.collidepoint(mx, my):
        screen.blit(backgroundText, explainTextPos)   


    #COLOR PICKING/USING THE PALETTE-----------------------------------------------------------------------------------------------
    if tool == "dropper":
        
        #if dropper hovers over palette, crosshair will appear
        screen.blit(palette, (20, 500)) #reblitting to cover all old crosshairs so it'll only show one at any given time
        if paletteRect.collidepoint(mx, my):
            screen.set_clip(paletteRect) #clipping to the palette so that the crosshair only shows up on the palette

            #drawing the crosshair
            draw.circle(screen, BLACK, (mx, my), 10, 1)
            draw.line(screen, BLACK, (mx, my+10), (mx, my+4))
            draw.line(screen, BLACK, (mx, my-10), (mx, my-4))
            draw.line(screen, BLACK, (mx-10, my), (mx-4, my))
            draw.line(screen, BLACK, (mx+10, my), (mx+4, my))


    #PREPPING FOR ACTUAL DRAWING-----------------------------------------------------------------------------------------------
    #clipping to the canvas so drawings only appear on canvas
    screen.set_clip(canvasRect)

    #if tool is one that needs constant reblitting of the canvas (to erase old shapes as user changes the size of these shapes or drags them around)
    if tool in screenCapTools:
        screen.blit(canvasCap, canvasRect) #reblit canvasCap


    #ACTUALLY DRAWING SHAPES AND LINES-----------------------------------------------------------------------------------------------
    if mb[0] and canvasRect.collidepoint(mx, my): #if the user clicked and dragged on the canvas
        
        #TOOLS-----------------------------------------------------------------------------------------------
        if tool == "pencil":
            draw.line(screen, col, (startx, starty), (mx, my), 1) #constantly drawing small lines from the last point the mouse was at to the current point
            
        if tool == "eraser":
            if backgroundPattern == False: #if there is no background pattern used

                #getting the distances
                dx = mx - startx
                dy = my - starty
                dist = sqrt(dx**2 + dy**2)

                #for every point in between last and current mouse position, draw a white circle (so that there won't be spaces that weren't covered if the mouse moves fast)
                for d in range(int(dist)): 
                    dotX = startx + d * dx/dist
                    dotY = starty + d * dy/dist
                    draw.circle(screen, WHITE, (int(dotX), int(dotY)), radius)
                    
            else: #if there is a background pattern
                
                if radius <= mx-400 <= 780-radius and radius <= my-125 <= 550-radius: #if the mouse is within range
                    #getting a small subsurface of the background pattern at the current mouse position and drawing it (to remove anythign that isn't the background pattern)
                    eraser = BKGDPatterns[backgroundPos].subsurface((mx-400-radius, my-125-radius, radius*2, radius*2))
                    screen.blit(eraser, (mx-radius, my-radius)) #blitting the subsurface
                        
        if tool == "brush":

            #getting the distances
            dx = mx - startx
            dy = my - starty
            dist = sqrt(dx**2 + dy**2)

            #for every point in between last and current mouse position, draw a white circle (so that there won't be spaces that weren't covered if the mouse moves fast)
            for d in range(int(dist)):
                dotX = startx + d * dx/dist
                dotY = starty + d * dy/dist
                draw.circle(screen, col, (int(dotX), int(dotY)), radius)
                
        if tool == "rect":
            #using clickx and clicky because they don't get updated everytime the loop runs (is the positon the mouse clicked on before dragging)
            myRect = Rect(clickx, clicky, mx-clickx, my-clicky)  #making a rect from the starting position to the current position
            myRect.normalize() #normalizing and blitting it
            draw.rect(screen, col, myRect, fill)
            
        if tool == "circle":
            #using clickx and clicky because they don't get updated everytime the loop runs (is the positon the mouse clicked on before dragging)
            myRect = Rect(clickx, clicky, mx-clickx, my-clicky) #making an ellipse from the starting position to the current position
            myRect.normalize()#normalizing and blitting it
            draw.ellipse(screen, col, myRect, fill)
            
        if tool == "triangle":
            #using clickx and clicky because they don't get updated everytime the loop runs (is the positon the mouse clicked on before dragging)
            myRect = Rect(clickx, clicky, mx-clickx, my-clicky) #making a triangle from the starting position to the current position
            myRect.normalize()#normalizing and blitting it
            draw.polygon(screen, col, [((mx-clickx)//2+clickx, clicky), (clickx, my), (mx, my)], fill) #points are calculated and made based on the "rectangle" that the user's mouse made
            
        if tool == "line":
            #using clickx and clicky because they don't get updated everytime the loop runs (is the positon the mouse clicked on before dragging)
            draw.aaline(screen, col, (clickx, clicky), (mx, my), radius)
            
        if tool == "roller":
            draw.rect(screen, col, canvasRect) #filling the canvas with the current color
            
        if tool == "spray":
            sprayRad = radius*2 #making a radius size for spray paint
            x = randint(mx-sprayRad, mx+sprayRad) #getting random coordinates
            y = randint(my-sprayRad, my+sprayRad)

            #if the coordinates fall within the circle with sprayRad radius, draw a small circle at that position (so the spray paint will be circular and not square)
            if sqrt((x-mx)**2+(y-my)**2) <= sprayRad: 
                draw.circle(screen, col, (x, y), 1)
                
            myClock.tick(900) #setting the rate that the random points will appear
            
        if tool == "select":
            if canvasRect.collidepoint(mx, my): #if user is selecting something on the canvas

                #is like rectangle tool but drawing a grey rectangle with thickness 1 instead
                #(this rectangle will be erased when the user lets go, and the selected area will be turned into a stamp)
                myRect = Rect(clickx, clicky, mx-clickx, my-clicky)
                myRect.normalize()
                draw.rect(screen, GREY, myRect, 1)
                
        if tool == "stamp":

            #getting the height and width of the stamp that the user selected to determine where to blit the stamp
            h = sticker.get_height()
            w = sticker.get_width()
            screen.blit(sticker, (mx - w//2, my - h//2)) #blitting the stamp
            
            if h == 600 and w == 780: #if the stamp is a background pattern (background patterns have that size)
                backgroundPattern = True #setting it to true since it's being used
                

    #if the user is currently drawing a polygon (clicking the points)
    if drawPoly == True:
        
        #it's as if user is using line tool from last point they clicked to current mouse position
        draw.line(screen, col, (clickx, clicky), (mx, my), radius)            

    screen.set_clip(None) #taking off the clip so the program can change things outside the canvas again
    
    startx, starty = mx, my #updating the starting positons to the current position for the next loop/move
    
    display.flip()
            
quit()
