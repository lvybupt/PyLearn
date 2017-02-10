'''
python 算法书 page 78  棋盘覆盖问题

部分矩阵或数组在作为函数参数的时候,需要将索引传入。所以cover2失败了

'''

def cover(board, lab = 1, top = 0, left = 0, side = None):
    if side is None: side =len(board)

    #Side length of sub board
    s = side //2

    #Offsets for outer/inner squares of subboards:
    offsets = (0,-1),(side-1,0)

    for dy_outer, dy_inner in offsets:
        for dx_outer,dx_inner in offsets:
            # If the outer corner is not set...

            if not board[top+dy_outer][left+dx_outer]:
                # ...laber the inner corner:
                board[top+s+dy_inner][left+s+dx_inner]=lab


    #Next label:
    lab += 1
    if s > 1:
        for dy in [0,s]:
            for dx in [0,s]:
                # Recursive calls if s is at least 2:
                lab = cover(board,lab,top+dy,left+dx,s)

    # Return the next available laber
    return lab

'''
def cover2(board,num = 1):
    board_len = len(board)
    if board_len ==2:
        for i in range(board_len):
            for j in range(board_len):
                if board[i][j] ==0:
                    board[i][j] == num;
        num +=1
        return num

    point_loc = (0,board_len//2-1),(board_len,board_len//2 )
    for i,m in point_loc:
        for j,n in point_loc:
            if board[i][j] ==0:
                board[m][n] == num

    section_loc = (0,board_len//2-1),(board_len//2,board_len)

    for i,j in section_loc:
        for m,n in section_loc:
            num = cover2(board[i:j][m,n],num+1)
    return num
'''














if __name__ == '__main__':
    board = [[0]*8 for i in range(8)]
    board[7][7] = -1
    for row in board:
        # print(row)
        print((" %2i" * 8) % tuple(row))
    #print(board)
    print(cover(board))
    for row in board:
        #print(row)
        print((" %2i"*8) % tuple(row))
