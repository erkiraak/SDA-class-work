from math import pi


def pizza_comparison(pizza_1_radius, pizza_1_price, pizza_2_radius, pizza_2_price):
    pizza_1_ratio = (pi * pizza_1_radius ** 2) / pizza_1_price
    print((pi * pizza_1_radius ** 2))
    pizza_2_ratio = (pi * pizza_2_radius ** 2) / pizza_2_price
    return f"Pizza 1 price to size ratio is {'{:.2f}'.format(pizza_1_ratio)}, " \
           f"pizza 2 price to size ratio is {'{:.2f}'.format(pizza_2_ratio)}, " \
           f"Pizza {1 if pizza_1_ratio > pizza_2_ratio else 2} is more economical"


print(pizza_comparison(2, 4, 3, 5))
