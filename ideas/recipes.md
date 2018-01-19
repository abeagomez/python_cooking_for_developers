## Recipes examples

### Spaghetti

```python
def spaghetti():
    water = Ingredient(liters(2))
    salt = Ingredient(spoons(2))
    spaghetti = Ingredient(g(500))
    cheese = Ingredient(g(200))
    tomato_sauce = Ingredient(g(150))

    pot = Utils()

    Add(water, pot)
    Add(salt, pot)
    Heat(water).until(Boil())
    Put(spaghetti).inside(Pot)
    Boil([water, salt, spaghetti]).during(minutes(15))
    Drop(water)
    Add([cheese, tomato_sauce], pot)
    Mix([spaghetti, salt, tomato_sauce, cheese], pot)
```

```python
def spaghetti():
    water = Ingredient(liters(2))
    salt = Ingredient(spoons(2))
    spaghetti = Ingredient(g(500))
    cheese = Ingredient(g(200))
    tomato_sauce = Ingredient(g(150))

    pot = Utils()

    Add(water, pot)
    Add(salt, pot)
    while ! water.boil():
        water.heat()
    Put(spaghetti).inside(Pot)
    water.boil(minutes(15))
    Drop(water)
    Add([cheese, tomato_sauce], pot)
    Mix([spaghetti, salt, tomato_sauce, cheese], pot)
```