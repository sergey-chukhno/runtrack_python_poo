class Tache: 
  def __init__(self, titre, description, statut = 'à faire'): 
    self.titre = titre
    self.description = description 
    self.statut = statut
  
  def __str__(self): 
    return f"{self.titre}: {self.description}[{self.statut}]"

class ListeDeTaches: 
  def __init__(self): 
    self.taches = []

  def ajouterTache(self, tache): 
    return self.taches.append(tache)
  
  def supprimerTache(self, tache): 
    return self.taches.remove(tache)
  
  def marquerCommeFinie(self, titre): 
    for tache in self.taches: 
      if tache.titre == titre: 
        tache.statut = 'Terminée'
        break

  def afficherListe(self): 
    return [str(tache) for tache in self.taches]
  
  def filterListe(self, statut): 
    return [str(tache) for tache in self.taches if tache.statut == statut]
  
tache1 = Tache('Préparer le dinner', "Réchauffer un plat A")
tache2 = Tache('Débarasser la table', 'Langer et laver la vaisselle')
tache3 = Tache("Faire les devoir", "Faire les maths et la dictée")

liste1 = ListeDeTaches()

liste1.ajouterTache(tache1)
liste1.ajouterTache(tache2)
liste1.ajouterTache(tache3)

liste1.supprimerTache(tache3)

liste1.marquerCommeFinie('Préparer le dinner')
print(liste1.afficherListe())
print(liste1.filterListe('à faire'))

    