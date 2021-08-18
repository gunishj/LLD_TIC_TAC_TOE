# Design A tic Tac Toe Game 
# Matrix Can be n * n 
# There can be only Two Player 
# Draw, Win P1, win by p2
# By Default P1 -> X P2 --> 0
def check_completion(board,i,j,flg):
    # row check
    n = len(board)
    cnt = 0

    for itr_row in range(len(board)):        
        if flg == 'x':
            if board[itr_row][j] == 0:
                cnt+=1
                continue
            else:
                break
        if flg == '0':
            if board[itr_row][j] == 1:
                continue
            else:
                break
    if cnt ==n:
        return True

    cnt =0 
    # column check
    for itr_col in range(len(board[0])):        
        if flg == 'x':
            if board[i][itr_col] == 0:
                cnt+=1
                continue
            else:
                break
        if flg == '0':
            if board[i][itr_col] == 1:
                continue
            else:
                break
    if cnt ==n:
        return True 
    
    cnt =0

    # negative slope diagnol
    
    for itr_col in range(len(board[0])):        
        if flg == 'x':
            if board[itr_col][itr_col] == 0:
                cnt+=1
                continue
            else:
                break
        if flg == '0':
            if board[i][itr_col] == 1:
                continue
            else:
                break
    if cnt ==n:
        return True
    
    # postive slope diagnol
    cnt =0
    for itr_col in range(len(board[0])):        
        if flg == 'x':
            if board[n-itr_col-1][itr_col] == 0:
                cnt+=1
                continue
            else:
                break
        if flg == '0':
            if board[i][itr_col] == 1:
                continue
            else:
                break
    if cnt ==n:
        return True
    
    return False


        




def main():
    print("plese enter the size of board")
    n = int(input())
    board = [ [-1] * n for i in range(n) ]
    flg = '0'
    i,j =0,0
    while(True):
        if flg =='0':
            print("player1 please enter your input and select the i")
            i = int(input())            
            print("player1 please enter your input and select the j")
            j = int(input())
            flg = 'x'
            if board[i][j] == -1:
                board[i][j] = 0
            else:
                print("player 1 you need to enter again your cordinates as it's already filled")
                flg ='0'
        elif flg == 'x':
            print("player2 please enter your input and select the i")
            i = int(input())
            
            print("player2 please enter your input and select the j")
            j = int(input())
            flg = '0'
            if board[i][j] == -1:
                board[i][j] = 1
            else:
                print("player 2 you need to enter again your cordinates as it's already filled")
                flg ='x'
        if check_completion(board,i,j,flg):
            if flg == 'x':
                print("player 1 has won")
            else:
                print("player 2 has won")
            return 
        

if __name__=='__main__':
    main()
    # [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
