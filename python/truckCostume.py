import time
import random
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
ledStrip = dotstar.DotStar(board.D2, board.D3, 60, brightness=.05, auto_write=False)

# HELPERS
# a random color 0 -> 255
def random_color():
  return random.randrange(0, 255)

orange = (255,128,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

# Initialize our light arrays
NUM_HEAD_LIGHTS = 5
headLight = list()
for i in range(NUM_HEAD_LIGHTS):
  headLight.append(white)

NUM_ENGINE_LIGHTS = 15
engineLight = list()
for i in range(NUM_ENGINE_LIGHTS / 3):
  engineLight.append(white)
  engineLight.append(black)
  engineLight.append(black)

NUM_TAIL_LIGHTS = 6
tailLights = list()
for i in range(2):
  tailLights.append(red)
  tailLights.append((96,0,0))
  tailLights.append((28,0,0))

NUM_WINGTIP_LIGHTS = 2
wingtipLights = [black,red]
wingTipLeft = [black]
wingTipRight = [red]

x = 1
# MAIN LOOP
n_dots2 = len(ledStrip)

# Clear the strip
def Clear():
  ledStrip.fill((0,0,0))
  ledStrip.show()

# Draws the whole strip
def Draw():  
  colors = list()
  colors = headLight + headLight + engineLight + wingTipLeft + tailLights + engineLight + wingTipRight
  
  for i in range(len(colors)):
    ledStrip[i] = colors[i]

  ledStrip.show()

# Flashes the wingtip lights
def UpdateWingtips():
  #global wingtipLights
  global wingTipLeft
  global wingTipRight

  if wingTipLeft[0] == black: 
    wingTipLeft = [green]
  else: 
    wingTipLeft = [black]

  if wingTipRight[0] == black: 
    wingTipRight = [red]
  else: 
    wingTipRight = [black]
  
  
# Animate the engine lights (rotate)
def UpdateEngines():
  global engineLight
  engineLight.append(engineLight[0])
  engineLight.pop(0)


