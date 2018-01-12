from random import randint

board = []
board_size = 20

#builds the board
for x in range(board_size):
  board.append(["O"] * board_size)

#formats the board
def print_board(board):
  for row in board:
    print " ".join(row)

#prints inital board 
print_board(board)

#generates the row for the ship
def random_row(board):
  return randint(0, len(board) - 1)

#generates the column for the ship
def random_col(board):
  return randint(0, len(board[0]) - 1)

def ship_startLoc(size):
  seedX = random_row(board)
  seedY = random_row(board)
  if(seedX + size >= board_size):
    seedX = board_size - size
  if(seedY + size >= board_size):
    seedY = board_size - size
  battle_ship = [seedX, seedY]
  print battle_ship
 
print "battle_ship: "
ship_startLoc(5)
print "fridgate: " 
ship_startLoc(3)
print "Destroyer: " 
ship_startLoc(4)
print "Gunner: "
ship_startLoc(3)

"""Need a method here to take a ship size, generate a seed and then randomly set the ship to the board either in the x direction or y direction also return ship size on hit"""

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(board_size - 1):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  
  #win conditions
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    #out of bounds conditions
    if(guess_row < 0 or guess_row > board_size) or (guess_col < 0 or guess_col > board_size):
      print "Oops, that's not even in the ocean."
    #already guessed condition
    elif(board[guess_row-1][guess_col-1] == "X"):
      print "You guessed that one already."
    else:
      if turn == 3:
        print "Game Over"
      print "You missed my battleship!"
      board[guess_row-1][guess_col-1] = "X"
    print_board(board)
    
"""Extra Credit
You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!"""
