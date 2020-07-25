from models import load2prog
nodes=load2prog("../data.dat")
PreNodeList=[]
def DFS(node):
    for Pre_node in node.pre_list:
        if(Pre_node not in PreNodeList):
            PreNodeList.append(Pre_node)
            FindPre(Pre_node)
def FindPre(node):
    DFS(node)
    return PreNodeList

