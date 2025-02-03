import math

class Cercle: 
  def __init__(self, rayon):
    self.rayon = rayon 
  
  def changerRayon(self, nouveau_rayon): 
    self.rayon = nouveau_rayon
    return self.rayon 
  
  def afficherInfos(self, cercle): 
    print(f'Ce cercle a le rayon de {cercle.rayon} \n Son diametre est {cercle.diametre()} \n Sa circonference est: {cercle.circonference()} \n Son aire est: {cercle.aire()}')
  
  def circonference(self):
    return 2 * math.pi * self.rayon 
  
  def diametre(self): 
    return 2 * self.rayon 
  
  def aire(self): 
    return math.pi * self.rayon ** 2
  
cercle1 = Cercle(10)
cercle2 = Cercle(0.8)

cercle1.afficherInfos(cercle1)
cercle2.afficherInfos(cercle2)