import random
def stick_cutting1(sticks): 
    result = []
    sticks = sorted(sticks) 
    while (sticks):
        m = sticks[0] 
        result.append(len(sticks)) 
        new_sticks =[]
        for item in sticks[1:]: 
            if item -m !=0:
                new_sticks.append(item-m) 
        sticks = new_sticks 
    return result 

def stick_cutting2(sticks): 
    result = []
    sticks = sorted(sticks) 
    if sticks:
        m =sticks[0]
    for item in sticks:
        if item == m:
            continue
        m =item
        result.append(len(sticks)) 
        sticks =sticks[1:]
    return result

from collections import Counter
def stick_cutting3(sticks): 
    answer=[]
    result = Counter(sticks)
    x= sum(result.values())
    lst=sorted(result.items(), key=lambda x:(x[0],x[1]))
    for k,v in lst:
        answer.append(x)
        x-=v
    return(answer)

from collections import Counter
def stick_cutting4(sticks): 
    answer=[]
    result = Counter(sticks)
    x= sum(result.values())
    for k,v in sorted(result.items()):
        answer.append(x)
        x-=v
    return(answer)

from collections import Counter
def stick_cutting5(sticks): 
    count= Counter(sticks)
    x=sorted(count.items(), key=lambda x:x[0])
    return([i[0] for i in x])

def make_sticks(n): return [random.randint(0, 20) for _ in range(n)]
for _ in range(10):
    sticks = make_sticks(10)
    one  = stick_cutting1(sticks)
    two  = stick_cutting2(sticks)
    three= stick_cutting3(sticks)
    four = stick_cutting4(sticks)
    five = stick_cutting5(sticks)

    if one !=three !=four:
        print(sticks)
        print('1--> ',one)
        print('2--> ',two)
        print('3--> ',three)
        print('4--> ',four)
        print('5--> ',five)
        print("----")
print("=============")

for sticks in [[3,3,2],[1,2,3],[],[1,1,1],[2,10],[10, 1, 9, 18, 6, 19, 8, 8, 19, 1]]:
    one  = stick_cutting1(sticks)
    two  = stick_cutting2(sticks)
    three= stick_cutting3(sticks)
    four = stick_cutting4(sticks)
    five = stick_cutting5(sticks)
    if one !=three !=four:
    # This should never happen
        print(sticks)
        print('1--> ',one)
        print('2--> ',two)
        print('3--> ',three)
        print('4--> ',four)
        print('5--> ',five)
        print("----")
