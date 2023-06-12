import pandas as pd

tvset = ['Samsung', 'LG', 'Sony', 'Philips', 'Panasonic']
gadgets = ['notebook',
           'tabletq',
           'smartphone',
           'headphones',
           'keyboard',
           'mouse',
           'monitor',
           'processor',
           'video-card',
           'hdd-disk',
           'CPU-memory',
           'printer'
           ];


def sarcina1():
    i = 0
    while i < len(gadgets):
        print(gadgets[i])
        i += 1


def sarcina2():
    print("Diapozon:")
    for i in range(4, len(gadgets)):
        print(i)
    else:
        print("Sfarsitul listei")


def sarcina3():
    if "notebook" in gadgets:
        print("True")
    else:
        print("False")

    if "televizor" in gadgets:
        print("True")
    else:
        print("False")


def sarcina4():
    gadgets.insert(0, 'microfon')
    print(gadgets)

    gadgets.append('colonki')
    print(gadgets)


def sarcina5():
    digital_gadgets = gadgets.copy()
    digital_gadgets.extend(tvset)
    print(digital_gadgets)


def sarcina6():
    gadgets.extend(tvset)
    print(gadgets)


def sarcina7():
    print(f"Total number of elements is {len(gadgets)}")


def sarcina8():
    element_at_index_10 = gadgets.pop(10)
    print(f"Removed element: {element_at_index_10}")
    print(f"Gadgets list after removal: {gadgets}")


def sarcina9():
    cars = ('Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Jeep', 'Kia', 'Mercedes-Benz', 'Nissan', 'Toyota')


def sarcina10():
    cars = ('Audi', 'BMW', 'Chevrolet', 'Ford', 'Honda', 'Jeep', 'Kia', 'Mercedes-Benz', 'Nissan', 'Toyota')
    expensive_cars = ('Ferrari', 'Pagani Huayra', 'McLaren Elva', 'Czinger 21C')
    cars_list = list(cars)
    cars_list.extend(expensive_cars)
    cars = tuple(cars_list)
    print(cars)


def sarcina11():
    cars = (
        'Audi', 'BMW', 'Chevrolet', 'Pagani Huayra', 'Ford', 'Honda', 'Jeep', 'Kia', 'Mercedes-Benz', 'Nissan',
        'Toyota')
    cars = list(cars);
    cars.remove('Pagani Huayra')
    cars = tuple(cars)
    print(cars)


def sarcina12():
    expensive_cars = ("Ferrari", "Pagani Huayra", "McLaren Elva", "Czinger 21C")
    element1, mijloc, *_, ultimul = expensive_cars
    mijloc = expensive_cars[len(expensive_cars) // 2]
    print(element1, mijloc, ultimul)


def sarcina13():
    fruits = set()

    for i in range(1, 6):
        if i == 1:
            fruits.add("apple")
        elif i == 2:
            fruits.add("banana")
        elif i == 3:
            fruits.add("cherry")
        elif i == 4:
            fruits.add("plum")
        else:
            fruits.add("pear")

    print(fruits)


def sarcina14():
    fruits = {"apple", "banana", "cherry", "plum", "pear"}
    vegetables = {"carrot", "tomato", "potato", "cucumber", "eggplant"}

    print(fruits.difference(vegetables))


def sarcina15():
    fruits = {"apple", "banana", "cherry", "plum", "pear"}
    vegetables = {"carrot", "tomato", "potato", "cucumber", "eggplant"}
    food = fruits.union(vegetables)
    print(food)


def sarcina16():
    word_list = {
        'tenacious': {
            'type': 'adjective',
            'meaning': 'holding together'
        },
        'repristinate':
            {'type': 'verb',
             'meaning': 'to restore to the first or original state or condition'},
        'gul': {
            'type': 'noun',
            'meaning': 'a large octagonal design derived from the shape of a rose, a motif on Oriental rugs'
        },
        'alluvion': {
            'type': 'noun',
            'meaning': 'a gradual increase of land on a shore or a river bank by the action of water, whether from natural or artificial causes'
        },
        'superannuated': {
            'type': 'adjective',
            'meaning': 'antiquated or obsolete'
        },
        'in medias res': {
            'type': 'adverb',
            'meaning': 'in the middle of things'
        },
        'lambent': {
            'type': 'adjective',
            'meaning': 'running or moving lightly over a surface'
        }
    }
    return word_list


def sarcina17():
    print(sarcina16().items())


# sarcina 18
def display_word_by_type(word_type):
    for key, value in sarcina16().items():
        if value['type'] == word_type:
            print(f"Term {key} is a/an {value['type']}. Meaning: {value['meaning']}")


# sarcina 19
def sort_dict_alpha(dict_obj):
    sorted_dict = dict(sorted(dict_obj.items()))
    return sorted_dict


def sarcina20():
    # df eto dataFrame
    df = pd.read_excel('D:\\usarb\\Sisteme_Inteligente_Lab1\\List of languages by total number of speakers.xlsx')
    mean_L1 = df['First-language(L1)speakers(millions)'].median()

    df['First-language(L1)speakers(millions)'] = df['First-language(L1)speakers(millions)'].fillna(mean_L1)

    print(df.tail(30))

    df = df[df['Second-language(L2)speakers'] != "--"]

    def defineDuplicated():
        duplicates = df[df.duplicated()]

        if not duplicates.empty:
            print("Duplicatele gasite:")
            print(duplicates.index.values)
        else:
            print("Duplicate nu au fost gasite")

    # gasirea si stergerea duplicatelor
    defineDuplicated()
    df = df.drop_duplicates()

    # salveaza filurile in excel excel
    df.to_excel('D:\\usarb\\Sisteme_Inteligente_Lab1\\result.xlsx', index=False)


if __name__ == '__main__':
    # sarcina1()
    # sarcina2()
    # sarcina3()
    # sarcina4()
    # sarcina5()
    # sarcina6()
    # sarcina7()
    # sarcina8()
    # sarcina9()
    # sarcina10()
    # sarcina11()
    # sarcina12()
    # sarcina13()
    # sarcina14()
    # sarcina15()
    # sarcina16()
    # sarcina17()
    # display_word_by_type('adjective')
    # print(sort_dict_alpha(sarcina16()))
    sarcina20()
