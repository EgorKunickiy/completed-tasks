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
        meta = ''
        sequence = ''
        for string in file:
            if '>' in string:

                if len(meta) != 0:
                    self.__list_of_sequence.append(Sequence(meta, sequence))
                    meta = string
                    sequence = ''
                else:
                    meta += string
            else:
                sequence += string
        self.__list_of_sequence.append(Sequence(meta, sequence))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Sequence:
    def __init__(self, meta, sequence):
        self.__meta = meta
        self.__sequence = sequence

    @property
    def get_meta(self):
        return self.__meta

    @property
    def get_sequence(self):
        return self.__sequence


if __name__ == "__main__":
    with ReaderFASTA('abcd.fasta') as reader:
        reader.read_sequence()

    print(reader.get_list_of_sequence)
