class Part:
  def __init__(self, name, material):
    self.name = name
    self.material = material
  
  def change_material(self, material):
    self.material = material

  def __str__(self):
    return f"{self.name} ({self.material})"

class Ship:
  def __init__(self, name, parts):
    self.name = name
    self.__parts = {part.name: part for part in parts}
  
  def display_state(self):
    for part in self.__parts.values():
      print(part)

  def replace_part(self, part_name, new_part):
    self.__parts[part_name] = new_part
    return self.__parts

  def change_material(self, part_name, material):
    self.__parts[part_name].change_material(material)
    return self.__parts

class RacingShip(Ship):
  def __init__(self, name, parts, max_speed):
    super().__init__(name, parts)
    self.max_speed = max_speed

  def display_speed(self):
    print(f"Max speed: {self.max_speed}")

if __name__ == "__main__":
  hull = Part("Hull", "Steel")
  engine = Part("Engine", "Iron")

  print(f"\nInitial memory addresses:")
  print(f"Hull object at: {id(hull)}")
  print(f"Engine object at: {id(engine)}")

  ship = Ship("Titanic", [hull, engine])
  print(f"\nShip object at: {id(ship)}")

  print("\nDisplaying ship state:")
  ship.display_state()

  print(f"\nModifying hull material...")
  ship.change_material("Hull", "Aluminum")

  print(f"\nAfter modification:")
  ship.display_state()

  print(f"\nMemory addresses after modification:")
  print(f"Hull object still at: {id(hull)}")
  print(f"Hull material is now: {hull.material}")
