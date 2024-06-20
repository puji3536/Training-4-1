class Solution(object):
    def solveNQueens(self, n):
        ans=[]
        col=[]
        posdiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        def backtracking(r):
            if r==n:
                l=["".join(i) for i in board]
                ans.append(l)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]="Q"
                col.append(c)
                posdiag.append(r+c)
                negdiag.append(r-c)
                backtracking(r+1)
                board[r][c]='.'
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        backtracking(0)
        return ans