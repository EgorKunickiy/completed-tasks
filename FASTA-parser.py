import re


def find_data(string: str):
    result_1 = re.search(r'(\w*) ', string)
    result_2 = re.search(r' (.*)\n', string)
    return [result_1.group(1), result_2.group(1)]


class ReaderFASTA:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.__list_of_sequence: list = []
        self.__read()

    @property
    def get_list_of_sequence(self):
        return self.__list_of_sequence

    def __read(self):
        file = open(self.file_name, 'r')
        id_par: str = ''
        description: str = ''
        sequence: str = ''
        for string in file:
            if '>' in string:
                if len(id_par) != 0:
                    self.__list_of_sequence.append(Sequence(id_par, description, sequence))
                    id_par, description = find_data(string)
                    sequence = ''
                else:
                    id_par, description = find_data(string)
            else:
                sequence += string
        self.__list_of_sequence.append(Sequence(id_par, description, sequence))
        file.close()


class Sequence:
    def __init__(self, id: str, description: str, sequence: str):
        self.__id: str = id
        self.__description: str = description
        self.__sequence: str = sequence

    @property
    def get_id(self):
        return self.__id

    @property
    def get_sequence(self):
        return self.__sequence

    @property
    def get_description(self):
        return self.__description

    def __str__(self):
        return f'ID: {seq.get_id}' + '\n' \
               f'DESCRIPTION: {seq.get_description}' + '\n' \
               f'SEQUENCE: {seq.get_sequence}'


if __name__ == "__main__":
    reader = ReaderFASTA('abcd.fasta')

    for seq in reader.get_list_of_sequence:
        print(seq)
