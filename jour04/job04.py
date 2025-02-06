class Forme: 
  def aire(self): 
    return None

class Rectangle(Forme): 
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur 
  
  def aire(self): 
    return self.longueur * self.largeur

rectangle1 = Rectangle(8, 10)
print(rectangle1.aire())