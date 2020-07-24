#coding:utf-8
'''
BF算法
'''
def BF(input,target):
    location=[]
    target_length = len(target)
    input_length = len(input)
    for i in range(target_length-input_length+1):
        loc=i
        for j in range(input_length):
            if target[loc]==input[j]:
                loc=loc+1
            else:
                break
        if loc-i==input_length:
            location.append(loc)
    return location

if __name__=="__main__":
    input= "因为"
    target="因为有你在，所以我才能分词，而不是因为算法厉害"
    print(BF(input, target))
