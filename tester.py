from kitchen import Ingredient
from kitchen import Cook, Boil

cebolla = Ingredient("cebolla", 1)
aji = Ingredient("aji", 2)

Boil([cebolla, aji], 45)

