class TicTacToe:
    """A tic-tac-toe game."""

    def __init__(self):
        """Create a new game instance.

        The initial board created is empty.
        The first player is always X.
        """
        self._board = self.Board()

    class Board:
        """A 3x3 board for tic-tac-toe."""

        def __init__(self):
            """Create a new game board.

            state: a multidimensional array representation of the current board
            """
            self.state = [[0] * 3 for i in range(3)]
        
        def mark(position: list, player: str) -> bool:
            """Marks a given position on the board with the player's corresponding symbol.

            Returns True if the given position is valid and successfully marked. Otherwise, returns False.
            """
            return True