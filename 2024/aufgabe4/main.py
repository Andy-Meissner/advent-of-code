from os.path import dirname



def func1():
    directions = [
        (1,0),
        (1,1),
        (0,1),
        (-1,1),
        (-1,0),
        (-1,-1),
        (0,-1),
        (1,-1)
    ]

    counts = 0
    with open(dirname(__file__) + "/input.txt", "r") as f:
        lines = f.readlines()
        height = 140
        width = 140
        for i in range(0, height):
            for j in range(0, width):
                def find_char_in_direction(char: str, x:int, y:int, distance):
                    new_i = i + distance * x
                    new_j = j + distance * y
                    if new_j < width and new_j >= 0 and new_i < height and new_i >= 0:
                        return lines[new_i][new_j] == char
                    
                if lines[i][j] == 'X':
                    for x_offset, y_offset in directions:
                        if find_char_in_direction('M', x_offset, y_offset, 1) \
                            and find_char_in_direction('A', x_offset, y_offset, 2) \
                                and find_char_in_direction('S', x_offset, y_offset, 3):
                            counts+=1
    print(str(counts))
          
def func2():
    directions = [
        (1,1),
        (-1,1),
        (-1,-1),
        (1,-1)
    ]

    counts = 0
    with open(dirname(__file__) + "/input.txt", "r") as f:
        lines = f.readlines()
        height = 140
        width = 140
        for i in range(0, height):
            for j in range(0, width):
                def find_char_in_direction(char: str, x:int, y:int):
                    new_i = i+ x
                    new_j = j + y
                    if new_j < width and new_j >= 0 and new_i < height and new_i >= 0:
                        return lines[new_i][new_j] == char
                    
                if lines[i][j] == 'A':
                    for x_offset, y_offset in directions:
                        if find_char_in_direction('M', x_offset, y_offset) and find_char_in_direction('S', -x_offset, -y_offset): 
                            if find_char_in_direction('M', -x_offset, y_offset) and find_char_in_direction('S', x_offset, -y_offset) or \
                               find_char_in_direction('M', x_offset, -y_offset) and find_char_in_direction('S', -x_offset, y_offset):
                                counts+=1
                                break
    print(str(counts))                  
print('\n')         
func1()
func2()