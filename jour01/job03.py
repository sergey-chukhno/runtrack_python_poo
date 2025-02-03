
class Operation: 
  def __init__(self, nombre1, nombre2): 
    self.nombre1 = nombre1 
    self.nombre2 = nombre2
  
  def addition(self): 
    print(self.nombre1 + self.nombre2)

operation = Operation(12,3)
operation.addition()