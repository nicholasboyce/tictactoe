import time
from sys import maxsize
from collections import deque

class TicTacToe:
    """A tic-tac-toe game."""

    def __init__(self, computer: bool, cpuPlayer: int):
        """Create a new game instance.

        The initial board created is empty.
        The first player is always X.
        """
        self._board = self.Board()
        self._players = self._determine_players(computer, cpuPlayer)
        self._curr_player_index = 0 #Corresponds to X
        self._curr_player : TicTacToe.Player = self._players[self._curr_player_index]
        self.finished = False

    def _determine_players(self, computer: bool, cpuPlayer: int) -> list:
        x, o = None, None
        if computer:
            if cpuPlayer == 1: #i.e. player X is the computer
                x = self.Player('X', computer)
                o = self.Player('O', not computer)
            else:
                x = self.Player('X', not computer)
                o = self.Player('O', computer)
        else: #neither is computer
            x = self.Player('X', False) #not using variable for sake of readability
            o = self.Player('O', False)
        return [x, o]
    
    def _make_choice(self) -> list:
        player = self._curr_player
        print(f'Player {player.symbol} is deciding...')
        if not player.computer:
            row = int(input("Which (zero-indexed) row? "))
            col = int(input("Which (zero-indexed) column? "))
            print("")
            return [row, col]
        else:
            start = time.perf_counter()
            choice = self._return_best_choice(self._board.state)
            end = time.perf_counter()
            time_elapsed = (end-start) * 1000

            print(f'Elapsed time in milliseconds: {time_elapsed}')
            return choice
        
    def _minimax_ab(self, curr_board : 'Board', available: list[tuple[int]], used: list[int], alpha: int, beta: int, player: str) -> int:
        """Implemented as a backtracking postorder algorithm traversing the implicit tree of choices given an initial board state.
        """
        if curr_board.is_finished():
            winner = curr_board.game_winner()
            if winner == 'X':
                return 1
            elif winner == 'O':
                return -1
            else:
                return 0
        
        # check whether to maximize value (X) or minimize value (O)
        optimal = maxsize * -1 if player == 'X' else maxsize
        
        for i in range(len(available)):
            if not used[i]:
                spot = available[i]
                used[i] = 1
                #mark the board
                curr_board.mark(spot, player)
                # return and store the value of the marked board, associate it with the position
                next_player = 'O' if player == 'X' else 'X'
                value = self._minimax_ab(curr_board, available, used, alpha, beta, next_player)
                if player == 'X':
                    optimal = max(optimal, value)
                    alpha = max(alpha, value)
                else:
                    optimal = min(optimal, value)
                    beta = min(beta, value)
                # unmark the board & restore availability
                curr_board._unmark(spot)
                used[i] = 0
                if beta <= alpha:
                    break

        return optimal

    
    def _return_best_choice(self, board: list[list[str]]) -> list:
        player = self._curr_player
        # find all possible moves from current board
        available = [(i // 3, i % 3) for i in range(9) if board[i // 3][i % 3] == ' ']
        used = [0] * len(available)

        alpha = maxsize * -1
        beta = maxsize
        # check whether to maximize value (X) or minimize value (O)
        optimal = (maxsize * -1, None) if player.symbol == 'X' else (maxsize, None)

        # for each available position mark the board
        for i in range(len(available)):
            if not used[i]:
                spot = available[i]
                self._board.mark(spot, player.symbol)
                used[i] = 1
                # return and store the value of the marked board, associate it with the position
                next_player = 'O' if player.symbol == 'X' else 'X'
                value = self._minimax_ab(self._board, available, used, alpha, beta, next_player)
                if player.symbol == 'X':
                    if value > optimal[0]:
                        optimal = (value, spot)
                    alpha = max(alpha, value)
                else:
                    if value < optimal[0]:
                        optimal = (value, spot)
                    beta = min(beta, value)
                # unmark the board & move on
                used[i] = 0
                self._board._unmark(spot)
                if beta <= alpha:
                    break

        # return the optimal position
        return optimal[1]

    def play_round(self) -> None:
        player = self._curr_player
        marked = False

        while not marked:
            choice = self._make_choice()
            marked = self._board.mark(choice, player.symbol)
            print(self._board)

        #start = time.perf_counter()
        self.finished = self._board.is_finished()
        #end = time.perf_counter()

        #time_elapsed = (end-start) * 1000

        #print(f'Elapsed time in seconds: {time_elapsed}')


        if not self.finished:
            self._curr_player_index = (self._curr_player_index + 1) % 2
            self._curr_player = self._players[self._curr_player_index]

        return None
    
    def display_result(self) -> None:
        winner = self._board.game_winner()

        if winner:
            print(f'Player {winner} has won!')
        else:
            print('It was a draw!')
    
    class Player:

        def __init__(self, symbol: str, computer: bool):
            self.symbol = symbol
            self.computer = computer

    class Board:
        """A 3x3 board for tic-tac-toe."""

        def __init__(self):
            """Create a new game board.

            state: a multidimensional array representation of the current board
            """
            self.state = [[' '] * 3 for i in range(3)]
        
        def mark(self, position: list, player: str) -> bool:
            """Marks a given position on the board with the player's corresponding symbol.

            Returns True if the given position is valid and successfully marked. Otherwise, returns False.
            """
            row, col = position
            if not self._is_valid(row, col):
                return False
            self.state[row][col] = player
            return True
        
        def _unmark(self, position: list) -> bool:
            """Unmarks a given position on the board with a string representing an available spot.

            Used primarily for backtracking purposes.
            """
            row, col = position
            if row >= 3 or col >= 3:
                return False
            self.state[row][col] = ' '
            return True
        
        def _is_valid(self, row: int, col: int) -> bool:
            """Checks validity of given position to be marked."""
            if row >= 3 or col >= 3:
                return False
            elif self.state[row][col] != ' ':
                return False
            return True
        
        def is_finished(self) -> bool:
            """Checks whether or not the game is finished."""
            if self.game_winner():
                return True
            
            for row in range(3):
                for col in range(3):
                    if self.state[row][col] == ' ':
                        return False
                    
            return True

        def game_winner(self) -> str:
            """Returns the winner of the current board."""
            winner = ''
            # check all rows
            for row in range(3):
                if (self.state[row][0] == self.state[row][1] == self.state[row][2]) and (self.state[row][0] != ' '):
                    winner = self.state[row][0]

            #check all cols
            for col in range(3):
                if (self.state[0][col] == self.state[1][col] == self.state[2][col]) and (self.state[0][col] != ' '):
                    winner = self.state[0][col]

            #check diagonals
            if ((self.state[0][0] == self.state[1][1] == self.state[2][2]) or (self.state[0][2] == self.state[1][1] == self.state[2][0])) and (self.state[1][1] != ' '):
                winner = self.state[1][1]
            
            return winner

        def __str__(self):
            rows = ['|'.join(self.state[r]) for r in range(3)]
            return '\n-----\n'.join(rows)
        
if __name__ == '__main__':
    print("Starting new TicTacToe game!\n")
    play_against_computer = input("Play against the computer? Type Y for yes and N for no: ")
    print("")
    if play_against_computer.lower() == 'y':
        computer_player = input("Should the computer play first (X) or second (O)?: ")
        response = computer_player.lower()
        if response == 'x' or response == 'first' or response == '1':
            game = TicTacToe(True, 1)
        else:
            game = TicTacToe(True, 2)
    else:
        game = TicTacToe(False, 0)

    while not game.finished:
        game.play_round()

    game.display_result()