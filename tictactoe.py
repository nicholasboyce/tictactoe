import time

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
            if cpuPlayer - 1: #i.e. player X is the computer
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
            return self._return_best_choice(self._board.state)
    
    def _return_best_choice(self, board: list[list[str]]) -> list:
        # find all possible moves from current board
        # for each available position mark the board
        # return and store the value of the marked board, associate it with the position
        # unmark the board
        # move on to the next position
        # return the optimal position
        pass

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

        def make_choice() -> list:
            pass

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
        if response == 'x' or response == 'first':
            game = TicTacToe(True, 1)
        else:
            game = TicTacToe(True, 2)
    else:
        game = TicTacToe(False, 0)

    while not game.finished:
        game.play_round()

    game.display_result()