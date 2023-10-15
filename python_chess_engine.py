import pygame
import sys
import chess_piece

# Create Pygame
chess_board = pygame.init()

# Length = X
# Width = Y
# Do not make (width > length) or else you're weird and my program
# will make fun of you (not work right). Otherwise choose whatever
# size you want. Didn't think of that before making this.
LENGTH = 800
WIDTH = 800

# Make sure that the dimensions of the screen will allow for 1 dimension to be
# fully consumed by the chess board. No random space.
assert(min(LENGTH, WIDTH) % 8 == 0)

# Define chess board size stats
square_width = square_height = WIDTH / 8
x_offset = (LENGTH / 2) - 4 * square_width

# Define piece highlight radius
highlight_radius = int(min(square_width, square_height) / 2)
highlight_width = int(highlight_radius / 4)

# Set image size as a function of the square size. Center the image
img_size = square_height / 2
center_square = img_size / 2

# Define colors
board_green = (118, 150, 86)
board_light_green = (186, 202, 68)
black = (0, 0, 0)
white = (255, 255, 255)
red = (224, 105, 96)

# Make the pygame window
window = pygame.display.set_mode((LENGTH, WIDTH))
pygame.display.set_caption("Chess")

# Make chess board
def color_board():
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(window, board_green, (x_offset + j * square_width, i * square_height, square_width, square_height))
            else:
                pygame.draw.rect(window, board_light_green, (x_offset + j * square_width, i * square_height, square_width, square_height))

# Place chess pieces on the board and make lists of each teams pieces
white_pieces = []
black_pieces = []
def make_pieces():
    for i in range(8):
        for j in range(8):
            # Black pawns
            if i == 1:
                if j == 0:
                    black_pawn_0 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_0)
                elif j == 1:
                    black_pawn_1 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_1)
                elif j == 2:
                    black_pawn_2 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_2)
                elif j == 3:
                    black_pawn_3 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_3)
                elif j == 4:
                    black_pawn_4 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_4)
                elif j == 5:
                    black_pawn_5 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_5)
                elif j == 6:
                    black_pawn_6 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_6)
                else:
                    black_pawn_7 = chess_piece.Pawn(j * square_height, i * square_width, False)
                    black_pieces.append(black_pawn_7)
            # White pawns
            if i == 6:
                if j == 0:
                    white_pawn_0 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_0)
                elif j == 1:
                    white_pawn_1 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_1)
                elif j == 2:
                    white_pawn_2 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_2)
                elif j == 3:
                    white_pawn_3 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_3)
                elif j == 4:
                    white_pawn_4 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_4)
                elif j == 5:
                    white_pawn_5 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_5)
                elif j == 6:
                    white_pawn_6 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_6)
                else:
                    white_pawn_7 = chess_piece.Pawn(j * square_height, i * square_width, True)
                    white_pieces.append(white_pawn_7)
            # Black pieces
            if i == 0:
                # Rooks
                if j == 0:
                    black_rook_0 = chess_piece.Rook(j * square_height, 0, False)
                    black_pieces.append(black_rook_0)
                if j == 7:
                    black_rook_1 = chess_piece.Rook(j * square_height, 0, False)
                    black_pieces.append(black_rook_1)
                # King
                if j == 4:
                    black_king = chess_piece.King(j * square_height, 0, False)
                    black_pieces.append(black_king)
                # Queen
                if j == 3:
                    black_queen = chess_piece.Queen(j * square_height, 0, False)
                    black_pieces.append(black_queen)
                # Bishops
                if j == 2:
                    black_bishop_0 = chess_piece.Bishop(j * square_height, 0, False)
                    black_pieces.append(black_bishop_0)
                if j == 5:
                    black_bishop_1 = chess_piece.Bishop(j * square_height, 0, False)
                    black_pieces.append(black_bishop_1)
                # Knights
                if j == 1:
                    black_knight_0 = chess_piece.Knight(j * square_height, 0, False)
                    black_pieces.append(black_knight_0)
                if j == 6:
                    black_knight_1 = chess_piece.Knight(j * square_height, 0, False)
                    black_pieces.append(black_knight_1)
            # White pieces
            if i == 7:
                # Rooks
                if j == 0:
                    white_rook_0 = chess_piece.Rook(j * square_height, i * square_width, True)
                    white_pieces.append(white_rook_0)
                if j == 7:
                    white_rook_1 = chess_piece.Rook(j * square_height, i * square_width, True)
                    white_pieces.append(white_rook_1)
                # King
                if j == 4:
                    white_king = chess_piece.King(j * square_height, i * square_width, True)
                    white_pieces.append(white_king)
                # Queen
                if j == 3:
                    white_queen = chess_piece.Queen(j * square_height, i * square_width, True)
                    white_pieces.append(white_queen)
                # Bishops
                if j == 2:
                    white_bishop_0 = chess_piece.Bishop(j * square_height, i * square_width, True)
                    white_pieces.append(white_bishop_0)
                if j == 5:
                    white_bishop_1 = chess_piece.Bishop(j * square_height, i * square_width, True)
                    white_pieces.append(white_bishop_1)
                # Knights
                if j == 1:
                    white_knight_0 = chess_piece.Knight(j * square_height, i * square_width, True)
                    white_pieces.append(white_knight_0)
                if j == 6:
                    white_knight_1 = chess_piece.Knight(j * square_height, i * square_width, True)
                    white_pieces.append(white_knight_1)

# Place the pieces images on the board
def place_pieces():
    for white in white_pieces:
        img = pygame.transform.scale(pygame.image.load(white.img), (img_size, img_size))
        window.blit(img, (white.x + x_offset + center_square, white.y + center_square))
    for black in black_pieces:
        img = pygame.transform.scale(pygame.image.load(black.img), (img_size, img_size))
        window.blit(img, (black.x + x_offset + center_square, black.y + center_square))

# Check if (x1, y1) and (x2, y2) are in the same square on the chess board
def in_bounds(x1, y1, x2, y2) -> bool:
    x_diff = x1 - (x1 % square_width)
    y_diff = y1 - (y1 % square_height)
    x2 -= x_diff
    y2 -= y_diff
    return x2 >= 0 and x2 < square_width and y2 >= 0 and y2 < square_height

# Returns the lowest coords of a square given (x, y) inside the square
def img_pos(x, y):
    # Make sure pos on the board
    if (x < x_offset or x >= x_offset + 8 * square_width or y < 0 or y > WIDTH):
        return None
    new_x = (x // square_width) * square_width
    new_y = (y // square_height) * square_height
    return new_x, new_y 

# Return white and black pieces at coordinate.
def find_pieces(mouse_x, mouse_y):
    w_piece = list(filter(lambda obj: in_bounds(mouse_x, mouse_y, obj.x, obj.y), white_pieces))
    b_piece = list(filter(lambda obj: in_bounds(mouse_x, mouse_y, obj.x, obj.y), black_pieces))
    return (w_piece, b_piece)

# Highlight piece at x and y position
def highlight(x, y):
    pygame.draw.circle(window, red, (x, y), highlight_radius, highlight_width)

# Pawn valid moves
#def valid_pawn(self, cur_x, cur_y, next_x, next_y):
#        y_move_size = 1 if self.has_moved else 2
#        return cur_x == next_x and img_pos(cur_x, cur_y, next_x, next_y) == y_move_size

# Set up chess board
window.fill(white)              
color_board()
make_pieces()
place_pieces()

# Start off with player/white to move
move = True
# No piece selected at start of game
piece = None

# Main game loop
while True:
    # Get the events in past game loop
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check user input for moving pieces on board.
        # Click to select piece and click to deselect/place.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get pos of click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # The chess piece positions are defined to start at (0, 0) and not the actual location
            # of the chess board... sorry lol
            mouse_x -= x_offset
            # If you have already selected a piece
            if piece:
                # Check if deselecting
                if in_bounds(mouse_x, mouse_y, piece.x, piece.y):
                    print('Piece square selected. Choose different square')
                else:
                    # Coords to move piece to
                    piece_x, piece_y = img_pos(mouse_x, mouse_y)
                    # Make sure valid
                    if piece_x:
                        # Find piece(s) at new location
                        white_piece, black_piece = find_pieces(mouse_x, mouse_y)
                        white = white_piece[0] if white_piece else None
                        black = black_piece[0] if black_piece else None
                        # Black takes
                        if white and not move:
                            idx = white_pieces.index(white)
                            white_pieces.pop(idx)
                        # White takes
                        elif black and move:
                            idx = black_pieces.index(black)
                            black_pieces.pop(idx)
                        # Illegal move (ignore/deselect)
                        elif white and move or black and not move:
                            piece = None
                            continue
                        # Move piece
                        piece.x = piece_x
                        piece.y = piece_y
                        # Change whose turn it is
                        move = not move
                # Reset piece
                piece = None
            else:
                # Get the piece at a position.
                white_piece, black_piece = find_pieces(mouse_x, mouse_y)
                # Choose the piece that is being moved.
                piece = white_piece[0] if move and white_piece else black_piece[0] if not move and black_piece else None

    # Update game by redrawing board and pieces in their positions
    color_board()
    place_pieces()

    # Highlight selected piece if there is one. Input = center of the square.
    if piece:
        highlight(int(piece.x + square_width / 2), int(piece.y + square_height / 2))

    pygame.display.flip()
    
    # Set frame rate
    pygame.time.Clock().tick(60)