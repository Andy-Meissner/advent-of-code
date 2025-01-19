from enum import Enum

class GameChoice(Enum):
    rock = 1
    paper = 2
    scissors = 3



def decode_opponents_choice(choice):
    match choice:
        case "A":
            return GameChoice.rock
        case "B":
            return GameChoice.paper
        case "C":
            return GameChoice.scissors

def decode_my_choice(choice):
    match choice:
        case "X":
            return GameChoice.rock
        case "Y":
            return GameChoice.paper
        case "Z":
            return GameChoice.scissors

with open("input2.txt") as f:
    lines = f.readlines()

rounds = []

for line in lines:
    line = line.removesuffix("\n")
    split = line.split(" ")
    opponents_choice = decode_opponents_choice(split[0])
    my_choice = decode_my_choice(split[1])


    if (my_choice == GameChoice.scissors and opponents_choice == GameChoice.rock 
    or  my_choice == GameChoice.rock and opponents_choice == GameChoice.paper
    or  my_choice == GameChoice.paper and opponents_choice == GameChoice.scissors):
        rounds.append(int(my_choice.value))
    elif(my_choice == opponents_choice):
        rounds.append(int(my_choice.value) + 3)
    else:
        rounds.append(int(my_choice.value) + 6)

print(sum(rounds))

