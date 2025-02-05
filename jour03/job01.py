class Ville: 
  def __init__(self, nom, nombre_habitants): 
    self.__nom = nom 
    self.__nombre_habitants = nombre_habitants 

  def get_nom(self): 
    return self.__nom
  def set_nom(self, nom): 
    self.__nom = nom 
    return self.__nom
  
  def get_nombre_habitants(self):
    return self.__nombre_habitants
  
  def set_nombre_habitants(self, nombre): 
    self.__nombre_habitants = nombre
    return self.__nombre_habitants

class Personne: 
  def __init__(self, nom, age, ville):
    self.nom = nom 
    self.age = age 
    self.ville = ville
    self.nombre_habitants = ville.get_nombre_habitants()

  def ajouterPopulation(self, ville): 
    nombre_habitants = ville.get_nombre_habitants()
    nouveau_nombre_habitants = nombre_habitants +1
    return ville.set_nombre_habitants(nouveau_nombre_habitants)

  

paris=Ville('Paris', 1000000)
marseille = Ville('Marseille', 861635)

print(f'Population de la ville de Paris: {paris.get_nombre_habitants()}')
print(f'Population de la ville de Marseille: {marseille.get_nombre_habitants()}')

personne1 = Personne('John', 45, paris)
personne2 = Personne('Myrtille', 4, paris)
personne3 = Personne('Chloé', 18, marseille)

personne1.ajouterPopulation(paris)
personne2.ajouterPopulation(paris)
personne3.ajouterPopulation(marseille)

print(f'Mise à jour de la population de la ville de Pairs: {paris.get_nombre_habitants()}')
print(f'Mise à jour de la population de la ville de Marseille: {marseille.get_nombre_habitants()}')

