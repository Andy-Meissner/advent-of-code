
def count_total_rolls(neighbours):
    cnt = 0
    for l in neighbours:
        for c in l:
            if c == "@":
                cnt+= 1
    return cnt -1


def find_accessable_rolls(lines: list[str], threshold, adjacent = 1):
    height = len(lines)
    width = len(lines[0])

    rolls = 0
    
    replaced = lines.copy()

    for x in range(0, width):
        for y in range(0, height):
            if lines[y][x] == "@":
                x_adj_idx_lower = max(x-adjacent, 0)
                x_adj_idx_upper = min(x+adjacent, width)
                y_adj_idx_lower = max(y-adjacent, 0)
                y_adj_idx_upper = min(y+adjacent, height)
                
                adj_l = lines[y_adj_idx_lower:y_adj_idx_upper+1]
                n = []
                for l in adj_l:
                    n.append(l[x_adj_idx_lower:x_adj_idx_upper+1])


                cnt = count_total_rolls(n)
                if cnt < threshold:
                    rolls+=1
                    replaced[y] = replaced[y][:x] + "x" + replaced[y][x+1:]

    return rolls, replaced


test = (
"..@@.@@@@.\n"
"@@@.@.@.@@\n"
"@@@@@.@.@@\n"
"@.@@@@..@.\n"
"@@.@@@@.@@\n"
".@@@@@@@.@\n"
".@.@.@.@@@\n"
"@.@@@.@@@@\n"
".@@@@@@@@.\n"
"@.@.@@@.@.")

lines = test.split("\n")

with open("adventofcode/p4.txt") as f:
    lines = f.read().splitlines()

total_rolls = 0
removed_rolls, last_arr = find_accessable_rolls(lines, 4)
total_rolls += removed_rolls

print(f"Removed {removed_rolls}")

while lines != last_arr:
    lines = last_arr
    removed_rolls, last_arr = find_accessable_rolls(lines, 4)
    print(f"Removed {removed_rolls}")
    total_rolls += removed_rolls
    

print(f"\n The number of accessable rolls is {total_rolls}")
