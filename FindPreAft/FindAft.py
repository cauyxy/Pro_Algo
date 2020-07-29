from models import load2prog
nodes=load2prog("data.dat")
def DFS(node, AftNodeList):
    for Aft_node in node.aft_list:
        if(Aft_node not in AftNodeList):
            AftNodeList.append(Aft_node)
            DFS(Aft_node, AftNodeList)
def FindAft(node):
    AftNodeList = []
    DFS(node,AftNodeList)
    return AftNodeList