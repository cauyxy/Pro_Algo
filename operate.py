from models import *

Nodes = []

node1 = Node("a", "b", "c", "d", "e")
node2 = Node("a", "b", "c", "d", "e")

node1.addNode(node2)


dump2file("data.dat", Nodes)
