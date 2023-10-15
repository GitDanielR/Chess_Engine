class Chess_Piece:
    # Chess piece image size (in pixels)
    img_size = 50

    # Chess piece class information
    # x_pos = x val
    # y_pos = y val
    # color = 0 if black, 1 if white
    def __init__(self, x_pos, y_pos, type=True):
        self.x = x_pos
        self.y = y_pos
        self.color = type
        
class King(Chess_Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.check = False
        self.img = "white_king.png" if color else "black_king.png"
        
    def in_check(self, check):
        self.check = check
        
class Queen(Chess_Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.img = "white_queen.png" if color else "black_queen.png"
        
class Bishop(Chess_Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.img = "white_bishop.png" if color else "black_bishop.png"
        
class Knight(Chess_Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.img = "white_knight.png" if color else "black_knight.png"
        
class Rook(Chess_Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.img = "white_rook.png" if color else "black_rook.png"
        
class Pawn(Chess_Piece):
    def __init__(self, x_pos, y_pos, color, has_moved=False):
        super().__init__(x_pos, y_pos, color)
        self.img = "white_pawn.png" if color else "black_pawn.png"

    def moved(self):
        self.has_moved = True