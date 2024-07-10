class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"

        lastPlayer = (len(moves) - 1) % 2 # 0 means A, 1 means B
        playersMoves = [moves[x] for x in range(len(moves)) if x % 2 == lastPlayer]

        lx, ly = playersMoves[-1][0], playersMoves[-1][1]

        if all(e in playersMoves for e in [[0,ly],[1,ly],[2,ly]]):
            return "A" if lastPlayer == 0 else "B"
        
        if all(e in playersMoves for e in [[lx,0],[lx,1],[lx,2]]):
            return "A" if lastPlayer == 0 else "B"

        if all(e in playersMoves for e in [[0,0],[1,1],[2,2]]):
            return "A" if lastPlayer == 0 else "B"

        if all(e in playersMoves for e in [[0,2],[1,1],[2,0]]):
            return "A" if lastPlayer == 0 else "B"

        return "Draw" if len(moves) == 9 else "Pending"
        