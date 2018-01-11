from random import randint

board = []

#builds the board
for x in range(5):
  board.append(["O"] * 5)

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

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  
  #win conditions
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    #out of bounds conditions
    if(guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
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
You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements�maybe you can think of some more!

Make multiple battleships: you'll need to be careful because you need to make sure that you don�t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you�ll need to make sure you don�t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!"""