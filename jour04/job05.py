class Forme: 
  def aire(self): 
    return None

class Rectangle(Forme): 
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur 

  def aire(self): 
    return self.longueur * self.largeur

class Cercle(Forme): 
  def __init__(self, radius): 
    self.radius = radius 
  
  def aire(self): 
    return self.radius ** 2

rectangle1 = Rectangle(10, 8)
cercle1 = Cercle(8)

print(rectangle1.aire())
print(cercle1.aire())