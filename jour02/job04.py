
class Student: 
  def __init__(self, nom, prenom, numero_etudiant, nombre_de_credits=0): 
    self.__nom = nom 
    self.__prenom = prenom 
    self.__numero_etudiant = numero_etudiant
    self.__nombre_de_credits = nombre_de_credits
    self.__level = self.get_student_eval()

  def get_nom(self): 
    return self.__nom
  
  def get_prenom(self): 
    return self.__prenom
  
  def get_numero_etudiant(self): 
    return self.__numero_etudiant
  
  def get_nombre_de_credits(self): 
    return self.__nombre_de_credits

  def add_credits(self, credits): 
    if credits > 0: 
     self.__nombre_de_credits += credits 
    return self.__nombre_de_credits 

  def __student_eval(self): 
    if self.get_nombre_de_credits() >= 90: 
      return 'Excellent'
    elif self.get_nombre_de_credits() >= 80: 
      return 'Très bien'
    elif self.get_nombre_de_credits() >= 70: 
      return 'Bien'
    elif self.get_nombre_de_credits() >= 60: 
      return 'Passable'
    else: 
      return 'Insuffisant'
    
  def get_student_eval(self): 
    return self.__student_eval()
  
  def get_student_level(self): 
    return self.__level
  
  def student_info(self): 
    print(f'Prenom: {self.get_prenom()}\n' 
          f'Nom: {self.get_nom()}\n'
          f'ID: {self.get_numero_etudiant()}\n'
          f'Niveau: {self.get_student_eval()}')
  
student= Student('Doe', 'Johan', 145)

student.add_credits(10)
student.add_credits(10)
student.add_credits(10)

print(f'Le nombre de credit de {student.get_prenom()} {student.get_nom()} est {student.get_nombre_de_credits()}')

print(student.student_info())
