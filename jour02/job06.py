class Commande: 
  def __init__(self, numero_de_commande): 
    self.__numero_de_commande = numero_de_commande
    self.__liste_de_plats = {}
    self.__statut_de_commande = 'en cours'

  # Getters et setters 
  def get_numero_de_commande(self): 
    return self.__numero_de_commande
  def set_numero_de_commande(self, nouveau_numero_de_commade): 
    self.__numero_de_commande = nouveau_numero_de_commade
    return self.__numero_de_commande
  
  def get_liste_de_plats(self): 
    return self.__liste_de_plats
  def set_liste_de_plats(self, nouveau_liste_de_plats): 
    if isinstance(nouveau_liste_de_plats, dict): 
      self.__liste_de_plats = nouveau_liste_de_plats
    else: 
      raise ValueError('La liste de plats doit être fournie sous forme de dictionnaire')
  
  def get_statut_de_commande(self): 
    return self.__statut_de_commande
  def set_statut_de_commande(self, nouveau_statut_de_commande): 
    self.__statut_de_commande = nouveau_statut_de_commande
    return self.__statut_de_commande
  
  # Ajouter un plat dans une commande 
  def ajouter_un_plat(self, nom, prix, statut_de_commande='en cours'): 
   nouveau_liste_de_plats = self.get_liste_de_plats()
   nouveau_liste_de_plats[nom] = {'prix':prix, 'statut_de_commande': statut_de_commande}
   self.set_liste_de_plats(nouveau_liste_de_plats)

  # Annuler la commande
  def annuler_commande(self): 
    self.set_statut_de_commande('annulée')
    print('La commande a été annulée')
  
  # Calculer le total 
  def calculer_total(self): 
    total = 0 
    liste_de_plats = self.get_liste_de_plats()
    for items in liste_de_plats.values(): 
      total += items['prix']
    return total 
  
  # Calculer le TVA 
  def calculer_tva(self, tva=20): 
    total = self.calculer_total()
    return total * tva / 100 
  
  # Afficher la commande 
  def afficher_commande(self): 
    print(
      f'Commande numéro {self.get_numero_de_commande()}\n'
      f'Statut de la commande: {self.get_statut_de_commande()}\n'
      f'Plats commandés:'
    )
    plats = self.get_liste_de_plats()
    for nom, values in plats.items(): 
      print(f'{nom}: {values['prix']} euros {values['statut_de_commande']}')
    total = self.calculer_total()
    tva = self.calculer_tva()
    print(f'Total à payer: {total:.2f} euros')
    print(f'TVA: {tva:.2f} euros')

commande = Commande(1856)
commande.ajouter_un_plat('Pizza', 12)
commande.ajouter_un_plat('Pates bolonaises', 14)
commande.ajouter_un_plat('Risotto', 16)

print(commande.get_liste_de_plats())

print(commande.calculer_total())
print(commande.calculer_tva(20))

commande.afficher_commande()
commande.annuler_commande()