from Search.search import Search
from models import load2prog

data = load2prog("./data.dat")
TestInput=["数组","书组","素组","线信表","数"]
for input in TestInput:
    SearchRes = Search(input)
    print("输入内容为:" + input)
    print("结果为")
    for node in SearchRes:
        MatchTarget = [node.name, node.desc]
        for line in MatchTarget:
            print(line)
