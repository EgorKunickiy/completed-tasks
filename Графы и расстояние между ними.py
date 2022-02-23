import numpy
import csv

class Reader_csv():
    def read_csv(self):
        with open('tree2.csv') as File:
            self.__result = []
            self.__reader_result = csv.DictReader(File, delimiter=';')
            for row in self.__reader_result:
                self.__result.append(row)
        return self.__result

    def build_dict(self):
        intermediate_dict = self.read_csv()
        result = dict()
        for dictionary in intermediate_dict:
            keys = tuple(dictionary.keys())
            if int(dictionary[keys[0]]) in result:
                result[int(dictionary[keys[0]])] += [int(dictionary[keys[1]])]
            else:
                result[int(dictionary[keys[0]])] = [int(dictionary[keys[1]])]
        return result

class Graph:
    def __init__(self, V, E, dictionary):
        self.V = V
        self.E = E
        self.graph = dictionary

    def Bfs(self, start, end):
        num_bfs = numpy.zeros(self.V)
        num_bfs[start - 1] = 1
        search_deque = []
        search_deque += [start]
        ine = 1
        pr = numpy.full(self.V, -1, 'int32')
        for i1 in search_deque:
            if i1 in self.graph.keys():
                for j in self.graph[i1]:
                    if num_bfs[j - 1] == 0:
                        ine += 1
                        num_bfs[j - 1] = ine
                        search_deque.append(j)
                        pr[j - 1] = i1
        self.Way(start, end, pr)

    def Way(self, start, end, arr):
        res = [end]
        i = arr[end - 1]
        while i != start:
            res.append(i)
            i = arr[i - 1]
            if i == -1 :
                print('No way')
                return 0
        res.append(start)
        res = res[::-1]
        print(*res, sep='->')


if __name__ == '__main__':
    d = {1: [2, 5],
         2: [1, 3, 6],
         3: [2, 4, 6],
         4: [3, 5],
         5: [1, 4],
         6: [2, 3, 7],
         7: [6]}

    graph = Graph(7, 8, d)
    graph.Bfs(1, 7)

    graph2 = Graph(9, 9, Reader_csv().build_dict())
    print(graph2.graph)
    graph2.Bfs(0, 4)
