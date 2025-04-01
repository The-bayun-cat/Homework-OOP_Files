# Задание №1.
from pprint import pprint

cook_book = {}

with open("recipes.txt", "r", encoding="utf-8") as file:
    while True:
        dish_name = file.readline().strip()               # Читаем название блюда
        if not dish_name:                                 # Если строка пустая (конец файла)
            break

        ingredient_count = int(file.readline().strip())   # Читаем кол-во ингредиентов
        ingredients = []

        for _ in range(ingredient_count):
            # Разбиваем строку на части: "Ингредиент | Количество | Мера"
            ingredient_data = file.readline().strip().split(" | ")
            ingredient = {
                "ingredient_name": ingredient_data[0],
                "quantity": int(ingredient_data[1]),
                "measure": ingredient_data[2]
            }
            ingredients.append(ingredient)

        cook_book[dish_name] = ingredients
        file.readline()                                    # Пропускаем пустую строку между рецептами

pprint(cook_book, width=100, sort_dicts=False)

# Задание №2.
def get_shop_list_by_dishes(dishes_list, person_count):
    shop_list = {}
    for dish in dishes_list:
        if dish not in cook_book:
            print(f'Блюда "{dish}" нет в книге')
            continue

        for ingredient in cook_book[dish]:
            name = ingredient["ingredient_name"]
            if name in shop_list:
                shop_list[name]["quantity"] += ingredient["quantity"] * person_count
            else:
                shop_list[name] = {
                    "measure": ingredient["measure"],
                    "quantity": ingredient["quantity"] * person_count
                }
    return shop_list

pprint(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))

# Задание №3
with open('1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()

with open('3.txt', 'r', encoding='utf-8') as file_3:
    line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        line_3['3.txt'] = count_3
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.read()

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as file_result:
    for name, lines in join:
        content = text_1 if name == '1.txt' else (text_2 if name == '2.txt' else text_3)
        file_result.write(f'{name}\n{lines}\n{content}\n')





















