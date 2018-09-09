"""
Module to test for :
 - Invalid board length
 - Invalid character provided
 - Invalid board with multiple plays
 - check for  user win
 - check for user lose
 - check for draw
 - check for proper game play

"""
from unittest import TestCase


from api.views.controller import app


class TicTacToeTest(TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_invalid_board_length(self):

        response = self.client.get("/?board=+xxo++o++x")
        assert response.status_code == 400

    def test_invalid_character_provided(self):

        response = self.client.get("/?board=+xxob+o++")
        assert response.status_code == 400

    def test_invalid_board_with_multiple_plays(self):
        response = self.client.get("/?board=o+xoox++o")
        assert response.status_code == 400

    def test_check_user_win(self):
        response = self.client.get("/?board=x+o+xo++x")
        assert response.status_code == 200

    def test_check_for_user_loss(self):
        response = self.client.get("/?board=+o++oxxo+")
        assert response.status_code == 200

    def test_check_for_draw(self):
        response = self.client.get("/?board=xoooxxxxo")
        assert response.status_code == 200

    def test_check_normal_game_play(self):
        response = self.client.get("/?board=+xxo++o++")
        import pdb ; pdb.set_trace()
        assert response.status_code == 200

    

