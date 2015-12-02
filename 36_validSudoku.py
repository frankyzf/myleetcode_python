__author__ = 'feng'

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ss = set(map(lambda x: x, "987654321"))
        for i in range(0,9):
            aa = filter(lambda x:x != '.', board[i])
            cell = set()
            for a in aa:
                if a in cell:
                    return False
                cell.add(a)
            if cell.difference(ss):
                return False
        for j in range(0, 9):
            cell = set()
            for i in range(0,9):
                if board[i][j] != '.':
                    if board[i][j] in cell:
                        return False
                    cell.add(board[i][j])
            if cell.difference(ss):
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                cell = set()
                for m in range(3*i, 3*i+3):
                    for n in range(3*j, 3*j+3):
                        if board[m][n] != '.':
                            if board[m][n] in cell:
                                return False
                            cell.add(board[m][n])
                if cell.difference(ss):
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    data = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    board = []
    for r in data:
        board.append(list(map(lambda x: x, r)))
    for d in board:
        print d
    print s.isValidSudoku(board)
