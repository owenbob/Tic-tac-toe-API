"""
    If X does not play center opening move (playing a corner is the best opening move), 
    take center, and then a side middle. This will stop any forks from happening. 
    If O plays a corner, a perfect X player has already played the corner opposite their first 
    and proceeds to play a 3rd corner, stopping O's 3-in-a-row and making their own fork.
    If X plays center opening move, O should pay attention and not allow a fork. 
    X should play a corner first.
        If O takes center (best move for them), X should take the corner opposite the original, 
        and proceed as detailed above.
        If O plays a corner or side-middle first, X is guaranteed to win:
            If corner, X simply takes any of the other 2 corners, and then the last, a fork.
            If O plays a side-middle, X takes the only corner that O's blocking won't make 2 in a row. O will block, 
            but the best of the other two will be seen by X, and O is forked. The only way that X must lose is if O 
            plays middle and then a side-middle.
"""

import numpy as np
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