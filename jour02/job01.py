
class Rectangle: 
  def __init__(self, longueur, largeur): 
    self._longueur = longueur
    self._largeur = largeur 
  
  def get_longueur(self): 
    return self._longueur
  
  def get_largeur(self): 
    return self._largeur
  
  def set_longueur(self, nouveau_longueur):
    self._longueur = nouveau_longueur 
    return self._longueur
  
  def set_largeur(self, nouveau_largeur):
    self._largeur = nouveau_largeur
    return self._largeur
  
rectangle = Rectangle(10, 5)
print (f'Rectangle: ({rectangle.get_longueur()}, {rectangle.get_largeur()})')

rectangle.set_longueur(7)
rectangle.set_largeur(3)
print (f'Rectangle: ({rectangle.get_longueur()}, {rectangle.get_largeur()})')


