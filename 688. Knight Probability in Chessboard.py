""" On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving. """



class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def subprob(a,b,prev):
            if (a<0 or a>=N) or (b<0 or b>=N):
                return 0
            return prev[a][b]

        if K==0: return 1
        if N <= 2: return 0

        moves = [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]


        prev = [[1]*N for x in range(N)]

        for left in range(1,K+1):
            curr = [[None]*N for x in range(N)]
            for i in range(N):
                for j in range(N):
                    curr[i][j] = sum([subprob(i+m[0],j+m[1],prev) for m in moves])/8
            prev = curr

        return curr[r][c]
