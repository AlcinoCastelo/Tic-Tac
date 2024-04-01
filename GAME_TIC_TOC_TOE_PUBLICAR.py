
def printBoard(board):
    for row in board:
        print(" | ". join(row))
        print("-"*9)

##board = [[' ', ' ', ' '],
##         [' ', ' ', ' '],
##         [' ', ' ', ' ']]
def checkWins(board):
    #check horizontal
    for row in board:
        if row[0]==row[1]==row[2]!= ' ':
            return row[0]
    #check vertical
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col]!= ' ':
            return board[0][col]
    if board[0][0]==board[1][1]==[2][2]!=' ':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!= ' ':
        return board[0][2]
    return None
def main():
    board = [ [' ' for _ in range(3)] for _ in range(3)]
    player = "X"
    sum = 0
    while True:
        printBoard(board)
        if sum %2 == 0:
            row = int(input("Enter row for [X]: (0,1,2):"))
            col = int(input("Enter col for [X]: (0,1,2):"))
        else:
            row = int(input("Enter row for [O]: (0,1,2):"))
            col = int(input("Enter col for [O]: (0,1,2):"))
        if board[row][col]==' ':
            board[row][col]= player
            if checkWins(board):
                printBoard(board)
                print("player wins:", player)
                break
            elif all(board[i][j]!= ' ' for i in range(3) for j in range(3)):
                printBoard(board)
                print("The game is tie!!!")
                break
            player = "O" if player== "X" else "X"
        else:
            print("There already existe value")
        sum+=1
main()
                
            
                
            
        
