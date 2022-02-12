from enum import Enum
import collections

class Cities (Enum):
    Minsk = 'минск'
    Vitebsk = 'витебск'
    Mogilev = 'могилев'
    Gomel = 'гомель'
    Grodno = 'гродно'
    Brest = 'брест'

def find_city (str):
    list_cities = [Cities.Brest, Cities.Minsk, Cities.Gomel, Cities.Grodno, Cities.Mogilev, Cities.Vitebsk]
    list_word = str.split()
    result = []

    for word in list_word:
        for city in list_cities:
            if word.lower() == city.value:
                result.append(word)

    return result

if __name__ == '__main__':
    print(find_city('привет грОдно ВитЕбск пока минСк'))
