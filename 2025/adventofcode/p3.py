
def walk_the_line(l):
    maxnr = 0
    index = -1
    for i, c in enumerate(l):
        if int(c) > maxnr:
            maxnr = int(c)
            index = i

    return index, maxnr
        


def find_max_joltage(line: str) -> int:
    joltage = 0
    index = 0
    for i in range(12, 0, -1):
        endx = -i+1
        if endx == 0:
            nidx, val = walk_the_line(line[index:])
        else:
            nidx, val = walk_the_line(line[index:endx])
        index += nidx + 1
        joltage = joltage * 10 + val
    return joltage

joltages = []

with open("adventofcode/p3.txt") as f:
    lines = f.readlines()

for l in lines:
    joltages.append(find_max_joltage(l.strip()))

print("\n")
#print(find_max_joltage("818181911112111"))
print(f"The total joltage output is {sum(joltages)}")