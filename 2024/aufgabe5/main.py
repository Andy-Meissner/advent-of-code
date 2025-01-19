import math
from os.path import dirname

rules = {}
orders = []

def next_incorrect_number(order, i):
    for item in order[i+1:-1]:
        if item in rules[order[i]]:
            return item
    return None

with open(dirname(__file__) + "/input.txt", "r") as f:
    lines = f.readlines()

    for l in lines:
        l_split = l.rstrip('\n').split("|")
        if len(l_split) == 2:
            if l_split[0] not in rules:
                rules[l_split[0]] = [l_split[1]]
            else:
                rules[l_split[0]].append(l_split[1].strip())
        else:
            order = l_split[0].split(",")
            if len(order) > 1:
                orders.append({"order": order})
    
    for order in orders:
        order["order"].reverse()
        order["reordered"] = order["order"].copy()
        for i in range(len(order["order"])):
            if next_incorrect_number(order["order"], i):
                order["invalid"] = True
                break

        if not "invalid" in order:
            order["invalid"] = False
        
        order["order"].reverse()
        order["reordered"].reverse()

for order in [x["reordered"] for x in orders if x["invalid"]]:
    unordered = True    
    while unordered:
        unordered = False
        for idx, nr in enumerate(order):
            intersect = set(order[idx:]) & set(rules[nr])
            if len(intersect) > 0:
                idx_of_last = order.index(list(intersect)[-1])
                order[idx], order[idx_of_last] = order[idx_of_last], order[idx]
                unordered = True
                break

        
sum = 0
sum2 = 0

for order in orders:
    if not order["invalid"]:
        sum += int(order["order"][math.floor(len(order["order"]) / 2)])
    else:
        sum2 += int(order["reordered"][math.floor(len(order["reordered"]) / 2)])

print("\n")
print(str(sum) )
print(str(sum2) + "\n")
