import math
counter = 0
cost = 0
expense = 1
while counter < 64:
    counter = counter + 1
    cost = cost + expense
    expense = expense * 2
print('Правитель должен был заплатить изобретателю', cost, 'зёрен')

print(cost / 2e8, 'тонн')
# Вес пшеницы в тоннах

cornArea = float(input()) / 2
countryArea = 17100000
regionArea = 178200
cityArea = 502.7
print(cost / cornArea // countryArea, 'слоёв')
# Количество слоёв зёрен для страны
print(cost / cornArea // regionArea, 'слоёв')
# Количество слоёв зёрен для области
print(cost / cornArea // cityArea, 'слоёв')
# Количество слоёв зёрен для города

cornCountryAmountPerYear = 26.6
cornRegionAmountPerYear = 18.3
cornCityAmountPerYear = 3.8

print('Потребовалось бы', math.ceil(cost / cornCountryAmountPerYear), 'лет')
print('Потребовалось бы', math.ceil(cost / cornRegionAmountPerYear), 'лет')
print('Потребовалось бы', math.ceil(cost / cornCityAmountPerYear), 'лет')

