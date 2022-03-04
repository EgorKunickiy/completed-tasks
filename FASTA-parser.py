import re


def find_data(string: str):
    result_1 = re.search(r'(\w*) ', string)
    result_2 = re.search(r' (.*)\n', string)
    return [result_1.group(1), result_2.group(1)]


class ReaderFASTA:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'r')
        self.__list_of_sequence = []

    @property
    def get_list_of_sequence(self):
        return self.__list_of_sequence

    def read_sequence(self):
        self.__read(self.file)

    def __read(self, file):
        id_par = ''
        description = ''
        sequence = ''
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Sequence:
    def __init__(self, id, description, sequence):
        self.__id = id
        self.__description = description
        self.__sequence = sequence

    @property
    def get_id(self):
        return self.__id

    @property
    def get_sequence(self):
        return self.__sequence

    @property
    def get_description(self):
        return self.__description


if __name__ == "__main__":
    with ReaderFASTA('abcd.fasta') as reader:
        reader.read_sequence()

    for seq in reader.get_list_of_sequence:
        print(seq.get_id)
        print(seq.get_description)
        print(seq.get_sequence)
