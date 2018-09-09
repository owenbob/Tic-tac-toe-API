"""
Module to handle API endpoint for get

Numpy Module to handle the game grid.
- Declare a game grid that is a 3 by 3 matrix
- Check for a win
- Check for a draw
- Check if board is valid(number of times the players have played)
- check for sucess loop through a list of possible success
"""



from flask import Flask, request, jsonify
from api.game.tictactoe import game


import numpy as np

import re


app = Flask(__name__)


@app.route("/", methods=["GET"])
def tic_tac_toe():
    board = request.args.get("board")
    
    #Check length to ensure board is of 9 characters
    if len(board) != 9:
        return jsonify({
            "Message":"Invalid board length"
        }),400

    #Check if there only 'x','o' and space characters
    if any(character not in 'xo ' for character in board):
        return jsonify({
        "Message":"Invalid character provided"
    }),400

    #Check is the board is valid for number of plays
    user_plays = board.count("x")
    api_plays = board.count("o")
    if not(user_plays == api_plays or (abs(user_plays-api_plays) == 1)):
        return jsonify({
            "Message":"Invalid board, User or API has played multiple times"
        }),400

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
                [g[0,2],g[1,1],g[0,2]]
                ] 

    winning_check = ["".join(x) for x in criteria]
        
    user_win = winning_check.count("xxx")
    api_win = winning_check.count("ooo")
    

    #Convert grid to list to check for a draw
    convert_to_list = [j for i in grid for j in i]

    if  user_win == 1:
        return jsonify({
            "Message": "Congratulations, You win"
        }),200
    elif api_win == 1:
        return jsonify({
            "Message": "Hard Luck, You lose"
        }),200
    elif " " not in convert_to_list:
        return jsonify({
            "Message": "It is a Draw"
        }),200
    else:
        result = game(convert_to_list,grid)
        return result,200

    
    