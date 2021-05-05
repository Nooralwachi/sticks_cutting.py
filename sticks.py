def stick_cutting(sticks): 
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

print(stick_cutting([1,2,3]))
print(stick_cutting([]))
print(stick_cutting([1,1,1]))
print(stick_cutting([2,10]))
print("=============")

def stick_cutting2(sticks): 
    result = []
    sticks = sorted(sticks) 
    m =0
    for item in sticks:
        if item == m:
            continue
        m =item
        result.append(len(sticks)) 
        sticks =sticks[1:]
    return result

print(stick_cutting2([1,2,3]))
print(stick_cutting2([]))
print(stick_cutting2([1,1,1]))
print(stick_cutting2([2,10]))
print("=============")


def stick_cutting3(sticks): 
    result = []
    m =0
    for item in sticks:
        if item <m:
            m -=item
        else:
            m =item
        result.append(len(sticks)) 
        sticks =sticks[1:]
    return result

print(stick_cutting2([1,2,3]))
print(stick_cutting2([]))
print(stick_cutting2([1,1,1]))
print(stick_cutting2([2,10]))
print("=============")
