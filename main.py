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
  global row
  print("\n")
  for row in board: 
    print("|{0}|{1}|{2}|{3}|{4}|{5}|".format(*row)) # From https://www.geeksforgeeks.org/python-star-or-asterisk-operator/
  
def user_rowCol_selection():
  display_board()
  
  print("\nEvery letter represents a row and column (only reaches F for each; rows then columns). Ex: AB. You CANNOT skip a row and must start from the bottom row. Choose whatever column you want.")
  def user_rowCol_selection_x():
    global selected_col_x
    print("\nX's turn!")
    
    row_selection = input("\nChoose Row (letter): ").upper()
    col_selection = input("\nChoose Column (letter): ").upper()
  
    if row_selection == 'A':
      selected_row = 0
    elif row_selection == 'B':
      selected_row = 1
    elif row_selection == 'C':    #selects row
      selected_row = 2
    elif row_selection == 'D':
      selected_row = 3
    elif row_selection == 'E':
      selected_row = 4
    elif row_selection == 'F':
      selected_row = 5
    

    if col_selection == 'A':
      selected_col_x = 0
    elif col_selection == 'B':  #selects columns
      selected_col_x = 1
    elif col_selection == 'C':
      selected_col_x = 2
    elif col_selection == 'D':
      selected_col_x = 3
    elif col_selection == 'E':
      selected_col_x = 4
    elif col_selection == 'F':
      selected_col_x = 5
    else:
      print("Invalid input!") 
      user_rowCol_selection_x()
    try:
      if board[selected_row][selected_col_x] == "   ":    
        board[selected_row][selected_col_x] = ' x '
        display_board()#Indices by selected row and col variables if the place they selected wasn't selected
        
      else:
        print("\nThere is already something here. Try again.")
        user_rowCol_selection_x()
      
    except Exception:
      pass
    
  def user_rowCol_selection_o():
    global selected_col_o
    print("\nO's turn!")
    
    row_selection = input("\nChoose Row (letter): ").upper()
    col_selection = input("\nChoose Column (letter): ").upper() #Input to choose their rows and columns

    if row_selection == 'A':
      selected_row = 0
    elif row_selection == 'B':      #Almost the same as X but X is replaced with O
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
      selected_col_o = 0
    elif col_selection == 'B':
      selected_col_o = 1
    elif col_selection == 'C':
      selected_col_o = 2
    elif col_selection == 'D':
      selected_col_o = 3
    elif col_selection == 'E':
      selected_col_o = 4
    elif col_selection == 'F':
      selected_col_o = 5
      
    else:
      print("Invalid input!")
      user_rowCol_selection_o()

    try:
      if board[selected_row][selected_col_o] == "   ":    
        board[selected_row][selected_col_o] = ' o '
        
      else:
        print("\nThere is already something here. Try again.")
        user_rowCol_selection_o()
    except Exception:
      pass


  user_rowCol_selection_x()
  user_rowCol_selection_o()

def exit_program():
  sure = input("Are you sure you want to exit the program (Y/N): ")
  if sure == "Y":
    global isUsed
    isUsed = False
  elif sure == "N":
    user_rowCol_selection()
  else:
    print("Invalid input! Try again.")
    exit_program()

def check_win():
  def restart():
    global board
    board = [
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
  ["   ","   ","   ","   ","   ","   "],
] # From https://replit.com/@AndrewFlye/Connect4-Board-Example#main.py
    user_rowCol_selection()  # do not forget to tab
 
  def exit_continue():
  
      exit_option = str(input("\nDo you want to restart the game or quit? (choose 1 or 2) "))
      if exit_option == "1":
        restart()
      elif exit_option == "2":
        exit_program()
      else: 
        print("\nInvalid option.")
        exit_continue()
      
      
  for row in board: # checks every row
    for x in range(3):
      x = x+1
      if board[x][0] == board[x][1] == board[x][2] == board[x][3] != board['   '][x]:
        print("\nX won!")
        exit_continue()
      else: 
        pass
    for x in range(6): # moves six times because it is too difficult to do col in row
      x = x+1
      if board[0][x] == board[1][x] == board[2][x] == board[3][x] == board[4][x] == board[5][x] != board[x]["   "]:
        print("\nX won!")
        exit_continue()
      else: 
        pass
      
        
def main(): #main function (where every function will go)
  while isUsed:
    user_rowCol_selection()
  

main()