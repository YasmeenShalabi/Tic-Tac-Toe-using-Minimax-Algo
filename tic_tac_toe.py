#Tic Tac Toe AI Using :Minimax Algorithm-> a recursive approach used for making decisions in turn-based games like tic tac toe
#The AI will simulate all possible moves, evaluate them, and choose the best one to either maximize its own chance of winning, or minimize the players chance of winning

#Define the board as a list
board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe board represented as a 1D list

#Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]: #Divides the 1D list into 3 rows each containing 3 elements and prints them as row seperated by vertical bars to mimic a tic tac toe board ....[start index: end index (non-inclusive)]
        print('| ' + ' | '.join(row) + ' |') #takes the list and inserts '|' between each element

#Function to check if there is a winner
def check_winner(board, player):
    win_conditions= [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  #Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #Columns
        [0, 4, 8], [2, 4, 6]              #Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

#Function to check if the board is full
#helps detect draws and tells Minimax when there are no future moves left to explore
def is_board_full(board):
    return ' ' not in board #returns True if board has no empty spaces, otherwise False

#Function to evaluate the board for the Minimax algorithm
#The AI will try to find paths leading toward 1 while avoiding paths leading toward -1
def evaluate(board):
    if check_winner(board, 'O'):  #AI is 'O'
        return 1        #returns 1 if the AI wins
    elif check_winner(board, 'X'):  #Human is 'X'
        return -1       #returns -1 if human wins
    else:
        return 0        #returns 0 if game is still ongoing or ends in a draw

#Minimax function to explore future possibilities
def minimax(board, depth, is_maximizing): #recursively evaluate possible moves; if is_maximizing is true =>AI's turn and algo tries to maximize the score; if false=>human players turn algo tries to minimize the score
    #depth => how many moves into the hypothetical future Minimax has traveled
    score = evaluate(board)

    if score == 1 or score == -1 or is_board_full(board): #base case
        return score

    if is_maximizing: #AI's turn
        best_score = -float('inf') #start with worst possible score so anything is better
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' #not an actual final move, AI temporarily puts an O there to see what happens only
                #using max bec max(-1,0,1)= 1 so AI would prefer move C
                best_score = max(best_score, minimax(board, depth + 1, False)) #False because after O moves, it becomes the humans hypothetical turn
                board[i] = ' ' #after seeing what happens, undo the hypothetical move to test another possibility
        return best_score
    else: #Human's turn
        best_score = float('inf')
        for i in range(9): #human tests each available position
            if board[i] == ' ':
                board[i] = 'X' #Human makes a move
                best_score = min(best_score, minimax(board, depth + 1, True)) #Human tries to make the AI's score as small as possible
                board[i] = ' ' #undo move
        return best_score

#Function to find the best move for the AI based on minimax
#Tries each possible current AI move, calls Minimax to predict its outcome, and picks the highest-scoring one
def find_best_move(board):
    best_value = -float('inf')
    best_move = -1  #board position

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' #AI makes a move
            move_value = minimax(board, 0, False) #false since its now humans turn
            board[i] = ' ' #undo move

            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move

#Main game loop
#Controls the actual game by alternating between the real human move and the AI's chosen move
def play_game():
    while True:
        print_board(board)

        #Player move
        player_move = int(input("Enter your move (1-9)")) - 1
        if board[player_move] != ' ':
            print("invalid move! Try again.")
            continue #stop this iteration and go back to beginning
        board[player_move] = 'X'

        #Check if player won
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        #Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        #AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'

        #Check if AI won
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        #Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

#Start the game
play_game()