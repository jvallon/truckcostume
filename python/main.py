import time
import random
import board
import adafruit_dotstar as dotstar
import truckCostume

# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
ledOnboard = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
ledOnboard[0] = (0,0,255)

# INIT
truckCostume.Clear()

# HELPERS
# a random color 0 -> 255
def random_color():
  return random.randrange(0, 255)

# the loop counter for use in timing, from 1 to maxLoopCount
loopCount = 1
maxLoopCount = 5

while True:
  truckCostume.Draw()
  time.sleep(.1)

  if loopCount >= 1:
    truckCostume.UpdateEngines()
  if loopCount >= 5:
    truckCostume.UpdateWingtips()
  
  loopCount += 1
  if loopCount > maxLoopCount: loopCount = 1

"""
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
ledStrip = dotstar.DotStar(board.D2, board.D3, 60, brightness=.05, auto_write=False)
"""