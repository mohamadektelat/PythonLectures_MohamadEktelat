# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# This function is responsible for calculating a product price according to his ingredient.
def calculating_one_price(ingredient, price):
    return (ingredient/100)*price


# This function is responsible for calculating the price of the recipe.
# The function gets an input a dictionary of the product prices, and the optional products and the ingredients
# of the products
def get_recipe_price(prices, optionals=[], **ingredients):
    price = (calculating_one_price(ingredients[ingredient], prices[ingredient]) for ingredient in ingredients
             if ingredient not in optionals)
    return sum(price)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
