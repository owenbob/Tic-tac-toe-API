# Tic-tac-toe-API

[![Build Status](https://travis-ci.org/owenbob/Tic-tac-toe-API.svg?branch=master)](https://travis-ci.org/owenbob/Tic-tac-toe-API)

## Hosted
This API is hosted on Heroku URL
```
https://tictac-toe-api.herokuapp.com/
```
```
Try  https://tictac-toe-api.herokuapp.com/?board=+xxo++o++ 
```

## Specifications
- The server will be provided the current board in a GET request, using the 'board' parameter in the query string.
- If the board string doesn't represent a valid tic-tac-toe board, or it’s not plausibly o’s turn, your server should return an HTTP response code 400 (Bad Request)
- The server always plays as o.
- Either player can go first.
- If the board is a valid tic-tac-toe board and it is plausibly o's turn, your server should return a string representation of the same board with one ‘o’ added.
-  The tic-tac-toe api should play optimally (i.e. never lose when it is possible to force a tie, or tie when it is possible to win)



## Installation
First clone this repository
```
$ git clone 
```
Create virtual environment and activate  it
```
$ virtualenv env
$ source/env/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```
## Run the application
At the terminal or console type
```
python run.py
```
To run tests  cd into tests directory run this command at the console/terminal
```
pytest pytest api/tests/tests.py
```
## Test locally
```
To test using  CURL or POSTMAN (a google chrome extention)
```
```
If I run curl YOUR_URL?board=+xxo++o++
I should get oxxo  o   (that’s o-x-x-o-space-space-o-space-space) in the body of the HTTP response.
```
#### Python Version Used
```
Python 3.6
```
