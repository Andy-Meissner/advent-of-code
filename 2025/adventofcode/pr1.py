import math

dial_val = 50
ctr= 0

with open('adventofcode/pr1.txt', 'r') as file:
    for l in  file:
        direction = l[0]
        value = int(l[1:]) 
        mod_val = value % 100
        clicks = math.floor(value / 100)
        hit = False
        nono = False
        threshold = 100 if direction == 'L' else -100
        
        if direction == 'L':
            if dial_val == 0:
                nono = True
            dial_val = dial_val - mod_val
            if dial_val < 0:
                dial_val = 100 + dial_val
                hit = True
                if not nono:
                    ctr+=1
        if direction == 'R':
            if dial_val == 0:
                nono = True
            dial_val = dial_val + mod_val
            if dial_val > 99:
                dial_val = -100 + dial_val 
                hit = True
                if not nono:
                    ctr+=1
        if not hit and dial_val == 0:
            ctr += 1
        ctr += clicks
        print(f"Dial:{l.strip()} -> {dial_val} ctr:{ctr}")

print("\n" + str(ctr))