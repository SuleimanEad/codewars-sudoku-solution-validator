def valid_solution(board):
    numlist = list(range(1,10))
    if 0 in board:
        return False
    for line in board:
        if sorted(line) != numlist:
            return False
    transboard = list(map(list, zip(*board)))
    for tline in transboard:
        if sorted(tline) != numlist:
            return False
    for x in range(2):
        for y in range(2):
            block = board[3*x][3*y:3*y+3] + board[3*x+1][3*y:3*y+3] + board[3*x+2][3*y:3*y+3]
            if sorted(block) != numlist:
                return False
    return True
