board = [
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
] # From https://replit.com/@AndrewFlye/Connect4-Board-Example#main.py

isUsed = True

# Displays board in visually-pleasing way
def display_board():
  for row in board: 
    print("|{0}|{1}|{2}|{3}|{4}|{5}|".format(*row)) # From https://www.geeksforgeeks.org/python-star-or-asterisk-operator/

def user_rowCol_selection():
  print("\nEvery letter represents a row and column (only reaches F for each; rows then columns). Ex: AB. You CANNOT skip a row and must start from the bottom row. Choose whatever column you want.")
  def user_rowCol_selection_x():
    
    row_selection = input("\nChoose Row (letter): ").upper()
    col_selection = input("\nChoose Column (letter): ").upper()

  
    if row_selection == 'A':
      selected_row = 0
    elif row_selection == 'B':
      selected_row = 1
    elif row_selection == 'C':
      selected_row = 2
    elif row_selection == 'D':
      selected_row = 3
    elif row_selection == 'E':
      selected_row = 4
    elif row_selection == 'F':
      selected_row = 5

    if col_selection == 'A':
      selected_col = 0
      board[selected_row][selected_col] = ' x '
    elif col_selection == 'B':
      selected_col = 1
      board[selected_row][selected_col] = ' x '
    elif col_selection == 'C':
      selected_col = 2
      board[selected_row][selected_col] = ' x '
    elif col_selection == 'D':
      selected_col = 3
      board[selected_row][selected_col] = ' x '
    elif col_selection == 'E':
      selected_col = 4
      board[selected_row][selected_col] = ' x '
    elif col_selection == 'F':
      selected_col = 5
      board[selected_row][selected_col] = ' x '

  def user_rowCol_selection_o():
    
    row_selection = input("\nChoose Row (letter): ").upper()
    col_selection = input("\nChoose Column (letter): ").upper()

  
    if row_selection == 'A':
      selected_row = 0
    elif row_selection == 'B':
      selected_row = 1
    elif row_selection == 'C':
      selected_row = 2
    elif row_selection == 'D':
      selected_row = 3
    elif row_selection == 'E':
      selected_row = 4
    elif row_selection == 'F':
      selected_row = 5

    if col_selection == 'A':
      selected_col = 0
      board[selected_row][selected_col] = ' o '
    elif col_selection == 'B':
      selected_col = 1
      board[selected_row][selected_col] = ' o '
    elif col_selection == 'C':
      selected_col = 2
      board[selected_row][selected_col] = ' o '
    elif col_selection == 'D':
      selected_col = 3
      board[selected_row][selected_col] = ' o '
    elif col_selection == 'E':
      selected_col = 4
      board[selected_row][selected_col] = ' o '
    elif col_selection == 'F':
      selected_col = 5
      board[selected_row][selected_col] = ' o '


  user_rowCol_selection_x()
  user_rowCol_selection_o()
def main(): #main function (where every function will go)
  while isUsed:
    display_board()
    user_rowCol_selection()
  

main()