class Description:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        print('get object')
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        print('set object')
        setattr(obj, self.private_name, value)


class TextProcessor:
    list_of_words = Description()
    language = Description()

    def __init__(self, text: str, lang: str):
        self.list_of_words = text.split(' ')
        self.language = lang

    def __getattr__(self, item):
        return None

    def __getattribute__(self, item):
        if item == 'language':
            return 'no access'
        else:
            return object.__getattribute__(self, item)

    def __getitem__(self, item):
        return self.list_of_words[item]


if __name__ == "__main__":
    b = TextProcessor('qwertyujk retyu u ytrew sdf ghjk nb ertyui k ', 'En')
    print(b.list_of_words)
    print(b.language)
    print(b.g)
    print(b.list_of_words[0])

