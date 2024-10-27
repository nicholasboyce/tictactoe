class TicTacToe:
    """A tic-tac-toe game."""

    def __init__(self):
        """Create a new game instance.

        The initial board created is empty.
        The first player is always X.
        """
        self._board = self.Board()
    

    class Board:

        def __init__(self):
            self.state = [[0] * 3 for i in range(3)]
        
        def mark()