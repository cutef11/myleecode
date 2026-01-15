num=[1,2,4,5,3,4]
target=6


def twosum(num,target):
    dic={}
    for i in range(len(num)):
        index=target-num[i]
        if (index in dic):
            print(i,dic.get(index))
        else:
            dic[num[i]]=i
    
twosum(num,target)
