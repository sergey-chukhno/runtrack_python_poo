class Produit: 
  def __init__(self, nom, prixHT, TVA): 
    self.nom = nom 
    self.prixHT = prixHT
    self.TVA = TVA
  
  def calculerPrixTTC(self): 
    return self.prixHT * (1 + self.TVA / 100)
  
  def afficherInfos(self): 
    return f"Produit: Nom: {self.nom}; Prix HT: {self.prixHT} euros; TVA: {self.TVA}%; Prix TTC: {self.calculerPrixTTC()} euros;"
  
  def modifierNom(self, nouveau_nom):
    self.nom = nouveau_nom

  def modifierPrixHT(self, nouveau_prixHT): 
    self.prixHT = nouveau_prixHT

  def obtenirNom(self): 
    return self.nom
  
  def obtenirPrixHT(self): 
    return self.prixHT
  
  def obtenirTVA(self): 
    return self.TVA
  
  def obtenirPrixTTC(self): 
    return self.calculerPrixTTC()

produit1 = Produit('Ordinateur', 1100, 15)
produit2 = Produit('Chocolat', 2, 20)
produit3 = Produit('Cigarettes', 10, 35)

prix_ttc_1 = produit1.calculerPrixTTC()
prix_ttc_2 = produit2.calculerPrixTTC()
prix_ttc_3 = produit3.calculerPrixTTC

print(produit1.afficherInfos())
print(produit2.afficherInfos())
print(produit3.afficherInfos())

produit1.modifierNom('Camera')
produit1.modifierPrixHT(80)
produit2.modifierNom('Jouet')
produit2.modifierPrixHT(20)
produit3.modifierNom('Boisson')
produit3.modifierPrixHT(1.4)

nouveau_prix_ttc_1 = produit1.calculerPrixTTC()
nouveau_prix_ttc_2 = produit2.calculerPrixTTC()
nouveau_prix_ttc_3 = produit3.calculerPrixTTC()

print(produit1.afficherInfos())
print(produit2.afficherInfos())
print(produit3.afficherInfos())

