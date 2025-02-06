import random

class Carte: 
  def __init__(self, valeur, couleur): 
    self.valeur = valeur 
    self.couleur = couleur
    self.valeur_choisie = 11 if valeur == 'As' else None
  
  def __str__(self): 
    return f'{self.valeur} de {self.couleur}'

class Jeu: 
  def __init__(self):
    self.cartes = []
    self.init_paquet_cartes()

  def init_paquet_cartes(self): 
    couleurs = ["Trèfle", "Pique", "Coeur", "Carreau"]
    valeurs = [str(n) for n in range(2, 11)] + ['Valet', 'Dame', 'Roi', 'As']
    self.cartes = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]

  def melanger(self): 
    random.shuffle(self.cartes)
  
  def tirer_une_carte(self): 
    if not self.cartes: 
      self.init_paquet_cartes()
      self.melanger()
    return self.cartes.pop()


def choisir_valeur_as(self): 
  choix = input("Vouz avez tiré un As. Voulez-vous compter cette As pour 1 ou pour 11?")
  while choix in ['1', '11']:
    choix = input("Veuillez choisir entre 1 ou 11 :")
  return int(choix)

def retourner_valeur_as(cartes): 
  for i, carte in enumerate(cartes): 
    if carte.valeur == 'As': 
      print(f"\nPour l'As de {carte.couleur}: ")
      choix = input("Voulez-vous le compter pour 1 ou 11 ?")
      carte.valeur_choisie = int(choix)

def calculer_total(cartes): 
  total = 0 
  for carte in cartes: 
    if carte.valeur == "As": 
      if carte.valeur_choisie is not None: 
        total += carte.valeur_choisie
      else: 
        total += 11
    elif carte.valeur in ['Valet', 'Dame', 'Roi']: 
      total += 10
    else: 
      total += int(carte.valeur)
  return total 

def jouer_le_jeu(): 
  jeu = Jeu()
  jeu.melanger()

  cartes_joeur = [jeu.tirer_une_carte(), jeu.tirer_une_carte()]
  cartes_croupier=[jeu.tirer_une_carte(), jeu.tirer_une_carte()]

  print('Les cartes du joueur:')

  for carte in cartes_joeur:
    print(carte) 

  print('Les cartes du croupier:')
  print(f'La carte visible: {cartes_croupier[0]}')
  print('La carte cachée')

  while True: 
    choix = input("Voulez-vous recevoir une carte(r) ou passer('p')?")

    if choix == 'r': 
      nouvelle_carte = jeu.tirer_une_carte()
      cartes_joeur.append(nouvelle_carte)
      print('Vous avez tiré: ', nouvelle_carte)
      print("Vos cartes actuelles sont: ")
      for carte in cartes_joeur: 
        print(carte)
      total_joueur = calculer_total(cartes_joeur)
      print('Votre total prévisoire (As compté pour 11) est: ', total_joueur)
      if total_joueur > 21: 
        print('Vous avez dépassé 21. Vous avez perdu!')
        return
      
    elif choix == 'p': 
      break 
    
    else: 
      print("Choix incorrecte. Veuillez taper 'r' ou 'p'")
    
  print('Tour du croupier')
  print('Cartes du croupier révélées:')

  for carte in cartes_croupier: 
    print(carte)
  
  total_croupier = calculer_total(cartes_croupier)
  print("Le total du croupier est: ", total_croupier)

  while total_croupier < 17: 
    nouvelle_carte = jeu.tirer_une_carte()
    cartes_croupier.append(nouvelle_carte)
    total_croupier = calculer_total(cartes_croupier)
  
  print('Choix des valeurs pour les as du joueur')
  retourner_valeur_as(cartes_joeur)
  total_joueur = calculer_total(cartes_joeur)

  print('Resultat final:')
  if total_joueur > 21: 
    print(f'Votre total est {total_joueur}. Le total du croupier est {total_croupier}. Vous avez perdu!')
  elif total_croupier > 21:
    print(f'Votre total est {total_joueur}. Le total du croupier est {total_croupier}. Vous avez gagné!')
  elif total_joueur > total_croupier:
    print(f'Votre total est {total_joueur}. Le total du croupier est {total_croupier}. Vous avez gagné!')
  elif total_joueur < total_croupier: 
    print(f'Votre total est {total_joueur}. Le total du croupier est {total_croupier}. Vous avez perdu!')
  else: 
    print(f"Votre total est {total_joueur}. Le total du croupier est {total_croupier}. Match nul!")

  return True

while True: 
  jouer_le_jeu()

  while True: 
    rejouer = input("\nVoulez-vous jouer encore ('o' pour oui, 'n' pour 'non'): ").strip().lower()
    if rejouer == 'o': 
      break
    elif rejouer == 'n': 
      print("Merci d'avoir joué!")
      exit()
    else: 
      print("Choix incorrecte. Veuillez introduire 'o' pour 'oui' ou 'n' pour 'non'")