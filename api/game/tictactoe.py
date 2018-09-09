
import random


def game(grid):
   
    #Convert to list and join to return required characters
    convert_to_list = [j for i in grid for j in i]

    #Pick position to play randomly
    #pm -> possible_moves
    #ptp -> position_to_play

    pm = [i for i, item in enumerate(convert_to_list) if item == " "]
    ptp = random.choice(pm)

    convert_to_list[ptp] = "o"
    
    result = "".join(convert_to_list)
    return result