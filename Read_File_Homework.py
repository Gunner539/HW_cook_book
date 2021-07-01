
import os.path
import random
from pprint import pprint

def file_exist(file_name):
    current_path = os.getcwd()
    if file_name != '':
        file_address = f'{current_path}\\{file_name}'
    else:
        return False

    if not os.path.isfile(file_address):
        return False
    else:
        return True

def create_cook_book(file_name='recipes.txt'):

    if not file_exist(file_name):
        print('Ошибка. Файл не найден')
        return None

    cook_book = {}
    with open(file_name, 'r', encoding ='utf-8') as file:
        for line in file:
            if line.strip() != '\n':
                food_name = line.strip()
                cook_book[food_name] = []
                ingredients_number = int(file.readline().strip())
                for i in range(1, ingredients_number + 1):
                    ingredient_str = file.readline().strip()
                    ingredient_list = ingredient_str.split(' | ')
                    cook_book[food_name].append({'ingredient_name': ingredient_list[0], 'quantity': ingredient_list[1], 'measure': ingredient_list[2]})
                file.readline()
    return cook_book

def get_data_for_test(cook_book):

    list_dishes_for_test = cook_book.keys()
    dishes_for_test = random.sample(list_dishes_for_test, random.randint(1, len(list_dishes_for_test) - 1))
    person_for_test = random.randint(2, 11)
    print('===========ДАННЫЕ ДЛЯ ТЕСТА============')
    print(person_for_test)
    print(dishes_for_test)
    print('=======================================')
    return {'dishes_for_test': dishes_for_test, 'person_for_test': person_for_test}

def get_shop_list_by_dishes(dishes, person):
    cook_book = create_cook_book()
    calculation = {}
    for dish in dishes:
        ingredients = cook_book.get(dish, None)
        if ingredients != None:
            for i in ingredients:
                ingredient_values = calculation.get(i['ingredient_name'], None)
                if ingredient_values == None:
                    calculation[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person}
                else:
                    calculation[i['ingredient_name']]['quantity'] += int(i['quantity']) * person
    return calculation

if __name__ == '__main__':

    cook_book = create_cook_book()
    if cook_book != None:
        data_for_test = get_data_for_test(cook_book)
        shop_list_by_dishes = get_shop_list_by_dishes(data_for_test['dishes_for_test'], data_for_test['person_for_test'])
        print('=====================SHOP LIST=====================')
        pprint(shop_list_by_dishes)
        print('===================================================')