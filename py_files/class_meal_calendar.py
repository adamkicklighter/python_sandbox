class Dinner:
    def __init__(self, dish, ingredients, prices):
        self.dish = dish
        self.ingredients = ingredients
        self.prices = prices
        print(f"{dish}: {ingredients} - Prices: {prices}")
    
    def total_cost(self):
        return sum(self.prices)

class MealPlanner:
    def __init__(self):
        self.weekly_menu = {}
    
    def add_dinner(self, day, dinner):
        self.weekly_menu[day] = dinner
    
    def display_menu(self):
        for day, dinner in self.weekly_menu.items():
            print(f"{day.capitalize()}: {dinner.dish}")
    
    def calculate_total_cost(self):
        total_cost = 0
        for dinner in self.weekly_menu.values():
            total_cost += dinner.total_cost()
        return total_cost
    
    def generate_shopping_list(self):
        shopping_list = {}
        for dinner in self.weekly_menu.values():
            for ingredient, price in zip(dinner.ingredients, dinner.prices):
                if ingredient in shopping_list:
                    shopping_list[ingredient] += price
                else:
                    shopping_list[ingredient] = price
        return shopping_list

# Example usage
monday_dinner = Dinner("spaghetti", ["pasta", "tomato_sauce"], [2.5, 3.0])
tuesday_dinner = Dinner("tacos", ["ground_beef", "salsa", "shells"], [5.0, 2.0, 1.5])
wednesday_dinner = Dinner("cheese_hamburgers", ["ground_beef", "ketchup", "cheese", "bacon", "pickles"], [5.0, 1.0, 2.0, 3.0, 1.5])
thursday_dinner = Dinner("fried_chicken", ["chicken_breast", "breading", "ranch_dressing"], [4.0, 2.0, 1.5])
friday_dinner = Dinner("club_sandwiches", ["turkey", "ham", "cheese", "bacon", "pickles"], [3.0, 3.0, 2.0, 3.0, 1.5])

meal_planner = MealPlanner()
meal_planner.add_dinner("monday", monday_dinner)
meal_planner.add_dinner("tuesday", tuesday_dinner)
meal_planner.add_dinner("wednesday", wednesday_dinner)
meal_planner.add_dinner("thursday", thursday_dinner)
meal_planner.add_dinner("friday", friday_dinner)

meal_planner.display_menu()
print("Total cost for the week:", meal_planner.calculate_total_cost())

shopping_list = meal_planner.generate_shopping_list()
print("Shopping List:")
for ingredient, total_price in shopping_list.items():
    print(f"{ingredient}: ${total_price:.2f}")