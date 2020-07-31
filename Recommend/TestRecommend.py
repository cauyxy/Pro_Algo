from Recommend.recommend import Recommend
id=[3,4]
Grades=[[100,50],[50,50],[50,100],[100,100]]
for Grade in Grades:
    print("两个知识点得分："+str(Grade[0])+","+str(Grade[1]))
    Nodes=Recommend(id,Grade)
    for node in Nodes:
        print(node.name)
