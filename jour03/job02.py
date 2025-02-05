class CompteBancaire: 
  def __init__(self, numero_compte, nom, prenom, solde, decouvert): 
    self.__numero_compte = numero_compte
    self.__nom = nom 
    self.__prenom = prenom 
    self.__solde = solde 
    self.__decouvert = decouvert
  
  def afficher(self): 
    print(f'Numero de compte: {self.__numero_compte}; Prenom: {self.__prenom}; Nom: {self.__nom};')
  
  def afficherSolde(self): 
    print(f'Le solde du compte est: {self.__solde}')
  
  def versement(self, montant): 
    self.__solde += montant
    return self.__solde
  
  def retrait(self, montant): 
    if self.__solde >= montant or self.__decouvert: 
      self.__solde -= montant
    else: 
      print('Le solde est insuffisant pour le montant demandé')
  
  def agios(self, montant_agios=25): 
    if self.__decouvert and self.__solde <0:
      self.__solde -= montant_agios
      print(f"Vous êtes à découvert. Le montant d'agios de {montant_agios} a été appliqué. Votre solde actuel est {self.__solde}")
      return self.__solde
  
  def virement(self, reference, compte_destinataire, montant): 
    if montant <= 0:
      print('Le montant doit être positif et supérieur à zéro')
    if self.__solde < montant and not self.__decouvert: 
      print('Montant insuffisant pour effectuer le virement. Veuillez approvisionner votre compte')
    else: 
      self.__solde -= montant 
      compte_destinataire.__solde += montant
      print(f'Le virement {reference} du {montant} euros du compte {self.__numero_compte} au compte {compte_destinataire.__numero_compte} a été effectué')
    

compte1 = CompteBancaire(101288, 'Thierry', 'Breton', 102380, False)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(35000)
compte1.afficherSolde()
compte1.retrait(55000)
compte1.afficherSolde()
compte1.retrait(90000)

compte2 = CompteBancaire(312100, 'Mikael', 'Jackson', -1054, True)
compte2.agios()

compte1.afficherSolde()
compte1.versement(10000)
compte1.afficherSolde()
compte1.virement('Ref123', compte2, 1100)
compte2.virement('Ref124', compte1, 2000)
compte1.virement('Ref125', compte2, 50000)
compte1.afficherSolde()
compte2.afficherSolde()
compte1.virement('Ref126', compte2, 100000)