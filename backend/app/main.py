"""Module instantiating a chess board with standard game logic."""

import chess

def main() -> None:
    """main module to organize tool and initialize instances of board and game logic,
      make connections to databases, frontend, call utils and services, etc."""
    board = chess.Board()

    print(board.legal_moves)
main()
