from flask import jsonify
import random
import numpy as np


def game(character_list):
   
    """
    9 possible moves - play any of the corners with indices[0,2,6,8]
    8 possible moves - if a corner played play the opposite corner
                     - if no corner played ,play any random corner

    7 possible moves - play any available corner
    6 possible moves - check if any possible win and block, if none play available corner
    5  and below - repeat process
    """

    #pm -> possible_moves
    #ptp -> position_to_play

    pm = character_list.count(" ")

    if pm == 9:
        choices = [0, 2, 4, 6]
        ptp = random.choice(choices)
        character_list[ptp] = "o"

        result = "".join(character_list)
        return result

    if pm == 8:
        choices = [0, 2, 4, 6]
        
        if character_list[0] != " ":
            character_list[6] = "o"
            result = "".join(character_list)
            return result
        elif character_list[2] != " ":
            character_list[4] = "o"
            result = "".join(character_list)
            return result
        elif character_list[4] != " ":
            character_list[2] = "o"
            result = "".join(character_list)
            return result
        elif character_list[6] != " ":
            character_list[0] = "o"
            result = "".join(character_list)
            return result
        else:
            ptp = random.choice(choices)
            character_list[ptp] = "o"
            result = "".join(character_list)
            
            return result
    if pm == 7:
        if character_list[0] != " ":
            character_list[0] = "o"
            result = "".join(character_list)
            return result

        elif character_list[2] != " ":
            character_list[0] = "o"
            result = "".join(character_list)
            return result

        elif character_list[4] != " ":
            character_list[4] = "o"
            result = "".join(character_list)
            return result

        elif character_list[6] != " ":
            character_list[6] = "o"
            result = "".join(character_list)
            return result

    if pm <= 6:
        blocking_check  = [[0,1,2],[0,3,6],[3,4,5],[1,4,7],[6,7,8],[2,5,8],[0,4,8],[2,4,6]]

        block_move = block(character_list,*blocking_check)

        if block_move:
            character_list[block_move] = "o"
            result = "".join(character_list)
            return result
        else :
            if character_list[0] != " ":
                character_list[0] = "o"
                result = "".join(character_list)
                return result

            elif character_list[2] != " ":
                character_list[0] = "o"
                result = "".join(character_list)
                return result

            elif character_list[4] != " ":
                character_list[4] = "o"
                result = "".join(character_list)
                return result

            elif character_list[6] != " ":
                character_list[6] = "o"
                result = "".join(character_list)
                return result
   
def block(character_list, *check_list):
    c = character_list

    for item in check_list:
        if ((c[item[0]] == c[item[1]]) and c[item[2]] == " "):
            return item[2]
        elif ((c[item[1]] == c[item[2]]) and c[item[0]] == " ") :
            return item[0]
        elif ((c[item[0]] == c[item[2]])  and c[item[1]] == " "):
            return item[1]
              
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
