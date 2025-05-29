from enum import Enum

class Category(Enum):
  REJECTED = "REJECTED"
  SPECIAL = "SPECIAL"
  STANDARD = "STANDARD"

class Package:
  BULKY_VOLUME_THRESHOLD = 1_000_000
  BULKY_DIMENSION_THRESHOLD = 150
  HEAVY_MASS_THRESHOLD = 20

  def __init__(self, width: float, height: float, length: float, mass: float):
    self.width = width
    self.height = height
    self.length = length
    self.mass = mass

  def is_bulky(self) -> bool:
    volume = self.width * self.height * self.length
    largest_dimension = max(self.width, self.height, self.length)
    return volume >= self.BULKY_VOLUME_THRESHOLD or largest_dimension >= self.BULKY_DIMENSION_THRESHOLD
  
  def is_heavy(self) -> bool:
    return self.mass >= self.HEAVY_MASS_THRESHOLD

  def classify(self) -> str:
    bulky = self.is_bulky()
    heavy = self.is_heavy()
  
    if bulky and heavy:
      return Category.REJECTED.value
    if bulky or heavy:
      return Category.SPECIAL.value
    return Category.STANDARD.value


def sort(width: float, height: float, length: float, mass: float) -> str:
  p = Package(width, height, length, mass)
  return p.classify()

assert sort(10, 10, 10, 5) == "STANDARD"
assert sort(100, 100, 100, 19) == "SPECIAL"
assert sort(150, 10, 10, 10) == "SPECIAL"
assert sort(100, 100, 100, 20) == "REJECTED"
assert sort(1000, 1, 1000, 5) == "SPECIAL"
assert sort(99, 100, 100, 19.9) == "STANDARD"
assert sort(200, 200, 200, 30) == "REJECTED"
assert sort(151, 10, 10, 20) == "REJECTED"
assert sort(149.9, 149.9, 149.9, 20) == "REJECTED"
assert sort(1e6, 1e6, 1e6, 1e6) == "REJECTED"

print("All test cases passed")
