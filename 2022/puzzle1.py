with open("input1.txt") as f:
    lines = f.readlines()

elves = []

elvesum = 0
for line in lines:
    if line == "\n":
        elves.append(elvesum)
        elvesum = 0
    else:
        elvesum += int(line)

sorted_elves = sorted(elves,reverse=True)

print(sorted_elves[0])
print(sorted_elves[0]+sorted_elves[1]+sorted_elves[2])

