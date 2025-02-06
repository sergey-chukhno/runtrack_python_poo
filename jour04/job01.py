class Personne: 
  def __init__(self, age=14): 
    self.age = int(age)
  
  def afficherAge(self): 
    print(f'Age: {self.age}')
  
  def bonjour(self): 
    print('Hello')
  
  def modifierAge(self, nouveau_age): 
    if isinstance(nouveau_age, int) and nouveau_age > 0: 
      self.age = nouveau_age
      return self.age

class Eleve(Personne): 

  def allerEnCours(self): 
    print('Je vais en cours')
  
  def afficherAge(self): 
    print(f"J'ai {self.age} ans")

class Professeur(Personne): 
  def __init__(self, matiereEnseignee): 
    self.__matiereEnseignee = matiereEnseignee
  
  
  def enseigner(self): 
    print('Le cours va commencer')

personne1 = Personne()

eleve1 = Eleve()
eleve1.afficherAge()
