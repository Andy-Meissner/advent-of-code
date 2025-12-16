with open("adventofcode/p5_test.txt") as f:
    lines = f.readlines()
with open("adventofcode/p5.txt") as f:
    lines = f.readlines()

def merge_ranges(new_range: tuple[int,int], existing_range: tuple[int,int]):
    merged_range = existing_range
    other_range = None
    if new_range[0] <= existing_range[0] and new_range[1] >= existing_range[0]:
        merged_range = (new_range[0], existing_range[1])
    if new_range[1] >= existing_range[1] and new_range[0] <= existing_range[1]:
        merged_range = (existing_range[0], new_range[1])
    if new_range[0] < existing_range[0] and new_range[1] > existing_range[1]:
        merged_range = (new_range[0], new_range[1])
    if existing_range == merged_range:
        other_range = new_range
    
    return merged_range, other_range

fresh_ranges = []
fresh_ids = []

for current_range in lines:
    current_range = current_range.strip()
    if "-" in current_range:
        spl = current_range.split("-")
        merge_found = False
        new_range = (int(spl[0]), int(spl[1]))
        for existing_range in fresh_ranges:
            merged, other = merge_ranges(new_range, existing_range)
            if merged != existing_range:
                merge_found = True
                break
        if not merge_found:
            fresh_ranges.append(new_range)
    else:
        if len(current_range) > 0:
            for existing_range in fresh_ranges:
                i = int(current_range)
                if existing_range[0] <= i and existing_range[1] >= i:
                    fresh_ids.append(i)
                    break

print(f"Fresh Ids: {len(fresh_ids)}")

sorted_ids = sorted(fresh_ranges, key=lambda x: x[0])

merged_ids = []

i = 0
while True:
    if i >= len(sorted_ids) -1:
        merged_ids.append(sorted_ids[i])
        break
    cur_range = sorted_ids[i]
    next_r = sorted_ids[i+1]
    merged = merge_ranges(next_r, cur_range)
    if merged == cur_range:
        i += 1
        merged_ids.append(merged)
    else:
        sorted_ids[i] = merged
        sorted_ids.pop(i+1)

for l in merged_ids:
    print(l)

ctr = 0
for existing_range in fresh_ranges:
    ctr += existing_range[1] - existing_range[0] + 1


print(f"All Fresh Ids: {ctr}")