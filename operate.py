from models import *

Nodes = []

node1_1=Node(1,'绪论1.1',1,1,1,'数据结构的相关概念')
node1_2=Node(2,'绪论1.2',1,2,1,'数据结构的时空分析方法')
node2_1=Node(3,'线性表2.1',2,2,2,'顺序存储线性表的定义以及查找插入删除等操作')
node2_2=Node(4,'线性表2.2',2,3,2,'单链表的定义及基本操作，循环链表的定义及基本操作，双向链表的定义及基本操作')
node3_1=Node(5,'栈队列3.1',3,2,1,'栈和队列的逻辑及存储结构')
node3_2=Node(6,'栈队列3.2',3,2,1,'栈和队列的基本操作实现')
node4_1=Node(7,'串4.1',4,2,2,'串的逻辑以及存储结构')
node4_2=Node(8,'串4.2',4,4,2,'串的模式匹配')

node1_2.addNode(node1_1)
node2_1.addNode(node1_2)
node2_2.addNode(node1_2)
node3_1.addNode(node2_1)
node3_1.addNode(node2_2)
node3_2.addNode(node3_1)
node4_1.addNode(node2_1)
node4_1.addNode(node2_2)
node4_2.addNode(node4_1)

Nodes.append(node1_1)
Nodes.append(node1_2)
Nodes.append(node2_1)
Nodes.append(node2_2)
Nodes.append(node3_1)
Nodes.append(node3_2)
Nodes.append(node4_1)
Nodes.append(node4_2)

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
