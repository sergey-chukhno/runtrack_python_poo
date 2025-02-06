class Rectangle: 
  def __init__(self, longueur, largeur): 
    self.__longueur = longueur
    self.__largeur = largeur
  
  def perimetre(self): 
    return (self.__longueur + self.__largeur) * 2

  def surface(self): 
    return self.__longueur * self.__largeur

  def get_longueur(self): 
    return self.__longueur
  
  def get_largeur(self): 
    return self.__largeur
  
  def set_longueur(self, nouvelle_longueur): 
    if isinstance(nouvelle_longueur, int) and nouvelle_longueur > 0:
     self.__longueur = nouvelle_longueur
     return self.__longueur
  
  def set_largeur(self, nouvelle_largeur): 
    if isinstance(nouvelle_largeur, int) and nouvelle_largeur> 0: 
      self.__largeur = nouvelle_largeur
    return self.__largeur

class Parallelepipide(Rectangle): 
  def __init__(self, longueur, largeur, hauteur): 
    super().__init__(longueur, largeur)
    self.hauteur = hauteur

  def volume(self): 
    return self.hauteur * self.get_longueur() * self.get_largeur()

rectangle1 = Rectangle(10, 5)
print(rectangle1.get_longueur())
print(rectangle1.get_largeur())
print(rectangle1.set_longueur(6))
print(rectangle1.set_largeur(8))

print(rectangle1.perimetre())
print(rectangle1.surface())

parallelepipide1 = Parallelepipide(3, 7, 8)
print(parallelepipide1.volume())