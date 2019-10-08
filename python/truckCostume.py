import time
import random
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
ledStrip = dotstar.DotStar(board.D2, board.D3, 60, brightness=.05, auto_write=False)

# Clear the strip
def Clear():
  ledStrip.fill((0,0,0))
  ledStrip.show()

# Draws the whole strip
def Draw(rgbList):  
  #colors = list()
  #colors = headLight + headLight + engineLight + wingTipLeft + tailLights + engineLight + wingTipRight
  
  for i in range(len(rgbList)):
    ledStrip[i] = rgbList[i]

  ledStrip.show()

# Flashes the wingtip lights
def UpdateWingtip(rgbList):
  rgbList.append(rgbList[0])
  rgbList.pop(0)
  return rgbList
  
  
# Animate the engine lights (rotate)
def UpdateEngine(eng):
  eng.append(eng[0])
  eng.pop(0)
  return eng


