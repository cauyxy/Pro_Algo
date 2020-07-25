from models import load2prog
nodes=load2prog("../data.dat")
def DFS(node,PreNodeList):
    for Pre_node in node.pre_list:
        if(Pre_node not in PreNodeList):
            PreNodeList.append(Pre_node)
            FindPre(Pre_node,PreNodeList)
def FindPre(node):
    PreNodeList = []
    DFS(node,PreNodeList)
    return PreNodeList


