from os.path import dirname

with open(dirname(__file__) + "/input.txt") as f:
    width = 0

    row_ctr = 0
    col_ctr = 0
    obstacles = []
    cur_pos = (0, 0)
    step_ctr = 0
    direction = (0,-1)

    while (chr := f.read(1)):
        if chr == '\n':
            row_ctr += 1
            width = col_ctr
            col_ctr = 0
        else:
            col_ctr += 1

        if chr == "#":
            obstacles.append((row_ctr, col_ctr))
        
        if chr == "^":
            cur_pos = (row_ctr, col_ctr)
    
    toggle = True
    while True:
        next_pos = (cur_pos[0] + direction[0], cur_pos[1] + direction[1])
        if next_pos in obstacles:
            if toggle:
                direction = (-direction[1], direction[0])
                toggle = False
            else:
                direction = (direction[1], direction[0])
                toggle = True
        elif next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= row_ctr:
            break
        else:
            cur_pos = next_pos
            step_ctr += 1
print("")
print(str(step_ctr))