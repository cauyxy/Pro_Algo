import pickle


class Node:
    def __init__(self, name, cate, level, time, desc):
        self.name = name
        self.cate = cate
        self.level = level
        self.time = time
        self.desc = desc
        self.pre_list = []
        self.aft_list = []

    def addNode(self, node, pre=True):
        if pre:
            self.pre_list.append(node)
        else:
            self.aft_list.append(node)


def dump2file(filename, Nodes):
    with open(filename, "wb") as f:
        pickle.dump(len(Nodes), f)
        for Node in Nodes:
            pickle.dump(Node, f)


def load2prog(filename):
    with open(filename, "rb") as f:
        num_nodes = pickle.load(f)
        Nodes = []
        for _ in range(num_nodes):
            Nodes.append(pickle.load(f))
    return Nodes
