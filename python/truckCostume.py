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


