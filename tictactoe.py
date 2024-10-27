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
        self._curr_player = self._players[self._curr_player_index]
        self._finished = False

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
        return None
    
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
            return True
        
        def __str__(self):
            rows = ['|'.join(self.state[r]) for r in range(3)]
            return '\n-----\n'.join(rows)