class Joueur: 
  def __init__(self, nom, numero, position, nombre_buts, passes_decisives, cartons_jaunes, cartons_rouges):
    self.nom = nom 
    self.numero = numero 
    self.position = position 
    self.nombre_buts = nombre_buts 
    self.passes_decisives = passes_decisives
    self.cartons_jaunes = cartons_jaunes
    self.cartons_rouges = cartons_rouges
  
  def marquerUnBut(self): 
    self.nombre_buts += 1
    return self.nombre_buts
  
  def effectuerUnePasseDecisive(self):
    self.passes_decisives += 1
    return self.passes_decisives
  
  def recevoirUnCartonJaune(self): 
    self.cartons_jaunes += 1
    return self.cartons_jaunes
  
  def recevoirUnCartonRouge(self): 
    self.cartons_rouges += 1
    return self.cartons_rouges
  
  def afficherStatistiques(self): 
    print(f'Joueur: {self.nom}, {self.numero}, {self.position}, {self.nombre_buts}, {self.passes_decisives}, {self.cartons_jaunes}, {self.cartons_rouges}')
  
class Equipe: 
  def __init__(self, nom): 
    self.nom = nom
    self.liste_joueurs = []
  
  def ajouterJoueur(self, joueur): 
    return self.liste_joueurs.append(joueur)
  
  def afficherStatistique(self): 
    for jouer in self.liste_joueurs: 
      print(jouer.afficherStatistiques())

  def mettreAJourStatistiquesJoueur(self, nom, action): 
    for joueur in self.liste_joueurs:
      if joueur.nom == nom:
          if action == "but": 
            joueur.marquerUnBut()
          elif action == 'passe decisive': 
            joueur.effectuerUnPasseDecisive()
          elif action == 'carton jaune': 
            joueur.recevoirUnCartonJaune()
          elif action == 'carton rouge': 
            joueur.recevoirunCartonRouge()

joueur1 = Joueur('Ronaldo', 9, 'Attaquant', 10, 20, 1, 0)
joueur2 = Joueur('Zinedine Zidane', 10, 'Attaquant', 12, 26, 2, 1)
joueur3 = Joueur('Killian Mbappe', 11, 'Attaquant', 18, 9, 5, 0)

barcelone = Equipe('Barcelone')
om = Equipe('OM')

barcelone.ajouterJoueur(joueur3)
om.ajouterJoueur(joueur1)
om.ajouterJoueur(joueur2)

barcelone.afficherStatistique()
om.afficherStatistique()

joueur2.effectuerUnePasseDecisive()
joueur1.marquerUnBut()
joueur3.recevoirUnCartonRouge()

barcelone.afficherStatistique()
om.afficherStatistique()