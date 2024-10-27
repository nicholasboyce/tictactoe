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
        x, y = None
        if computer:
            if cpuPlayer - 1: #i.e. player X is the computer
                x = self.Player('X', computer)
                y = self.Player('Y', not computer)
            else:
                x = self.Player('X', not computer)
                y = self.Player('Y', computer)
        else: #neither is computer
            x = self.Player('X', not computer)
            y = self.Player('Y', not computer)
        return [x, y]

    def play_round(self) -> None:
        player = self._curr_player
        marked = False

        while not marked:
            choice = player.make_choice()
            marked = self._board.mark(choice, player.symbol)

        self._curr_player_index = (self._curr_player_index + 1) % 2
        self._curr_player = self._players[self._curr_player_index]
        return None
    
    def display_result(self) -> None:
        pass
    
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
        
        def _is_valid(self, row: int, col: int) -> bool:
            """Checks validity of given position to be marked."""
            if row >= 3 or col >= 3:
                return False
            elif self.state[row][col] != ' ':
                return False
            return True

        def __str__(self):
            rows = ['|'.join(self.state[r]) for r in range(3)]
            return '\n-----\n'.join(rows)
        
if __name__ == '__main__':
    print("Starting new TicTacToe game!\n")
    play_against_computer = input("Play against the computer? Type Y for yes and N for no: ")
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