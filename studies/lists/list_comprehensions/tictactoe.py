#!/usr/bin/env python
import os
import sys
import logging


class TicTacToe:
    MOVES = {
        'TL': (0, 0),
        'TM': (0, 1),
        'TR': (0, 2),
        'ML': (1, 0),
        'MM': (1, 1),
        'MR': (1, 2),
        'BL': (2, 0),
        'BM': (2, 1),
        'BR': (2, 2),
    }

    EXIT = 'EXIT'

    def __init__(self):
        self.game_board = [
            ['___|', '___', '|___'],
            ['___|', '___', '|___'],
            ['   |', '   ', '|   ']
        ]

        self.current_move = None
        self.to_move = 'x'
        self.game_end = False

    def print_game_board(self):
        for i in self.game_board:
            print(''.join(i))

    def get_user_input(self):
        print('\nMoves: tl = Top Left | tm = Top Middle | tr = Top Right\n'
              '\tml = Mid Left | mm = Mid Middle | mr = Mid Right\n'
              '\tbl = Bot Left | bm = Bot Middle | br = Bot Right')
        self.current_move = input('\n>>> ').upper()
        print(f'Move: {self.current_move}')

    def verify_user_input(self):
        if self.current_move == self.EXIT:
            print('Thanks for playing! Good bye!')
            sys.exit(0)

        if self.current_move not in list(self.MOVES.keys()):
            print('Invalid move. Please try again.')
            return True

    def make_valid_move(self, move) -> bool:
        try:
            target = list(self.game_board[self.MOVES[self.current_move][0]][self.MOVES[self.current_move][1]])

            if 'x' in target or 'o' in target:
                raise ValueError

            if target[-1] == '|' or '|' not in target:
                if target[1] == '_' or target[1] == ' ':
                    target[1] = move

            else:
                if target[2] == '_' or target[2] == ' ':
                    target[2] = move

            self.game_board[self.MOVES[self.current_move][0]][self.MOVES[self.current_move][1]] = ''.join(target)
            return True

        except ValueError:
            return False

    def check_game_ended(self):
        # Across
        if self.game_board[0][0][1] == self.game_board[0][1][1] == self.game_board[0][2][2]:
            return True, self.game_board[0][0][1]

        elif self.game_board[1][0][1] == self.game_board[1][1][1] == self.game_board[1][2][2]:
            return True, self.game_board[1][0][1]

        elif self.game_board[2][0][1] == self.game_board[2][1][1] == self.game_board[2][2][2]:
            return True, self.game_board[2][0][1]

        # Vertical
        elif self.game_board[0][0][1] == self.game_board[1][0][1] == self.game_board[2][0][2]:
            return True, self.game_board[0][0][1]

        elif self.game_board[0][1][1] == self.game_board[1][1][1] == self.game_board[2][1][2]:
            return True, self.game_board[0][1][1]

        elif self.game_board[0][2][1] == self.game_board[1][2][1] == self.game_board[2][2][2]:
            return True, self.game_board[0][2][1]

        else:
            return False, None

    def main_loop(self):
        while True:
            result = self.check_game_ended()
            if result[0]:
                print(f'{result[1]} wins!')

            # os.system('clear')
            print(f'To move: {self.to_move}')
            self.print_game_board()
            self.get_user_input()

            if self.verify_user_input():
                continue

            if not self.make_valid_move(self.to_move):
                print('That move is invalid, please try again.')
                continue

            if self.to_move == 'x':
                self.to_move = 'o'
                continue

            if self.to_move == 'o':
                self.to_move = 'x'
                continue

if __name__ == '__main__':
    new_game = TicTacToe()

    new_game.main_loop()
