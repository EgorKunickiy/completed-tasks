import re

def split_line(str):
    name = re.search(r'(\w+).(\w+).(\w+).', str)
    #(\w+).(\w+).(\w+). здесь ищется 3 последовательности символов разделенный пробелом
    print((name.group(1).capitalize()),
          (name.group(2).capitalize()),
          (name.group(3).capitalize()), sep='\n')
if __name__ == '__main__':
    split_line('QWER SdfgH xFvGn 1234567yregh')