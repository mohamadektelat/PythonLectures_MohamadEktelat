# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_recipe_price(prices, optionals=[], **ingredients):
    price = 0
    for ingredient in ingredients:
        if ingredient not in optionals:
            price += ((ingredients[ingredient] / 100) * prices[ingredient])
    return price


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
