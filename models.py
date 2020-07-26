import pickle


class Node:
    def __init__(self, id, name, cate, level, time, desc):
        self.id = id
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

    def __le__(self, other):
        return self.level <= other.level

    def __lt__(self, other):
        return self.level < other.level

    def setLevel(self, level):
        self.level = level


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

def To_Graph():      #创建图的邻接矩阵
    Nodes = load2prog('../data.dat')
    length=len(Nodes)
    edgs=[[float('inf')] * length for _ in range(length)]
    for node in Nodes:
        for aft_node in node.aft_list:
            edgs[node.id-1][aft_node.id-1]=1
    return edgs



