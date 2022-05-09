def find_city (str):
    list_word = str.split()
    result = []
    list_cities = {'минск', 'витебск', 'могилев', 'гродно', 'гомель', 'брест'}
    for word in list_word:
        if word.lower() in list_cities:
            result.append(word)

    return result

if __name__ == '__main__':
    print(find_city('привет грОдно ВитЕбск пока минСк'))
