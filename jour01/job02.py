
class Operation: 
  def __init__(self, nombre1, nombre2): 
    self.nombre1 = nombre1 
    self.nombre2 = nombre2

operation = Operation(12,3)
print(f'Le nombre 1 est {operation.nombre1}\n Le nombre 2 est {operation.nombre2}')