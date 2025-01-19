from __future__ import annotations
from enum import Enum

class GameChoice(Enum):
    rock = 1
    paper = 2
    scissors = 3

    def get_win(el: GameChoice) -> GameChoice:
        match el:
            case GameChoice.rock:
                return GameChoice.paper
            case GameChoice.paper:
                return GameChoice.scissors
            case GameChoice.scissors:
                return GameChoice.rock

    def get_loose(el: GameChoice) -> GameChoice:
        match el:
            case GameChoice.rock:
                return GameChoice.scissors
            case GameChoice.paper:
                return GameChoice.rock
            case GameChoice.scissors:
                return GameChoice.paper


def decode_opponents_choice(choice):
    match choice:
        case "A":
            return GameChoice.rock
        case "B":
            return GameChoice.paper
        case "C":
            return GameChoice.scissors

with open("input2.txt") as f:
    lines = f.readlines()

rounds = []

for line in lines:
    line = line.removesuffix("\n")
    split = line.split(" ")
    opponents_choice = decode_opponents_choice(split[0])
    match split[1]:
        case "X": #WIN
            rounds.append(GameChoice.get_loose(opponents_choice).value)
        case "Y": #TIE
            rounds.append(opponents_choice.value + 3)
        case "Z": #LOOSE
            rounds.append(GameChoice.get_win(opponents_choice).value + 6)

print(sum(rounds))
            
