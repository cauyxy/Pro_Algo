from models import load2prog
from Search.search import Search
data=load2prog("./data.dat")
SearchRes=Search("素")
for node in SearchRes:
    MatchTarget = [node.id, node.name, node.desc, node.level]
    for line in MatchTarget:
        print(line)

