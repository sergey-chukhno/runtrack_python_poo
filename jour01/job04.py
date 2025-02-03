
class Personne: 
  def __init__(self, nom, prenom): 
    self.nom = nom 
    self.prenom = prenom 
  
  def SePresenter(self): 
    print(f'Je suis {self.prenom} {self.nom}')

personne1 = Personne("Sergey", "Chukhno")
personne2 = Personne("Rimma", "Chukhno")
personne3 = Personne("Jean-Claude", "van Dame")

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
