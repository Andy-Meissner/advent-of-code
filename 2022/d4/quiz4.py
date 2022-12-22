lines = open("data.txt").readlines()

count1 = 0
count2 = 0

for l in lines:
    split = l.rstrip().split(",")
    s1,e1 = (int(x) for x in split[0].split("-"))
    s2,e2 = (int(x) for x in split[1].split("-"))
    d1 = s1-s2
    d2 = e1-e2

    if int(d1 <0) != int(d2 <0) or d1 == 0 or d2 == 0:
        count1 += 1
    if s1 <= e2 and s2 <= e1:
        count2 += 1

print("Solution 1: " + str(count1))
print("Solution 2: " + str(count2))