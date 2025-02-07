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

def display_menu():
  print("\nShip Management System")
  print("1. Display ship state")
  print("2. Replace part")
  print("3. Change material")
  print("4. Exit")
  return input("Select an option (1-4): ")

def interactive_menu(ship):
  while True:
    choice = display_menu()
    if choice == "1":
      print("\nCurrent ship state:")
      ship.display_state()

    elif choice == "2":
      part_name = input("Enter part name to replace: ")
      new_part_name = input("Enter new part name: ")
      new_part_material = input("Enter new material: ")
      try:
        new_part = Part(new_part_name, new_part_material)
        ship.replace_part(part_name, new_part)
        print(f"Part {part_name} replaced with {new_part_name}")
      except KeyError:
        print(f"Part {part_name} not found")

    elif choice == "3":
      part_name = input("Enter part name to modify: ")
      material = input("Enter new material: ")
      try: 
        ship.change_material(part_name, material)
        print(f"Material for part {part_name} changed to {material}")
      except KeyError:
        print(f"Part {part_name} not found")

    elif choice == "4":
      print("Exiting program")
      break
    
if __name__ == "__main__":
  hull = Part("Hull", "Steel")
  engine = Part("Engine", "Iron")

  ship = Ship("Titanic", [hull, engine])
  interactive_menu(ship)
