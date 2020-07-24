from models import *

Nodes = []

#id, name, cate, level, time, desc

node1_1=Node(1,'绪论1.1',1,1,1,'数据结构的相关概念')
node1_2=Node(2,'绪论1.2',1,2,1,'数据结构的时空分析方法')
node2_1=Node(3,'线性表2.1',2,2,2,'顺序存储线性表的定义以及查找插入删除等操作')
node2_2=Node(4,'线性表2.2',2,3,2,'单链表的定义及基本操作，循环链表的定义及基本操作，双向链表的定义及基本操作')
node3_1=Node(5,'栈队列3.1',3,2,1,'栈和队列的逻辑及存储结构')
node3_2=Node(6,'栈队列3.2',3,2,1,'栈和队列的基本操作实现')
node4_1=Node(7,'串4.1',4,2,2,'串的逻辑以及存储结构')
node4_2=Node(8,'串4.2',4,4,2,'串的模式匹配')
node5_1=Node(9,'数组广义表5.1',5,3,1,'数组和广义表的逻辑以及存储结构')
node5_2=Node(10,'数组广义表5.2',5,4,1,'数组和广义表的基本操作以及实现')
node6_1=Node(11,'树和二叉树6.1',6,3,1,'树和二叉树的逻辑以及存储结构')
node6_2=Node(12,'树和二叉树6.2',6,5,1,'树和二叉树的基本操作实现')
node6_3=Node(13,'树和二叉树6.3',6,6,1,'树和二叉树的转换，数和森林的遍历')
node6_4=Node(14,'树和二叉树6.4',6,5,1,'哈夫曼树及其应用')
node7_1=Node(15,'图7.1',7,4,2,'图的逻辑及存储结构')
node7_2=Node(16,'图7.2',7,6,2,'图的基本操作的实现')
node7_3=Node(17,'图7.3',7,10,2,'最小生成树、拓扑排序、关键路径以及最短路径的设计')
node8_1=Node(18,'查找8.1',8,7,2,'静态查找、动态查找、哈希查找方法')
node8_2=Node(19,'查找8.2',8,4,2,'查找方法效率分析')
node9_1=Node(20,'排序9.1',9,8,4,'插入、交换、选择、归并、基数排序法')


node1_2.addNode(node1_1)
node2_1.addNode(node1_2)
node2_2.addNode(node1_2)
node3_1.addNode(node2_1)
node3_1.addNode(node2_2)
node3_2.addNode(node3_1)
node4_1.addNode(node2_1)
node4_1.addNode(node2_2)
node4_2.addNode(node4_1)
node5_1.addNode(node2_1)
node5_2.addNode(node5_1)
node6_1.addNode(node2_1)
node6_1.addNode(node2_2)
node6_2.addNode(node6_1)
node6_3.addNode(node6_1)
node6_3.addNode(node6_2)
node6_4.addNode(node6_1)
node6_4.addNode(node6_2)
node7_1.addNode(node2_1)
node7_1.addNode(node2_2)
node7_2.addNode(node7_1)
node7_3.addNode(node6_1)
node7_3.addNode(node7_1)
node8_1.addNode(node6_1)
node8_2.addNode(node8_1)
node9_1.addNode(node2_1)
node9_1.addNode(node2_2)

Nodes.append(node1_1)
Nodes.append(node1_2)
Nodes.append(node2_1)
Nodes.append(node2_2)
Nodes.append(node3_1)
Nodes.append(node3_2)
Nodes.append(node4_1)
Nodes.append(node4_2)
Nodes.append(node5_1)
Nodes.append(node5_2)
Nodes.append(node6_1)
Nodes.append(node6_2)
Nodes.append(node6_3)
Nodes.append(node6_4)
Nodes.append(node7_1)
Nodes.append(node7_2)
Nodes.append(node7_3)
Nodes.append(node8_1)
Nodes.append(node8_2)
Nodes.append(node9_1)


for node in Nodes:
    for pre_node in node.pre_list:
        pre_node.aft_list.append(node)

for node in Nodes:
    print("---------------------")
    print(node.name)
    print('after_node:')
    for aft_node in node.aft_list:
        print(aft_node.name)



dump2file("data.dat", Nodes)
