class Vehicule: 
  def __init__(self, marque, modele, annee, prix): 
    self.marque = marque 
    self.modele = modele 
    self.annee = annee
    self.prix = prix 
  
  def informationsVehicule(self): 
    print(f'Marque : {self.marque}; Modele: {self.modele}; Annee: {self.annee}; Prix: {self.prix}')
  
  def demarrer(self): 
    print('Attention, je roule')

class Voiture(Vehicule): 
  def __init__(self, marque, modele, annee, prix, portes = 4): 
    super().__init__( marque, modele, annee, prix)
    self.portes = portes 
  def informationsVehicule(self): 
    print(f'Marque : {self.marque}; Modele: {self.modele}; Annee: {self.annee}; Prix: {self.prix}; Nombre de portes: {self.portes}')
  
  def demarrer(self): 
    print('Tres attention, je roule')

class Moto(Vehicule): 
  def __init__(self, marque, modele, annee, prix, roues=2): 
    super().__init__( marque, modele, annee, prix)
    self.roues = roues 
  def informationsVehicule(self): 
    print(f'Marque : {self.marque}; Modele: {self.modele}; Annee: {self.annee}; Prix: {self.prix}; Nombre de roues: {self.roues}')
  
  def demarrer(self): 
    print('Vroum vroum! Je roule')



voiture1 = Voiture('BMW', 'X5', 2024, 80000)
voiture1.informationsVehicule()
voiture1.demarrer()


moto1 = Moto('Honda', 'ZX7', 2024, 20000)
moto1.informationsVehicule()
moto1.demarrer()