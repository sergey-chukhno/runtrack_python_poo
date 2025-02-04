class Voiture: 
  def __init__(self, marque, modele, annee, kilometrage): 
    self.__marque = marque 
    self.__modele = modele
    self.__annee = annee
    self.__kilometrage = kilometrage
    self.__en_marche = False
    self.__reservoir = 50
  
  # Getters
  def get_marque(self): 
    return self.__marque
  def get_modele(self):
    return self.__modele
  def get_annee(self): 
    return self.__annee
  def get_kilometrage(self):
    return self.__kilometrage
  def get_en_marche(self): 
    return self.__en_marche
  def get_reservoir(self): 
    return self.__verifier_plein()

  
  # Setters
  def set_marque(self, nouvelle_marque):
    self.__marque = nouvelle_marque
    return self.__marque 
  
  def set_modele(self, nouveau_modele):
    self.__modele = nouveau_modele
    return self.__modele
  
  def set_anne(self, nouvelle_annee):
    self.__annee = nouvelle_annee
    return self.__annee
  
  def set_kilometrage(self, nouveau_kilometrage):
    self.__kilometrage = nouveau_kilometrage
    return self.__kilometrage
  
  def set_reservoir(self, nouveau_reservoir):
    self.__reservoir = nouveau_reservoir
    return self.__reservoir
  
  # Demarrer et arreter 
  def demarrer(self): 
      if self.__verifier_plein() >= 5: 
        print('La voiture est démarrée')
        self.__en_marche == True
      else:
        print('Réservoir insuffisant. La voiture ne peut pas démarrer')
        self.__en_marche == False
  
  def arreter(self): 
    self.__en_marche == False
    print('La voiture est arrêtée')
  
  # Verifier plein 
  def __verifier_plein(self):
    return self.__reservoir 
  
voiture1 = Voiture('Peugeot', '208', 2019, 1200)
print(voiture1.get_reservoir())
voiture1.demarrer()
voiture1.arreter()

voiture1.set_reservoir(3)
print(voiture1.get_reservoir())
voiture1.demarrer()

