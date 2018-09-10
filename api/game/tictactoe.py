from flask import jsonify
import random
import numpy as np


def game(character_list):
   
    # #Convert to list and join to return required characters
    # convert_to_list = [j for i in grid for j in i]

    #Pick position to play randomly
    #pm -> possible_moves
    #ptp -> position_to_play

    pm = [i for i, item in enumerate(character_list) if item == " "]
    ptp = random.choice(pm)

    character_list[ptp] = "o"
    
    result = "".join(character_list)
    return result


def winning_criteria(board):
    #Split the board to  individual values in a list called spit_board
    split_board = [x for x in board]

    #Convert this list into a 3 by 3 numpy array
    grid = np.array(split_board).reshape(3,3)

    #Winning criteria - a list with the necessary winning criteria
    g = grid

    criteria = [g[0],
                g[1],
                g[2],
                [g[0,0],g[1,0],g[2,0]],
                [g[0,1],g[1,1],g[2,1]],
                [g[0,2],g[1,2],g[2,2]],
                [g[0,0],g[1,1],g[2,2]],
                [g[0,2],g[1,1],g[2,0]]
                ] 

    winning_check = ["".join(x) for x in criteria]
        
    user_win = winning_check.count("xxx")
    api_win = winning_check.count("ooo")

    #Convert grid to list to check for a draw
    convert_to_list = [j for i in grid for j in i]

    #return board
    if  user_win == 1:
        return jsonify({
            "Message": "Congratulations, You win",
            "Board state": board
        }),200
    elif api_win == 1:

        return jsonify({
            "Message": "Hard Luck, You lose",
            "Board state": board
        }),200
    elif " " not in convert_to_list:
        return jsonify({
            "Message": "It is a Draw",
            "Board state": board
        }),200
    else:
        return convert_to_list
    
