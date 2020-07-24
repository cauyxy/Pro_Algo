from models import *

def cmp1(node1,node2):
    return node1.level <= node2.level

def cmp2(node1,node2):
    return node1.time <= node2.time