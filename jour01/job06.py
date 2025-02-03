class Animal: 
  def __init__(self): 
    self.age = 0 
    self.prenom = ''
  
  def viellir(self): 
    self.age +=1
    return self.age
  
  def nommer(self, prenom): 
    self.prenom = prenom
    return self.prenom
  
animal = Animal()
print(f"L'age de l'animal est {animal.age}")

animal.viellir()
print(f"L'age de l'animal est {animal.age}")

animal.nommer('Bluey')
print(f"L'animal se nomme {animal.prenom}")


    
  
