
class Livre: 
  def __init__(self, titre, auteur, nombre_de_pages): 
    self.__titre = titre
    self.__auteur = auteur 
    self.__nombre_de_pages = nombre_de_pages
  
  def get_titre(self): 
    return self.__titre
  
  def get_auteur(self): 
    return self.__auteur
  
  def get_nombre_de_pages(self): 
    return self.__nombre_de_pages
  
  def set_titre(self, nouveau_titre):
    self.__titre = nouveau_titre
    return self.__titre
  
  def set_auteur(self, nouvel_auteur): 
    self.__auteur = nouvel_auteur
    return self.__auteur
  
  def set_nombre_de_pages(self, nouveau_nombre_de_pages): 
    if isinstance(nouveau_nombre_de_pages, int) and nouveau_nombre_de_pages > 0:
        self.__nombre_de_pages = nouveau_nombre_de_pages
        return self.__nombre_de_pages
    else: 
       raise ValueError('Le nombre de pages doit être un nombre entier positif')
       
       
    
livre1 = Livre('Harry Potter', 'J.K.Rowling', 312)
print(livre1.get_auteur(), livre1.get_titre(), livre1.get_nombre_de_pages())

livre1.set_nombre_de_pages(328)
print(livre1.get_auteur(), livre1.get_titre(), livre1.get_nombre_de_pages())

livre1.set_nombre_de_pages(-10)
print(livre1.get_auteur(), livre1.get_titre(), livre1.get_nombre_de_pages())


