from pprint import pprint

class Ingredient:

    def __init__(self, ingredient_name, amount):
        self.name = ingredient_name
        self.amount = amount

class Cook:
    def __init__(self, ingredients_list = [], time = None):
        self.ingredients = ingredients_list
        self.time = time
        #self.recipe_header()

    def ingredients_list(self):
        return self.ingredients

    def time(self):
        return self.time

    def recipe_header(self):
        pprint("Recipe")
        for ingridient in self.ingredients:
            pprint(ingridient.name + "   " + str(ingridient.amount))

    def till(self, condition):
        pprint(condition)

class Boil(Cook):
    def __init__(self, ingredients_list, time):
        Cook.__init__(self, ingredients_list, time)
        print(self.time)
        for i in self.ingredients_list():
            print(i.name)
        #self.instruction()

    def instruction(self):
        pass
        #i = ""
        #if len(self.ingredients_list() == 1):
        #    i = "ingredient"
        #else:
        #    i = "ingredients"
        #pprint("Boil the" + i + " "
        #                + str(self.ingredients_list())
        #                + " during "
        #                + self.time())

class Cut:
    def __init__(self, ingredient, style):
        pass

class Fry(Cook):
    pass

class Heat(Cook):
    pass
