from models import load2prog
from FindPreAft.FindPre import FindPre
from FindPreAft.FindAft import FindAft
nodes=load2prog("../data.dat")
AftNodes=FindAft(nodes[0])
PreNodes=FindPre(nodes[-1])
for Nodes in [AftNodes,PreNodes]:
    print("-----------------")
    for node in Nodes:
        print(node.name)
