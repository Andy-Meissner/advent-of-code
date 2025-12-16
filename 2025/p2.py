def repeats(nr: str) -> bool:
    if len(nr) % 2 != 0 or nr.startswith("0"):
        return False
    return nr[0:int(len(nr)/2)] == nr[int(len(nr)/2):len(nr)]

def repeats_any(nr:str) -> bool:
    ln = len(nr)
    for parts in range(2, ln+1):
        if len(nr) % parts == 0:
            repeats = True
            part_len = int(len(nr) / parts)
            starting_nr= nr[0:part_len]
            for i in range(0, parts):
                part = nr[i*part_len:(i+1)*part_len]
                if part != starting_nr:
                    repeats = False
                    break
            if repeats:
                return True        
    return False


with open("adventofcode/p2.txt") as f:
    ranges = f.read().strip().split(",")

invalid_ids = []
for r in ranges:
    start, end = r.split("-")
    print(f"Processing range {start}->{end}")
    for i in range(int(start), int(end) +1):
        #if repeats(str(i)):
            #invalid_ids.append(i)
            # print(f"Found invalid ID: {i}")
        if repeats_any(str(i)):
            invalid_ids.append(i)
            print(f"Found invalid ID: {i}")
        
print(f"Sum of invalid IDs: {sum(invalid_ids)}")