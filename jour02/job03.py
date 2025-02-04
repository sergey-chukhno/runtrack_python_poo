
class Livre: 
  def __init__(self, titre, auteur, nombre_de_pages, disponible): 
    self.__titre = titre
    self.__auteur = auteur 
    self.__nombre_de_pages = nombre_de_pages
    self.__disponible = True
  
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
  
  def verification(self): 
    if self.__disponible: 
      print('Le live est disponible')
      return True
    else: 
      return f'Le livre est indisponible'
  
  def emprunter(self): 
    if self.verification(): 
      self.__disponible = False
      return f'Le livre est emprunté'
    else: 
      return 'Le livre est indisponible'


  def rendre(self): 
    if self.emprunter(): 
      self.__disponible = True
      return f'Le livre est rendu'
    else: 
      return f'Le livre est disponible'

livre = Livre('Harry Potter', 'J.K.Rowling', 325, True)

print(livre.verification())

livre.emprunter()
print(livre.emprunter())
print(livre.verification())

livre.rendre()
print(livre.rendre())
print(livre.verification())
