import time
import random
import board
import adafruit_dotstar as dotstar
import truckCostume

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
ledOnboard = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
ledOnboard[0] = (0,0,255)

# CONSTANTS
orange = (255,128,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)

# INIT
truckCostume.Clear()

# Define a head light 
NUM_HEAD_LIGHTS = 5
headLight = list()
for i in range(NUM_HEAD_LIGHTS):
  headLight.append(white)

# Define an engine light
NUM_ENGINE_LIGHTS = 15
engineLight = list()
for i in range(NUM_ENGINE_LIGHTS / 3):
  engineLight.append(white)
  engineLight.append(black)
  engineLight.append(black)

# Define a tail light
NUM_TAIL_LIGHTS = 3
tailLight = list()
for i in range(NUM_TAIL_LIGHTS):
  tailLight.append(red)

# Define wing tip lights
wingTipLeft = [green,black]
wingTipRight = [black,red]

# HELPERS
# a random color 0 -> 255
def random_color():
  return random.randrange(0, 255)

# the loop counter for use in timing, from 1 to maxLoopCount
loopCount = 1
maxLoopCount = 5

while True:
  colors = list()
  colors = headLight + headLight + engineLight + wingTipLeft[0] + tailLight + tailLight + engineLight + wingTipRight[0]
  truckCostume.Draw(colors)
  time.sleep(.1)

  if loopCount >= 1:
    engineLight = truckCostume.UpdateEngine(engineLight)

  if loopCount >= 5:
    wingTipLeft = truckCostume.UpdateWingtip(wingTipLeft)
    wingTipRight = truckCostume.UpdateWingtip(wingTipRight)
  
  loopCount += 1
  if loopCount > maxLoopCount: loopCount = 1

"""
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
ledStrip = dotstar.DotStar(board.D2, board.D3, 60, brightness=.05, auto_write=False)
"""