import csv

class Tree():
    def __init__(self, dict_tree: dict):
        self.tree_nodes = dict_tree

    def find_node(self, id_node: str) -> list:
        if id_node in self.tree_nodes.keys():
            return [id_node, self.tree_nodes[id_node]]
        else:
            return [id_node, '']
class Reader_csv():
    def read_csv(self):
        with open('tree2.csv') as File:
            self.result = []
            self.reader_result = csv.DictReader(File, delimiter=';')
            for row in self.reader_result:
                self.result.append(row)
        return self.result

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
if __name__ == "__main__":
    tree = Tree(Reader_csv().build_dict())
    print(tree.tree_nodes)
    print(tree.find_node(6))
