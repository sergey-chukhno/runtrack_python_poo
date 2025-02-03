class Point: 
  def __init__(self, x, y): 
    self.x = x 
    self.y = y 
  
  def afficherLesPoints(self): 
    print(self.x, self.y)
  
  def afficherX(self): 
    print(self.x)
  
  def afficherY(self): 
    print(self.y)
  
  def changerX(self, nouveau_x): 
    self.x = nouveau_x

  def changerY(self, nouveau_y): 
    self.y = nouveau_y

point = Point(5, 5)
point.afficherLesPoints()
point.afficherX()
point.afficherY()

point.changerX(7)
point.changerY(0)
point.afficherLesPoints()