board = [
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
] # From https://replit.com/@AndrewFlye/Connect4-Board-Example#main.py


rowA = board[0]
rowB = board[1] # columns are part of the list of board
rowC = board[2]
rowD = board[3]
rowE = board[4]
rowF = board[5]
row = rowA or rowB or rowC or rowD or rowE or rowF

colA = row[0]  # columns are part of the list of row
colB = row[1]
colC = row[2]
colD = row[3]
colE = row[4]
colF = row[5]
col = colA or colB or colC or colD or colE or colF

# Displays board in visually-pleasing way
def display_board():
  for row in board: 
    print("|{0}|{1}|{2}|{3}|{4}|{5}|".format(colA, colB, colC, colD, colE, colF))

 

def main(): #main function (where every function will go)
  display_board()

main()