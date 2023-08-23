
class piece:
    def __init__(self, icon):
        self.icon = icon
    def __str__(self):
        return f"{self.icon}"
    def __repr__(self):
        return f"{self.icon}"

bP = piece("♟")
bN = piece("♞")
bB = piece("♝")
bR = piece("♜")
bQ = piece("♛")
bK = piece("♚")

wP = piece("♙")
wN = piece("♘")
wB = piece("♗")
wR = piece("♖")
wQ = piece("♕")
wK = piece("♔")

board = [[ bR, bN, bB, bQ, wQ, bB, bN, bR],
         [ bP, bP, bP, bP, bP, bP, bP, bP],
         ["□","■","□","■","□","■","□","■",],
         ["■","□","■","□","■","□","■","□",],
         ["□","■","□","■","□","■","□","■",],
         ["■","□","■","□","■","□","■","□",],
         [ wP , wP, wP, wP, wP, wP, wP, wP],
         [ wR , wN, wB, wQ, wK, wB, wN, wRz]]


def printBoard:
   
