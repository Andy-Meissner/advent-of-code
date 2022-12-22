import re
import copy

lines = open("data.txt").readlines()

cargo = x = [[] for _ in range(9)]

for line in lines[0:8]:
    test = line[1::4]
    for i in range(len(test)):
        if test[i] != ' ':
            cargo[i].append(test[i])

for stapel in cargo:
    stapel.reverse()

cargo2 = copy.deepcopy(cargo)


for line in lines[10:]:
    match = re.match("move (\\d*) from (\\d*) to (\\d*)", line)
    cnt = int(match.group(1))
    mv_from = int(match.group(2))
    mv_to = int(match.group(3))

    for i in range(cnt, 0, -1):
        from_stapel_2 = cargo2[mv_from -1]
        to_stapel_2 = cargo2[mv_to -1]
        # Part 1:
        cargo[mv_to -1].append(cargo[mv_from -1].pop())
        # Part 2:
        to_stapel_2.append(from_stapel_2.pop(len(from_stapel_2) - i))

print("Solution 1:", ''.join([x[len(x)-1] for x in cargo]))
print("Solution 2:", ''.join([x[len(x)-1] for x in cargo2]))