class Dinner:
    def __init__(self, dish, ingredients):
        self.dish = dish # Define an instance variable
        self.ingredients = ingredients
        print(dish, ingredients)

dinner = Dinner("spaghetti", ["pasta", "tomato sauce"])