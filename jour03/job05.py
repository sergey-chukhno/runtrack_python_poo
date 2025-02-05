class Personnage: 
  def __init__(self, nom, vie): 
    self.nom = nom 
    self.vie = vie
  
  def attaquer(self, personnage): 
    personnage.vie -= 10
    return personnage.vie
  


class Jeu: 
  def __init__(self): 
    self.niveau = None 
    self.joueur = None 
    self.ennemi = None 
  
  def choisirNiveau(self):
    print('Choisissez le niveau du jeu')
    print("Tapez 1 pour le niveau facile")
    print("Tapez 2 pour le niveau moyen")
    print("Tapez 3 pour le niveau difficile")

    while True: 
      choix = input('Entrez le numéro du niveau(1, 2 ou 3):')
      if choix in ["1", "2", "3"]: 
        self.niveau = int(choix)
        break
      else: 
        print('Choix incorrecte. Veuillez entrer 1, 2 ou 3 pour choisir le niveau du jeu')
  
  def lancerJeu(self): 
    self.choisirNiveau()

    if self.niveau == 1: 
      joueur_vie = 100
      ennemi_vie = 50
    elif self.niveau == 2: 
      joueur_vie = 50
      ennemi_vie = 50
    elif self.niveau == 3: 
      joueur_vie = 50
      ennemi_vie = 100 

    self.joueur = Personnage("Joueur", joueur_vie)
    self.ennemi = Personnage('Ennemi', ennemi_vie)

    while self.joueur.vie and self.ennemi.vie > 0: 
      input("Appuyer 'Entrez' pour lancer une attaque")
      self.joueur.attaquer(self.ennemi)
      if self.ennemi.vie <= 0:
        print('Bravo! Vous avez gange!')
        break
      else: 
        print("L'ennemi lance une attaque")
        self.ennemi.attaquer(self.joueur)
        if self.joueur.vie <= 0: 
          print('Hélas, vous avez perdu')
          break
        else: 
          continue 
jeu = Jeu()
jeu.lancerJeu()