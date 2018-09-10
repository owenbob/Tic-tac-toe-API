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
from api.game.tictactoe import game,winning_criteria


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

    check_results = winning_criteria(board)

    if type(check_results) is list:
        result = game(check_results)
        api_win = winning_criteria(result)
        if type(api_win) is list:
            return result
        else:
            return api_win
    else:
        return check_results
